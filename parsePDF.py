
#try:  
#    from cStringIO import StringIO  
#except ImportError:  
#    from StringIO import StringIO

#from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
#from pdfminer.converter import TextConverter
#from pdfminer.layout import LAParams
#from pdfminer.pdfpage import PDFPage
import os, glob, re, sys

#from pdfminer.pdfparser import PDFParser
#from pdfminer.pdfdocument import PDFDocument

from collections import Counter

from nltk.util import ngrams


# N-Gram the string
def ngram_String(sentence, n):
    #return object type is a generator, but each item of this return object is tuple.  
    return ngrams(sentence.split(), n)
	    


# change to assigned folder and list all PDF filenames
def get_All_TXT_Name(directoryPath):
    os.chdir(directoryPath)
    allTXT = []
    for filename in glob.glob("*.txt"):
        allTXT.append(filename)
    return allTXT

#get PDF's metadata
#def getPDF_Metadata(filename):
#    print('filename = ' + filename)
#    fp = open(filename, 'rb')
#    parser = PDFParser(fp)
#    doc = PDFDocument(parser)
#    return(doc.info)


# get content of PDF and convert to txt string
# how to use it? ex. convert('myfile.pdf', pages=[5,7])

#def convert(fname, pages=None):
#    if not pages:
#        pagenums = set()
#    else:
#        pagenums = set(pages)
#
#    output = StringIO()
#    manager = PDFResourceManager()
#    converter = TextConverter(manager, output, laparams=LAParams())
#    interpreter = PDFPageInterpreter(manager, converter)
#
#    infile = file(fname, 'rb')
#    for page in PDFPage.get_pages(infile, pagenums):
#        interpreter.process_page(page)
#    infile.close()
#    converter.close()
#    text = output.getvalue()
#    output.close
#    return text




def count_word_occurrences(list_of_words):
    return Counter(list_of_words)


def split_string_with_re(txt):
    #pattern1 is select all words except "\n" "\s" "\t" ","
    pattern1 = re.compile(r'[\w]+\.?[\w]+\.?')
    allresult = re.findall(pattern1, txt)
    return allresult

# main program 

##### 1. read file.txt to string variable
'''
if len(sys.argv) < 2:
    #no argument
    print('please assign the pdf_folder path and try again. ex: python parsePDF.py /pdf/path/')
    sys.exit()
elif len(sys.argv) > 2:
    print('too many argv, please try again')
    sys.exit()

#print(sys.argv[0])
#print(sys.argv[1])
#print(get_All_PDF_Name(sys.argv[1]))

filenameList = get_All_PDF_Name(sys.argv[1])

print(filenameList)
'''

if len(sys.argv) < 2:
    #no argument
    print('please assign some arguments and try again. ex: python3 parsePDF.py /working/path/filename.txt')
    sys.exit()
elif len(sys.argv) > 2:
    print('too many argv, please try again')
    sys.exit()


head, tail = os.path.split(sys.argv[1])

print('folder: '+ head)
print('filename: '+ tail)
os.chdir(head)
#fullText = convert(tail, 0)

#read file
f = open(tail, 'rt')
fullText = f.read()
f.close

#count word occurrences
reResult = count_word_occurrences(split_string_with_re(fullText))

exceptList = ['was','Was','Were','were','is','Is','Are','are','the','The','this','This','that','That','not','Not','yes','no','Yes','No','and','And','to','To','Page','page','pages','Pages','of','Of','Before','before','over','Over','in','In','on','On','then','Then','between','Between','after','After','with','With','for','For','all','All','by','By','table','Table','Figure','figure','can','Can','from','From','data','Data','Or','or','if','If','else','Else','its','Its','than','Than','be','Be','only','Only','out','Out','datasheet','Datasheet']


for item in exceptList:
    if item in reResult:
       del reResult[item]

print(reResult)

'''

for eachFile in filenameList:
    pdfMetadata = getPDF_Metadata(eachFile)
    print(pdfMetadata[0].items())
    print('===========================')

'''

#print(type(meta))
#print(len(meta))
#print(type(meta[0]))



