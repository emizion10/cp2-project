from readxyz import readxyz_function
from writexyz import writexyz_function


def stretch(filename, atom1, atom2, delta):

    
    result = readxyz_function(filename)
    coordinates = result[3]
    comments = result[1]
    symbols = result[2]
    # calculate bond vector and make it longer by 'delta' Angstrom ('coordinates' is a list of 3-vectors!)
    e_bond = [(coordinates[int(atom2)])[i]                                      # calculate bond vector
              - (coordinates[int(atom1)])[i] for i in range(3)]
    len_bond = (e_bond[0]**2 + e_bond[1]**2 + e_bond[2]**2)**(1/2)              # abs value of bond vector
    coordinates[int(atom2)] = [(coordinates[int(atom2)])[i] + float(delta) *    # new coordinates, stretched by delta
                               e_bond[i] / len_bond for i in range(3)]          # e_bond/len_bond is bond unit vector

    # convert atom positions into strings in order to write (saved them as float for math operations)
    positions_str = []                                                          # list for atom positions
    for position in coordinates:                                                # convert float in str for all atoms
        position_str = [str(coordinate) + ' ' for coordinate in position]
        positions_str.append(position_str)

    stretched_result = result[0], comments, symbols, positions_str

    writexyz_function(stretched_result, 'stretched_'+filename)

    


