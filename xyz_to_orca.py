def xyz_to_orca(filename):
    command1 = '! OPT BP86 cc-pvdz'
    command2 = '* xyzfile'
    command3 = '%pal'
    command4 = 'nproc = 4'
    command5 = 'end'
    command6 = '%maxcore  1024'
    charge = '0'
    command11 = 'end'
    multiplicity = '1'
    # write data from array into a orca input file
    with open(filename.split('.')[0] +'_orca.inp', "w") as file:
        # specifications
        file.write(command1)
        file.write('\n')
        file.write('\n')
        file.write(command3)
        file.write('\n')
        file.write(command4)
        file.write('\n')
        file.write(command5)
        file.write('\n')
        file.write('\n')
        file.write(command6)
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
