import codecs
from pythainlp.tokenize import Tokenizer, dict_trie
from pythainlp.corpus.common import thai_words

# Given a list of words, return a dictionary of
# word-frequency pairs.
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

# Sort a dictionary of word-frequency pairs in
# order of descending frequency.
def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

def main():
    engineOption = ["newmm","longest-matching" ,"dict","ulmfit"]
    f = codecs.open('input.txt', encoding='utf-8')
    fsort = open("output-sort.csv", "w", encoding="utf-8")

    text = ""
    for line in f:
        # print (line)
        text = text + line


    custom_words_list = set(thai_words())
    custom_words_list.add('รีเทนเนอร์')
    custom_words_list.add('จัดฟัน')
    custom_words_list.add('ฟันชิด')
    trie = dict_trie(dict_source=custom_words_list)
    _tokenizer   = Tokenizer(custom_dict=trie, engine='newmm')

    print('------ Starting to tokenize words ------')
    # words = word_tokenize(text, engine=engineOption[0])
    words = _tokenizer.word_tokenize(text)
    i = 0
    wordsNew = ""
    for word in words:
        if word and (not word.isspace()) and word != '-' and word != '/' and not word.isnumeric():
            i=i+1
            # print(i , ': ' , word.strip() )
            wordsNew = wordsNew + word.strip() + " "
    f.close()

    print('------ Starting to count words: ------')
    wordlist = wordsNew.split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w.strip()))
        dictionary = wordListToFreqDict(wordlist)
        sorteddict = sortFreqDict(dictionary)
        i=i+1
        if ( i % 150 == 0 ) :
            print(".")
        else:
            print(".", end = '')

    print('------ Starting to sort words and write to file ------')
    for s in sorteddict:
        print(s[1],"|", s[0])
        fsort.write(s[1]+"|"+ str(s[0]))
       	fsort.write('\n')
    fsort.close()
main()


# Excel UTF-8 problem: Need to open blank excel and import external data from csv (select encoding)
# https://sysadmin.psu.ac.th/2018/09/17/open-thai-csv-excel-correctly/
