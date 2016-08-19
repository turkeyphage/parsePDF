from nltk.util import ngrams

def ngram_String(sentence, n):
    return ngrams(sentence.split(), n)



txt = 'this is roger, I am going to tell you a story'
n = 3

after_ngram = ngram_String(txt, n)


print(type(after_ngram))

for grams in after_ngram:
    #print(grams)
    #combine the words
    s = grams[0]+' '+grams[1]+' '+grams[2]
    print(s)
