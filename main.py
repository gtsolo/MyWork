from pathlib import Path
import os
import re
import jieba
pathName='./webshell'
fnLst=list(filter(lambda x:not x.is_dir(),Path(pathName).glob('**/*.php')))
#print(fnLst)

a=open('file.txt','w')
for fn in fnLst:
    with open(fn,'r',encoding="utf-8") as f:
            #print(f)                        
            for eachline in f:
                #line = eachline.strip().decode('utf-8','ignore')  
                wordList = list(jieba.cut(eachline))
                outStr = ''
                for word in wordList:
                 outStr += word
                 print(word)
              #for word in re.findall(r'\w+', line):
                 
                  #print(word,end="|")
                #dicw=word
#print(dicw)