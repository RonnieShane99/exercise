#coding=utf-8

import os
from PIL import Image

iphone5_height=1136
iphone5_width=640

def resizepic(path,new_path,width=iphone5_width,height=iphone5_height):
	im=Image.open(path)
	w,h=im.size
	if w>width:
		h=width*h//w
		w=width
	if h>height:
		w=height*w//h
		h=height
	im_resized = im.resize((w,h), Image.ANTIALIAS)
	im_resized.save(new_path)

def walk_dir_and_resize(path):
	for root, dirs, files in os.walk(path):
		for f_name in files:
			if f_name.lower().endswith('jpg'):
				path_dst = os.path.join(root,f_name)
				f_new_name = 'iPhone5_' + f_name
				resizepic(path=path_dst, new_path=f_new_name)

if __name__ == '__main__':
	walk_dir_and_resize('./')