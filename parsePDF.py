import os, glob, re, sys, operator, json, codecs

from english_Ngram import ngram_process
from collections import Counter
from dfilter_fuc import dfilter_fuc



manufacturer_reference_data={}
electronicTerm_reference_data={}

data_after_ngram = {}

#manufacturer_search_result=[]
#electronic_term_search_result=[]
manufacturer_search_result={}
electronic_term_search_result={}


ngram_number = 0



# ---------------- Function Defined ---------------- #

# change to assigned folder and list all PDF filenames
def get_All_TXT_Name(directoryPath):
    os.chdir(directoryPath)
    allTXT = []
    for filename in glob.glob("*.txt"):
        allTXT.append(filename)
    return allTXT

# counting word occurences
def count_word_occurrences(list_of_words):
    return Counter(list_of_words)


def split_string_with_re(txt):
    #pattern1 is select all words except "\n" "\s" "\t" ","
    #pattern1 = re.compile(r'[\w]+[=]?[\']?[\w]+[°C]?\.?[\w]+\.?[\w]+')
    pattern1 = re.compile(r'[\w]*[±]?[-]?[=]?[\']?[\w]*[°C]?\.?[\w]*\.?[\w]*')
    allresult = re.findall(pattern1, txt)

    allresult = list(filter(('').__ne__, allresult))


    for n, i in enumerate(allresult):
        if i[-2:] == '\'s':
            allresult[n] = i[:-2]
        if i[-1] == '.':
            allresult[n] = i[:-1]

    return allresult


def compare_with_target_list(Content_list, Reference_list):

    result=[]
 
    for eachItem in Content_list:
        if eachItem.lower() in [x.lower() for x in Reference_list]:
            if eachItem not in result:
                result.append(eachItem)

    return result



def read_reference_JSONFile(json_name):
    json_file = open(json_name, 'r')
    return json.load(json_file).keys()

def read_reference_TXTFile(txt_name):
    with open(txt_name) as f:
        reference_list = f.read().splitlines()
    return reference_list



def classifiler_reference(reference_list):

#    with open(reference_file_name) as f:
#        reference_list = f.read().splitlines()

    term_max_length = 0
    final_result = {'max_length':0, 'result':{}}

    for item in reference_list:
        item_in_list = item.split(' ')

        # update max term length
        if len(item_in_list) > term_max_length:
            term_max_length = len(item_in_list)
            final_result['max_length'] = term_max_length

        if str(len(item_in_list)) not in final_result['result'].keys():
            final_result['result'][str(len(item_in_list))] = []
        final_result['result'][str(len(item_in_list))].append(item)
    return final_result


def count_occurrence(target_list):
    #remove the duplicated one
    seen = set()
    seen_add = seen.add
    filtered = [x for x in target_list if not (x in seen or seen_add(x))]

    #set a dictionary with keys from target_list No Duplicated result
    result_dic ={ el:0 for el in filtered}

    #count the occurance
    for s in target_list:
        if s in result_dic:
            result_dic[s] = result_dic[s]+1
    
    return result_dic


#remove duplicated item
def remove_duplicated_item(original_dic):
    noDuplicatedDic = {}
    for key,value in original_dic.items():
        if key.lower() not in noDuplicatedDic.keys():
           noDuplicatedDic[key.lower()]=value
        elif key.lower() in noDuplicatedDic.keys():
           newValue = noDuplicatedDic[key.lower()] + value
           noDuplicatedDic[key.lower()] = newValue

    return noDuplicatedDic




# ---------------- Main Program Start ---------------- #

##### 1. read file.txt to string variable

if len(sys.argv) < 2:
    #no argument
    print('please assign some arguments and try again. ex: python3 parsePDF.py filename.txt')
    exit(1)


# get reference data:
### manufacturer.txt
manufacturer_list = read_reference_TXTFile('manufacturer_list.txt')

electriIndex_list = read_reference_JSONFile('index.json')


manufacturer_reference_data = classifiler_reference(manufacturer_list)
electronicTerm_reference_data=classifiler_reference(electriIndex_list)

maxLength_in_mRef = manufacturer_reference_data['max_length']
maxLength_in_eRef = electronicTerm_reference_data['max_length']

if maxLength_in_mRef > maxLength_in_eRef:
    ngram_number = maxLength_in_mRef
else:
    ngram_number = maxLength_in_eRef    

#print(ngram_number)


#read file
with open(sys.argv[1]) as f:
     original_texts = f.read()


#fullText = re.sub("[-―･\n–&:(),\"”“/]", " ", original_texts)
fullText = re.sub("[･\n&:(),\"”“/]", " ", original_texts)
#fullText = re.sub("[-―･\n–&:]"," ", fullText)


# -------- One word -------- 
#type(filted_words) = List
filtered_words = split_string_with_re(fullText)
one_word_occurrence = count_word_occurrences(filtered_words)


#type(filteredwords2String) = String
filteredwords2String = ' '.join(filtered_words)





# gether N-Gram data:
for i in range(1, ngram_number+1):
    if i == 1:
        #data_after_ngram[str(i)] = filtered_words
        data_after_ngram[str(i)] = one_word_occurrence
    else:
        #data_after_ngram[str(i)] = ngram_process(filteredwords2String, i).keys()
        data_after_ngram[str(i)] = ngram_process(filteredwords2String, i)




# get manufacturer index result:

print('--------------------------------------------')
for i in range(1, manufacturer_reference_data['max_length']+1):
    compare_result = compare_with_target_list(data_after_ngram[str(i)].keys(), manufacturer_reference_data['result'][str(i)])

    for each in compare_result:
        manufacturer_search_result[each] = data_after_ngram[str(i)][each]

manufacturer_search_result = remove_duplicated_item(manufacturer_search_result)

print('Searching Manufacturer List:')
print(sorted(manufacturer_search_result.items(), key=lambda x: (-x[1], x[0])))
#for item in manufacturer_search_result.keys():
#    print(item,':',manufacturer_search_result[item])



print('--------------------------------------------')
# get electronic index search result
for i in range(1, electronicTerm_reference_data['max_length']+1):
    compare_result = compare_with_target_list(data_after_ngram[str(i)].keys(), electronicTerm_reference_data['result'][str(i)])

    for each in compare_result:
        electronic_term_search_result[each] = data_after_ngram[str(i)][each]

electronic_term_search_result = remove_duplicated_item(electronic_term_search_result)

print('Searching Electronic Index List:')
print(sorted(electronic_term_search_result.items(), key=lambda x: (-x[1], x[0])))
#for item in electronic_term_search_result.keys():
#    print(item,':',electronic_term_search_result[item])







'''

sorted_ngram = sorted(n_gram_result.items(), key=operator.itemgetter(1))

#count word occurrences
reResult = count_word_occurrences(filtered_words)

exceptList = ['was','were','is','are','not','yes','no','and','to','page','pages','before','over','in','on','then','between','after','with','for','by','table','figure','can','could','from','data','or','if','else','than','be','only','out','datasheet','the','a','an','this','that','these','those','my','yours','his','her','its','our','their','few','little','much','many','lot','lots','of','most','some','any','enough','all','both','half','either','neither','each','every','other','another','such','what','who','where','how','whom','which','will','rather','quite','over', 'do','did', 'does','you','we','it','like','want','they']


for item in exceptList:
    if item in reResult:
       del reResult[item]

'''




