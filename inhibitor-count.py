from os import listdir
import shutil
from collections import Counter
from os import listdir
from os.path import join
import os
file='data2.txt'
outfile='out2.txt'
destination='./results/'
path="./"
prefixes=('model','out')

def get_id(file_name):
        with open(file_name) as handle:
                for line in handle:
                        if line.startswith("REMARK  Name"):
                                id = line.split()[3]
				break
        return id
def get_ene(file_name):
        with open(file_name) as handle:
                for line in handle:
			if line.startswith("REMARK VINA"):
                                ene = line.split()[3]
				break
	return ene
with open(file, 'r') as file:
	for location in file:	
		loc=location.split()
		location=location.replace("/"," ")
		location=location.split()
		for i in loc:
			energ=get_ene(i)
			print i,energ
		
for i in location[:]:
	if i.startswith(prefixes):
		location.remove(i)
c=Counter(location)
print c
counts=Counter(i for i in c.elements() if c[i] > 5)
count=sorted(counts.items())
print count
	
ids = []
ene = []

for lig in os.listdir(path): 
        if lig.endswith('pdbqt'):
                new=os.path.splitext(os.path.basename(lig))[0]
		ids = get_id(lig)
		ene = get_ene(lig)
                if new in counts:
			print new,ene,ids



