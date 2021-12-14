def createxyz(array, filename):
    atoms = array[2]
    positions_float = array[3]

    # convert atom positions into strings in order to write
    positions_str = []
    for position in positions_float:
       position_str = [str(coordinate) + '\t'for coordinate in position]
       positions_str.append(position_str)
    print(positions_str)

    with open(filename, "w") as file:
        file.write(str(array[0]))
        file.write('\n')
        file.write(array[1])
        for atom_index in range(array[0]):
            file.write(atoms[atom_index])
            file.write('\t')
            file.writelines(positions_str[atom_index])
            file.write('\n')
    file.close()

createxyz('water.xyz')
