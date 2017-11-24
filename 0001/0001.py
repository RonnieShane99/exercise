#coding=utf-8

import random
import codecs

def gencode(length):
	s='abcdefghijklmnopqrstuvwxyz1234567890'
	l="".join(random.sample(s,length))
	return l

def write_list_to_file(code_list,code_output):
	f_code=codecs.open('codes.txt','w','utf8')
	f_code.write("invitation code here\r\n")
	for code in codes:
		f_code.write(code+"\r\n")
	f_code.close()



if __name__ == '__main__':
	length=10
	codes=[]
	for i in range(0,100):
		codes.append(gencode(length))
	code_output='./codes.txt'
	write_list_to_file(codes,code_output)



