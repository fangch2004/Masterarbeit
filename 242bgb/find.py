# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from tqdm import tqdm
from shutil import copy2
path= 'C:\\Users\Administrator\Desktop'


for filename in tqdm(os.listdir(os.getcwd())):
	with open (filename) as myfile:
		
		input=unicode(myfile.read(),'utf-8')
		#unicode function make string in method case sensitive
		
		
		if 'Tatbestand'   in  input and 'Gründe' in input:
		    if input.find('Tatbestand') < input.find('Gründe'):
				copy2(filename, path+'\\'+'tatbestand'+'\\')
			#print(str(filename))
			#print(myfile.read().find('Tatbestand'))
			#if myfile.read().find('Tatbestand') <= myfile.read().find('Gr쮤e'):
				#copy2(filename, path+'\\'+'tatbestand'+'\\')	
				

'''
for filename in tqdm(os.listdir(os.getcwd())):
	with open (filename) as myfile:
		if 'Tatbestand'   in myfile.read():
			if myfile.read().find('Tatbestand'[,0[,len(myfile.read())-1]]) >1:
				print('with tatbestand')
				
				
string='dalian no Gr쮤e school'
if 'Gr쮤e' in string:
	print('found it ')
'''				