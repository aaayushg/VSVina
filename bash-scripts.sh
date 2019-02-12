# these scripts can be used individually for different purposes
for in in {0..11}; do mv lig$i.pdbqt ./lig$i; done
for i in {101..299}; do rm $i.pdbqt; done
for i in {0..100}; do sed '/ENDMDL/,$d' $i.pdbqt > new$i.pdbqt; done
for i in {0..100}; do sed '/MODEL 1/d' new$i.pdbqt > $i.pdbqt; done
for i in {0..100}; do rm new$i.pdbqt; done
