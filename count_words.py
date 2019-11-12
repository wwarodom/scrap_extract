# -*- coding: utf-8 -*-
# count-list-items-1.py
import obo

def main():
    f = open("output.xls", "r")
    fsort = open("output-sort.xls", "w")

    wordstring = f.read() 
    #print('wordstring: ', wordstring)
    wordlist = wordstring.split() 
    print('startlist 0: ', wordlist[0])
    print('startlist 1: ', wordlist[1])
    #fsort.write(wordlist[1])

    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))

        #print("String\n" + wordstring +"\n")
        #print("List\n" + str(wordlist) + "\n")
        #print("Frequencies\n" + str(wordfreq) + "\n")
        #print("Pairs\n" + str(list(zip(wordlist, wordfreq))))
        #fsort.write(str(list(zip(wordlist, wordfreq)))  )
        dictionary = obo.wordListToFreqDict(wordlist)
        sorteddict = obo.sortFreqDict(dictionary)

        #fsort.write('Word, Count\n')

        for s in sorteddict: 
        	fsort.write(s[1])
        	fsort.write(',')
        	fsort.write(str(s[0]))
        	fsort.write('\n')
        #for s in sorteddict: print(s[1])

#    for x in range(10):
#    	print(sorteddict[x][1])
#        fsort.write(sorteddict[x][1]) 
    f.close()
    fsort.close()
main()