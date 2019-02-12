#!/usr/bin/env python

# This python code is for ranking the ligands after virtual screening
# on the basis of their binding affinity to the protein. This produces
# an output consisting of ligand index and binding affinity in kcal/mol

#Importing Libraries
from os import listdir
from os.path import join
import os

# The output will be saved as rank.table
table="rank.table"
# Path should direct to the original location of all the output files from vina
path="./"

def get_score(file_name):
	with open(file_name) as handle:
		for line in handle:
			if line.startswith("REMARK VINA RESULT:"):
				score = float(line.split()[3])
				break
	return score

ligands=[i for i in listdir(path) if len(i)==15 and i.startswith("lib_ligand_")]

scores = []
for ligand in ligands:
	file_name = join(path, ligand, "out.pdbqt")
	score = get_score(file_name)
	scores.append((ligand, score))

scores.sort(key = lambda item : item[1])

with open(table, "w") as handle:
	for ligand, score in scores:
		handle.write("%20s %20.10f\n"%(ligand, score))
