import os
import argparse

from xyz_to_orca import xyz_to_orca
from stretch_molecule import stretch_molecule
from readxyz import readxyz_function
from writexyz import writexyz_function


parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("atom1")
parser.add_argument("atom2")
parser.add_argument("delta")
parser.add_argument("iteration")
args = parser.parse_args()

# Sample command to run
# python3 epoxy.xyz 1 2 0.01 3


xyz_to_orca(args.filename)


def read_write_trj(filename,i):
    with open(filename,"r") as file:
        lines = file.readlines()
        fi = open("input_epoxy"+str(i)+".xyz","w")
        fi.writelines(lines[-5:])

for i in range(0,args.iteration):
    if(i==0):
        os.system('runorca_4_2 input_epoxy.inp')
        read_write_trj('input_epoxy_trj.xyz',i)
        stretch_molecule('input_epoxy0.xyz', args.atom1,args.atom2,args.delta)
        xyz_to_orca('stretched_input_epoxy0.xyz')
        os.system('runorca_4_2 stretched_input_epoxy0.inp')
    else:
       read_write_trj('stretched_input_epoxy'+str(i-1)+'_trj.xyz',i)
       stretch_molecule('input_epoxy'+str(i)+'.xyz',args.atom1,args.atom2,args.delta)
       xyz_to_orca('stretched_input_epoxy'+str(i)+'.xyz')
       os.system('runorca_4_2 stretched_input_epoxy'+str(i)+'.inp')
       if(i<args.iteration-1):
           os.system('rm stretched_input_epoxy'+str(i-1)+'.xyz')
           os.system('rm stretched_input_epoxy'+str(i-1)+'.inp')
           os.system('rm stretched_input_epoxy'+str(i-1)+'_trj.xyz')
           os.system('rm stretched_input_epoxy'+str(i-1)+'.out')
           os.system('rm stretched_input_epoxy'+str(i-1)+'.gbw')
           os.system('rm input_epoxy'+str(i)+'.xyz')