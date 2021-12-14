#!/usr/bin/env python3

# read xyz file and create gaussian input file

def xyz_to_gauss(filename):

    # open xyz file and save data in array
    symbols = []
    coordinates = []
    with open(filename, "r") as file:
        for line_number, line in enumerate(file):
            if line_number == 0:
                n_atoms = int(line)
            elif line_number == 1:
                comment = line
            else:
                print(line,line.split())
                atomic_symbol, x, y, z = line.split()
                symbols.append(atomic_symbol)
                coordinates.append([float(x), float(y), float(z)])
        file.close()
    array = n_atoms, comment, symbols, coordinates
    atoms = array[2]
    positions_float = array[3]

    # convert atom positions into strings in order to write
    positions_str = []
    for position in positions_float:
        position_str = [str(coordinate) + '\t' for coordinate in position]
        positions_str.append(position_str)
    print(positions_str)

    # add additional info for gaussian input file
    filepath = '%chk=water.chk'
    cpu = '%nproc=4'
    mem = '%mem=4GB'
    calc_type = '#P OPT BP86/cc-pvdz'
    title = filename + ' ' + calc_type
    charge = '0'
    multiplicity = '1'

    # write data from array into a gaussian input file
    with open('input_' + filename[:-4] + '.com', "w") as file:
        # specifications
        file.write(filepath)
        file.write('\n')
        file.write(cpu)
        file.write('\n')
        file.write(mem)
        file.write('\n')
        file.write(calc_type)
        file.write('\n\n')
        file.write(title)
        file.write('\n\n')
        file.write(charge)
        file.write(' ')
        file.write(multiplicity)
        file.write('\n')
        # write xyz coordinates
        for atom_index in range(array[0]):
            file.write(atoms[atom_index])
            file.write('\t')
            file.writelines(positions_str[atom_index])
            file.write('\n')
        file.write('\n')
    file.close()

xyz_to_gauss('water.xyz')