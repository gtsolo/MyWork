from pathlib import Path
import os
import re
import jieba

sen=" "
with open('./webshell/fcee6226d09d150bfa5f103bee61fbde.php','r',encoding = 'UTF-8') as f:
        # for line in f.readlines():
        #     print(line+'\n')
        #     word = jieba.cut(line)
        #     print(word)
           
                             
            for line in f:
               print(line)
               word = jieba.cut(line)
              
               print(word)