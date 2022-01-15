import os
from xyz_to_orca import xyz_to_orca
from stretch_molecule import stretch_molecule
from readxyz import readxyz_function
from writexyz import writexyz_function

filename = input('Enter the Filename(xyz) ? ')
xyz_to_orca(filename)


def read_write_trj(filename,i):
    with open(filename,"r") as file:
        lines = file.readlines()
        fi = open("water"+str(i)+".xyz","w")
        fi.writelines(lines[-5:])

for i in range(0,100):
    if(i==0):
        os.system('runorca_4_2 water.inp')
        read_write_trj('water_trj.xyz',i)
        stretch_molecule('water0.xyz')
        xyz_to_orca('stretched_water0.xyz')
    else:
        os.system('runorca_4_2 stretched_water'+str(i-1)+'.inp')
        os.system('rm stretched_water'+str(i-1)+'.inp')
        read_write_trj('stretched_water'+str(i-1)+'_trj.xyz',i)
        if(i<99):
            os.system('rm stretched_water'+str(i-1)+'_trj.xyz')
            os.system('rm stretched_water'+str(i-1)+'.out')
            os.system('rm stretched_water'+str(i-1)+'.gbw')
        stretch_molecule('water'+str(i)+'.xyz')
        os.system('rm water'+str(i)+'.xyz')
        xyz_to_orca('stretched_water'+str(i)+'.xyz')
        # os.system('rm stretched_water'+str(i)+'.xyz')
