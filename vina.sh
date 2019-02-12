#! /bin/bash

for f in div*.pdbqt; do
    b=`basename $f .pdbqt`
    echo Processing ligand $b
    mkdir -p $b
    vina --config pdz.conf --ligand $f --out ${b}/out.pdbqt --log ${b}/log.txt
done
~        
