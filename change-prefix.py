#!/usr/bin/env python3
from os import listdir
import os
path='./'
pbs='run.pbs'
new= [i for i in listdir(path) if i.startswith('1asinex')]
new=''.join(map(str,new))[0:8]
print new[0:8]
with open(pbs, 'r') as file:
        filedata=file.read()
filedata=filedata.replace('asinex0',new)
with open(pbs,'w') as file:
        file.write(filedata)

sh='vina.sh'
with open(sh, 'r') as file:
        filedata=file.read()
filedata=filedata.replace('div',new)
with open(sh,'w') as file:
        file.write(filedata)

