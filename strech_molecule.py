from readxyz import readxyz_function
from writexyz import writexyz_function

def strech_molecule():
    filename = input('Enter the Filename(xyz) ?')
    axis = input('Along which axis ?')
    atom1 = input('At which atom ?')
    delta = 0.01

    result = readxyz_function(filename)

    n_atoms=result[0]
    coordinates=result[3]
    # change coordinates
    atom_count = 0
    while atom_count < n_atoms:
        if (coordinates[atom_count - 1])[int(axis) - 1] <= (coordinates[int(atom1) - 1])[int(axis) - 1]:
            (coordinates[atom_count - 1])[int(axis) - 1] += -delta
        else:
            (coordinates[atom_count - 1])[int(axis) - 1] += delta
        atom_count += 1

    streched_result=n_atoms,result[1],result[2],coordinates

    writexyz_function(streched_result, 'streched_'+filename)

strech_molecule()