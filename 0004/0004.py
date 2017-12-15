#coding=utf-8

import re
import os
from collections import Counter
import glob
from pprint import pprint

def list_txt():
	#use glob to find every notes with type txt
	return glob.glob("*.txt")

def wc(filename):
	datalist=[]
	with open(filename,'r')as f:
		for line in f:
			content=re.sub("\"|,|\.","",line)
			datalist.extend(content.strip().split(' '))
	return Counter(datalist).most_common(1)

def most_comm():
	all_txt=list_txt()
	for txt in all_txt:
		print wc(txt)

if __name__ == '__main__':
	filename=0004
	print map(wc,list_txt())