from readxyz import readxyz_function
from writexyz import writexyz_function
import math


def stretch_molecule(filename,atom1,atom2,delta):
    result = readxyz_function(filename)

    n_atoms = result[0]
    coordinates = result[3]

    # stretch coordinates

    coordinate_diff = []
    for i in range(3):
        coordinate_diff.append(coordinates[atom1][i]-coordinates[atom2][i])

    bond_length = math.sqrt(coordinate_diff[0]**2 + coordinate_diff[1]
                            **2 + coordinate_diff[2]**2)

    for i in range(3):
        coordinates[atom2][i] = coordinates[atom2][i] + (delta *
                                                         coordinate_diff[i])/bond_length

    stretched_result = n_atoms, result[1], result[2], coordinates

    writexyz_function(stretched_result, 'stretched_'+filename)
