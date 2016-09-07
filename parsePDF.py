import os, glob, re, sys, operator

from english_Ngram import ngram_process
from collections import Counter
from dfilter_fuc import dfilter_fuc

ngram_number = 2

# change to assigned folder and list all PDF filenames
def get_All_TXT_Name(directoryPath):
    os.chdir(directoryPath)
    allTXT = []
    for filename in glob.glob("*.txt"):
        allTXT.append(filename)
    return allTXT



def count_word_occurrences(list_of_words):
    return Counter(list_of_words)


def split_string_with_re(txt):
    #pattern1 is select all words except "\n" "\s" "\t" ","
    pattern1 = re.compile(r'[\w]+\.?[\w]+\.?')
    allresult = re.findall(pattern1, txt)
    return allresult


####### main program ##########

##### 1. read file.txt to string variable

if len(sys.argv) < 2:
    #no argument
    print('please assign some arguments and try again. ex: python3 parsePDF.py filename.txt')
    exit(1)



print('filename: ' + sys.argv[1])

#read file

with open(sys.argv[1]) as f:
     original_texts = f.read()


fullText = re.sub("[(),=\"”“/]", "", original_texts)
fullText = re.sub("[-―･\n–&:]"," ", fullText)

#print(fullText)
    




#type(filted_words) = List
filtered_words = split_string_with_re(fullText.lower())

#type(filteredwords2String) = String
filteredwords2String = ' '.join(filtered_words)

print(filteredwords2String)
#process n-gram testing:

#print('n_gram = ', ngram_number)
#print('n_gram result:\n')

n_gram_result = ngram_process(filteredwords2String, ngram_number)
#type(n_gram_result) = Dictionary
#print(n_gram_result)

sorted_ngram = sorted(n_gram_result.items(), key=operator.itemgetter(1))
#print(sorted_ngram)

print('==================================================')


#print(type(filtered_words))
#print(filtered_words)

#count word occurrences
reResult = count_word_occurrences(filtered_words)

exceptList = ['was','were','is','are','not','yes','no','and','to','page','pages','before','over','in','on','then','between','after','with','for','by','table','figure','can','could','from','data','or','if','else','than','be','only','out','datasheet','the','a','an','this','that','these','those','my','yours','his','her','its','our','their','few','little','much','many','lot','lots','of','most','some','any','enough','all','both','half','either','neither','each','every','other','another','such','what','who','where','how','whom','which','will','rather','quite','over', 'do','did', 'does','you','we','it','like','want','they']


for item in exceptList:
    if item in reResult:
       del reResult[item]


#print('Parse result with regular expression:\n')

#print(reResult)

#print(reResult['High'])

'''
for eachFile in filenameList:
    pdfMetadata = getPDF_Metadata(eachFile)
    print(pdfMetadata[0].items())
    print('===========================')

'''




