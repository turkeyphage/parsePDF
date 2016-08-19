from nltk.util import ngrams

def ngram_String(sentence, n):
    return ngrams(sentence.split(), n)



txt = 'this is roger, I am going to tell you a story'
n = 3

after_ngram = ngram_String(txt, n)


print(type(after_ngram))


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
  #print(s)
  all_list.append(s)
print(all_list)
'''
for grams in after_ngram:
    #print(grams)
    #combine the words
    s = grams[0]+' '+grams[1]+' '+grams[2]
    print(s)
'''
