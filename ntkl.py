import nltk


f=open('./webshell/ffd7e5b969e56a23213d703d2f659841.php')
text=f.read()

print(text)
value = nltk.sent_tokenize(text)
print(value)
# word_tokenize 分词处理,分词不支持中文
for i in value:
    words = nltk.word_tokenize(text=i)
    print(words)

