def xyz_to_orca(filename, atom1, atom2):
    command1 = '! OPT BP86 cc-pvdz'
    command2 = '* xyzfile'
    command3 = '%pal'
    command4 = 'nproc = 4'
    command5 = '%maxcore  1024'
    charge = '0'
    command6 = '%geom'
    command7 = 'Constraints'
    command8 = '{B' 
    command9 = 'C}'#constraints
    command10 = 'end'
    multiplicity = '1'
    # write data from array into a orca input file
    with open(filename.split('.')[0] +'_orca.inp', "w") as file:
        # specifications
        file.write(command1)
        file.write('\n')
        file.write('\n')
        file.write(command6)
        file.write('\n')
        file.write(command7)
        file.write('\n')
        file.write(command8)
        file.write(' ')
        file.write(str(atom1))
        file.write(' ')
        file.write(str(atom2))
        file.write(' ')
        file.write(command9)
        file.write('\n')
        file.write(command10)
        file.write('\n')
        file.write(command10)
        file.write('\n')
        file.write(command3)
        file.write('\n')
        file.write(command4)
        file.write('\n')
        file.write(command10)
        file.write('\n')
        file.write(command5)
        file.write('\n')
        file.write('\n')
        file.write(command2)
        file.write(' ')
        file.write(charge)
        file.write(' ')
        file.write(multiplicity)
        file.write(' ')
        file.write(filename)
        file.write('\n')
    file.close()
