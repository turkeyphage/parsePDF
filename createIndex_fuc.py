'''
createIndex_fuc.py
 
Load a txt file, it will ignore "Numbers 0-9", "space" and "," automatically, and also create a reference json file

How to use it?

   createIndex_fuc('reference.txt')

It will create a same-name json file in the same folder(reference.json)

'''

# regulate index file of EE

import json
import codecs

def createIndex_fuc(source_file_name):


    max_len=0

    # output json filname   'sourceTxtName.json'
    sourceName = source_file_name.split('.')[0]
    jsonfile_fullname = sourceName + '.json' 
   

    with open(source_file_name, 'r', encoding='utf-8', buffering=1000000) as f:
        lines = f.readlines()
    f.close()

    #print(lines)

    dic = {}

    wholeList = []

    for line in lines:
        s = line.strip() #delete \n
        #print(s)
        n = len(s)
        t = ''
        for i in range(0, n):
            ca = ord(s[i])
            if (ca >= ord('0') and ca <= ord('9')) or (ca == ord(',')):
                pass
            else:
                t = t + str(s[i])
        t = t.strip()
        #t = t.rstrip()
        #t = t.lower()

        if t != '':
          t_in_list = t.split()

          if len(t_in_list) > max_len:
             max_len = len(t_in_list)

          wholeList.append(t)

        dic[t] = 0

    #for item in wholeList:
    #    print(item)


    #print(wholeList)

    #print('max_len = ', max_len)


    print('====================================================================')
    
    #print(dic)


    
    # write into output JSON file
    jsonData = json.dumps(dic, ensure_ascii=False)

    with codecs.open(jsonfile_fullname, 'w', 'utf8') as outfile:
        # json.dump(jsonData, outfile, sort_keys=True, ensure_ascii=False)
        json.dump(dic, outfile, sort_keys=True, ensure_ascii=False)


    print('JSON file created. Filename: ', jsonfile_fullname)
    

    # test: read output json 
    json_file = open(jsonfile_fullname, 'r')
    index_content = json.load(json_file)
    #print(index_content)
    #for item in index_content.keys():
    #    print(item)

    

#test
createIndex_fuc('index.txt')

