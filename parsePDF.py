import os, glob, re, sys, operator

from english_Ngram import ngram_process
from collections import Counter
from dfilter_fuc import dfilter_fuc


manufacturer_search_result=[]

ngram_number = 2




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
    pattern1 = re.compile(r'[\w]+[=]?[\w]+[°C]?\.?[\w]+\.?[\w]+')
    allresult = re.findall(pattern1, txt)
    return allresult


def compare_with_target_list(compare_file_name, target):
    result=[]

    with open(compare_file_name) as f:
       compare_items_list = f.read().splitlines() 
 
    for eachItem in compare_items_list:
       if eachItem.lower() in [x.lower() for x in target]:
            result.append(eachItem)

    return result





# ---------------- Main Program Start ---------------- #


##### 1. read file.txt to string variable

if len(sys.argv) < 2:
    #no argument
    print('please assign some arguments and try again. ex: python3 parsePDF.py filename.txt')
    exit(1)


#read file
with open(sys.argv[1]) as f:
     original_texts = f.read()


fullText = re.sub("[-―･\n–&:(),\"”“/]", " ", original_texts)

#fullText = re.sub("[-―･\n–&:]"," ", fullText)



#type(filted_words) = List
filtered_words = split_string_with_re(fullText)



#Compare with Manufacturers List
manufacturer_search_result += compare_with_target_list('manufacturer_list.txt', filtered_words)




#type(filteredwords2String) = String
filteredwords2String = ' '.join(filtered_words)



n_gram_result = ngram_process(filteredwords2String, ngram_number)

print('Searching Manufacturer List: ')
manufacturer_search_result += compare_with_target_list('manufacturer_list.txt', n_gram_result.keys())
print(manufacturer_search_result) if len(manufacturer_search_result)!= 0 else print('no found')



sorted_ngram = sorted(n_gram_result.items(), key=operator.itemgetter(1))

#count word occurrences
reResult = count_word_occurrences(filtered_words)

exceptList = ['was','were','is','are','not','yes','no','and','to','page','pages','before','over','in','on','then','between','after','with','for','by','table','figure','can','could','from','data','or','if','else','than','be','only','out','datasheet','the','a','an','this','that','these','those','my','yours','his','her','its','our','their','few','little','much','many','lot','lots','of','most','some','any','enough','all','both','half','either','neither','each','every','other','another','such','what','who','where','how','whom','which','will','rather','quite','over', 'do','did', 'does','you','we','it','like','want','they']


for item in exceptList:
    if item in reResult:
       del reResult[item]






