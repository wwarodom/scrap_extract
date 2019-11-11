# -*- coding: utf-8 -*-
#from pythainlp.tokenize import sent_tokenize 
from pythainlp.tokenize import word_tokenize

engineOption = "newmm"
#engineOption = "longest-matching"

# text = "โอเคบ่พวกเรารักภาษาบ้านเกิด"
#ll = word_tokenize(text, engine="newmm")
#print(ll)

f = open("output.xls", "r")
text = f.read() 

l1 = word_tokenize(text.decode("utf-8"), engine=engineOption)

f = open("token.xls", "w")
for t in l1:
    #print('xx' , t)   
    #f.write(t.encode("utf-8"))
#    if t == " ":
#       print("wow")
    if  t != '\n' and t != ' ':
       print('xx' , t)
       f.write(t.encode("utf-8"))
       f.write('\n')
f.close() 