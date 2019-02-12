# This code can be used to split a library of millions of ligands into several disjoints
# This works with the sdf format (Downloaded from ZINC database)

f= "library-name-prefix"
split_number= 10000 #(number of molecules in each file--delete this line in bracket)
number_of_sdfs = split_number
i=0
j=0
f2=open(f+str(j)+'.sdf','w')
for line in open(f+'.sdf'):
	f2.write(line)
	if line[:4] == "$$$$":
		i+=1
	if i > number_of_sdfs:
		number_of_sdfs += split_number 
		f2.close()
		j+=1
		f2=open(f+str(j)+'.sdf','w')
print(i)
