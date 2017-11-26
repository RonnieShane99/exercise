#coding=utf-8

import os
from PIL import Image


def resizepic(width,height):
	im=Image.open('./1.jpg')
	w,h=im.size
	#resize the pic with the certain retio
	if w>width:
		h=width*h//w
		w=width
	if h>height:
		w=height*w//h
		h=height
	im_resized = im.resize((w,h),Image.ANTIALIAS)#antialias----of the highest quality
	im_resized.save('./new.jpg')
pass

if __name__ == '__main__':
	iphone5_height=1136
	iphone5_width=640
	resizepic(width=iphone5_width,height=iphone5_height)
