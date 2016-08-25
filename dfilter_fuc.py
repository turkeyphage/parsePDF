'''
dfilter_fuc.py

This script do a quick scanning job on a string based on a json file 

how to call this function?
    
  dfilter_fuc(JSON_FileName, String_For_Scanning, Maximum_Words_in_a_set)
  eg.
     dfilter_fuc('dic.json', 'hello this is roger', 3)
'''

import json
import codecs

def dfilter_fuc(json_file, content_string, maximum_words_set):
    # Load the dic of Electrics
    with open(json_file, encoding='utf-8') as input_file:
        dic = json.loads(input_file.read())

    # Split words in content
    words = content_string.lower().split()
    n = len(words)

    # scan phrase in dic
    sig = []
    for m in range(maximum_words_set,0,-1):
        for i in range(0, n-m+1):
            phrase = ' '. join(words[i:i+m])
            print(phrase)
            if phrase in dic:
                if phrase in sig:
                    pass
                else:
                    sig.append(phrase)

    # variable "sig" will list out those significant phrases in this data sheet based on 
    return sig



