# -*- coding: utf-8 -*-
#from pythainlp.tokenize import sent_tokenize 
from pythainlp.tokenize import word_tokenize

engineOption = ["newmm","longest-matching" ,"dict","deepcut","ulmfit"]
#engineOption = "longest-matching"

# text = "โอเคบ่พวกเรารักภาษาบ้านเกิด"
#ll = word_tokenize(text, engine="newmm")
#print(ll)

f = open("output.xls", "r")
text = f.read() 
 
words = word_tokenize(text.decode("utf-8"), engine=engineOption[0])
f = open("token.xls", "w")
for word in words:
    #print('xx' , t)   
    #f.write(t.encode("utf-8"))
#    if t == " ":
#       print("wow")
    #if  word != '\n' and word != ' ':
    if  word != '\n':
       #print('xx' , word)
       f.write(word.encode("utf-8"))
       f.write('\n')
f.close() 

#Ref: https://www.thainlp.org/pythainlp/tutorials/notebooks/pythainlp-get-started.html