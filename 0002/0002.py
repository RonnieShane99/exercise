#coding=utf-8

import re
from collections import Counter
import codecs

def word_count(txt):
	wordpattern = r'[a-zA-Z-]+'
	words=re.findall(wordpattern,txt)
	l=Counter(words)
	return l

def writetofile(l):
	f=codecs.open("wordcount.txt","w","utf8")
	f.write("word and count\r\n")
	for word,freq in l.items():
		f.write(word+" "+str(freq)+'\r\n')
	f.close()


if __name__ == '__main__':
	txt = open('./test.txt', 'r').read().lower()
	l=word_count(txt)
	writetofile(l)
	