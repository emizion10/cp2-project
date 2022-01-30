import os
import argparse

from xyz_to_orca import xyz_to_orca
from stretch_molecule import stretch_molecule
from readxyz import readxyz_function
from writexyz import writexyz_function


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Filename of the molecule:")
parser.add_argument("atom1", help="Atom 1 to be stretched")
parser.add_argument("atom2",help="Atom 2 to be stretched")
parser.add_argument("delta", help="Distance to be stretched")
parser.add_argument("iteration", help="No of iterations needed")
args = parser.parse_args()

atom1 = int(args.atom1)
atom2 = int(args.atom2)
delta = float(args.delta)
iteration = int(args.iteration)

# Sample command to run
# python3 routine.py epoxy.xyz 1 2 0.01 3


xyz_to_orca(args.filename)

molecule = args.filename.split('.')[0]


tr_file = open('trajectory.xyz','a')


def read_write_trj(filename,i):
    with open(filename,"r") as file:
        lines = file.readlines()
        fi = open(molecule+str(i)+".xyz","w")
        for line in lines:
            fi.write(line)
            tr_file.write(line)

for i in range(0,iteration):
    if(i==0):
        os.system('runorca_4_2 '+ molecule + '_orca.inp')
        read_write_trj(molecule+'_orca.xyz',i)
        stretch_molecule(molecule+'0.xyz', atom1,atom2,delta)
        xyz_to_orca('stretched_'+molecule+'0.xyz')
        os.system('runorca_4_2 stretched_'+molecule+'0_orca.inp')
    else:
       read_write_trj('stretched_'+molecule+str(i-1)+'_orca.xyz',i)
       stretch_molecule(molecule+str(i)+'.xyz',atom1,atom2,delta)
       xyz_to_orca('stretched_'+molecule+str(i)+'.xyz')
       os.system('runorca_4_2 stretched_'+molecule+str(i)+'_orca.inp')

       os.system('rm stretched_'+molecule+str(i-1)+'.xyz')
       os.system('rm stretched_'+molecule+str(i-1)+'_orca.inp')
       os.system('rm stretched_'+molecule+str(i-1)+'_orca_trj.xyz')
       os.system('rm stretched_'+molecule+str(i-1)+'_orca.xyz')
       os.system('rm stretched_'+molecule+str(i-1)+'_orca.out')
       os.system('rm stretched_'+molecule+str(i-1)+'_orca.gbw')
       os.system('rm '+molecule+str(i)+'.xyz')