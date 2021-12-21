from readxyz import readxyz_function
from writexyz import writexyz_function


def stretch_molecule(filename):
    atom1 = int(input('Enter first atom ? '))
    atom2 = int(input('Enter second atom ? '))
    delta = float(input('Enter the distance to be stretched ? '))

    result = readxyz_function(filename)

    n_atoms = result[0]
    coordinates = result[3]

    # stretch coordinates
    coordinate_diff = [(coordinates[atom1][i]-coordinates[atom2][i])
                       for i in range(3)]
    bond_length = (
        coordinate_diff[0]**2 + coordinate_diff[1]**2+coordinate_diff[2]**2)**1/2
    coordinates[atom2] = [coordinates[atom2][i] + delta *
                          (coordinate_diff[i])/bond_length for i in range(3)]
    streched_result = n_atoms, result[1], result[2], coordinates

    writexyz_function(streched_result, 'streched_'+filename)

