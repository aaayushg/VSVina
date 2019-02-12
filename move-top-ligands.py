#!/usr/bin/python
import os
import shutil

#data.txt is the file which contains all the top scored ligands path 
#(output of top-score-ligands.py)

file='data.txt'
destination='./results/'
with open(file, 'r') as file:
	for path in file:
		path=path.split()

#Copying all top scored ligands to new directory for further analysis
j=0
for i in path:
	print i
	shutil.copy(i,destination+str(j)+".pdbqt")
	j+=1
