try:  
    from cStringIO import StringIO  
except ImportError:  
    from StringIO import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os, glob, re, sys

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

from collections import Counter

# change to assigned folder and list all PDF filenames
def get_All_PDF_Name(directoryPath):
    os.chdir(directoryPath)
    allPDF = []
    for filename in glob.glob("*.pdf"):
	allPDF.append(filename)
    return allPDF


#get PDF's metadata
def getPDF_Metadata(filename):
    print('filename = ' + filename)
    fp = open(filename, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    return(doc.info)


# get content of PDF and convert to txt string
# how to use it? ex. convert('myfile.pdf', pages=[5,7])

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


# modify string
'''
def removeEmptyLine(txt):
    return re.sub("\n\s*\n*", "\n", txt)

'''

def count_word_occurrences(list_of_words):
    return Counter(list_of_words)


def split_string_with_re(txt):
    #pattern1 is select all words except "\n" "\s" "\t" ","
    pattern1 = re.compile(r'[\w]+\.?[\w]+\.?')
    allresult = re.findall(pattern1, txt)
    return allresult

# main program 

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
    print('please assign some arguments and try again. ex: python parsePDF.py /working/path/filename.pdf')
    sys.exit()
elif len(sys.argv) > 2:
    print('too many argv, please try again')
    sys.exit()


head, tail = os.path.split(sys.argv[1])

print('folder: '+ head)
print('filename: '+ tail)
os.chdir(head)
fullText = convert(tail, 0)

reResult = count_word_occurrences(split_string_with_re(fullText))

for key in reResult.keys():
    exceptList = ['is','are','the','The','this','This','that','That','V','not','Not','yes','no','Yes','No','v','and','And','to','To','pages','of','before','over','in','In','on','On','then','between','after','pages','with','for','all','by','By','table','Table','Figure','figure','can','from','data','or','if','else','its','than','be','only','out','Out','datasheet']

    for item in exceptList:
        if key == item:
	   del reResult[key]

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



