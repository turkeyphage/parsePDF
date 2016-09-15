'''
--- english_Ngram.py ---

function:
1. n-gram the string
2. count occurrence
3. return a dictionary for counting result

'''

from nltk.util import ngrams
import operator
from collections import Counter

#txt = 'roger is the man and hello world roger is the first sentence'
#n = 3

def ngram_process(sentence, n):
    after_ngram = ngrams(sentence.split(), n)

    all_list = []
    for item in after_ngram:
      #print(len(item)
      s =''
      for index in range(len(item)):
        #print(item[index])
        if index == (len(item)-1):
           s += item[index] 
        else:
           s += item[index]+' '

      all_list.append(s)

    
    '''
    #remove the duplicated one
    seen = set()
    seen_add = seen.add
    filtered = [x for x in all_list if not (x in seen or seen_add(x))]

    #set a dictionary with keys from n-gram_noDuplicated result
    dic ={ el:0 for el in filtered}

    #count the occurance
    for s in all_list:
        if s in dic:
            dic[s] = dic[s]+1
    '''

    dic = Counter(all_list)
    return dic

#print(ngram_process(txt, n))

