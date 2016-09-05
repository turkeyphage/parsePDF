# -*- coding: UTF-8 -*-
import re

with open('2099.txt', 'r') as fp:
    content = fp.readlines()



#print(content)

#content.replace('\s', '')
#content.replace('\n', ' ').replace('\r', '')
#print(content)

contentList=[]


for item in content:
    clearItem = item.rstrip('\n').rstrip(' ')
    if clearItem != '':
        contentList.append(clearItem)

print(contentList)
#print(contentList)
#print('')
