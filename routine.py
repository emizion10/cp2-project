import os
import argparse
import math

from xyz_to_orca import xyz_to_orca
from stretch_molecule import stretch_molecule
from energy import readenergy_function


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

energies = []
bond_lengths = []

def write_energy_bondlength(energy, coordinates):
    coordinate_diff = []
    for i in range(3):
        coordinate_diff.append(coordinates[atom1][i]-coordinates[atom2][i])

        bond_length = math.sqrt(coordinate_diff[0]**2 + coordinate_diff[1]
                            **2 + coordinate_diff[2]**2)
        energies.append(energy)
        bond_lengths.append(bond_length)


# Function to append coordinates to trajectory file
def write_trajectory_file(filename,energy):
    coordinates = []
    with open(filename,"r") as file:
        for  line_number,line in enumerate(file):
            if line_number == 0:
                continue
            if line_number == 1:
                tr_file.write('Energy is:'+str(energy))
            else:
                atomic_symbol, x, y, z = line.split() 
                coordinates.append([float(x), float(y), float(z)])

            tr_file.write(line)
    write_energy_bondlength(energy, coordinates)
    

for i in range(0,iteration):
    if(i==0):
        os.system('runorca_4_2 '+ molecule + '_orca.inp')
        energy = readenergy_function(molecule+'_orca.out')
        write_trajectory_file(molecule+'_orca.xyz',energy)
        # Renaming epoxy_orca.xyz to epoxy0.xyz
        os.rename(molecule+'_orca.xyz',molecule+str(i)+'.xyz')
        stretch_molecule(molecule+'0.xyz', atom1,atom2,delta)
        xyz_to_orca('stretched_'+molecule+'0.xyz')
        os.system('runorca_4_2 stretched_'+molecule+'0_orca.inp')
    else:
       energy = readenergy_function('stretched_'+molecule+str(i-1)+'_orca.out')
       write_trajectory_file('stretched_'+molecule+str(i-1)+'_orca.xyz',energy)
       # Eg:- Renaming stretched_epoxy0_orca.xyz to epoxy1.xyz
       os.rename('stretched_'+molecule+str(i-1)+'_orca.xyz',molecule+str(i)+'.xyz')
       stretch_molecule(molecule+str(i)+'.xyz',atom1,atom2,delta)
       xyz_to_orca('stretched_'+molecule+str(i)+'.xyz')
       os.system('runorca_4_2 stretched_'+molecule+str(i)+'_orca.inp')
       # Removing unwanted files
       os.system('rm stretched_'+molecule+str(i-1)+'.xyz')
       os.system('rm stretched_'+molecule+str(i-1)+'_orca.inp')
       os.system('rm stretched_'+molecule+str(i-1)+'_orca_trj.xyz')
       os.system('rm stretched_'+molecule+str(i-1)+'_orca.out')
       os.system('rm stretched_'+molecule+str(i-1)+'_orca.gbw')
       os.system('rm '+molecule+str(i)+'.xyz')


print(energies)
print(bond_lengths)