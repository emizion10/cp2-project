
# Read energy function
def readenergy_function(filename):
    energy = 0                      #testing intial values are zero
    not_converged = 0
    nearly_converged = 0
    with open(filename, "r") as file:
        for  line_number,line in enumerate(file):
            if line[0:25] == 'FINAL SINGLE POINT ENERGY':
               data=line.split()
               energy=data[4]
            elif line[30:61] == '****ORCA TERMINATED NORMALLY****':
               orca_terminated_normally = 1
            elif line[51:78] == '(SCF not fully converged!)':
               nearly_converged = 1
            elif line[32:56] == 'SERIOUS PROBLEM IN SOSCF':
               not_converged = 1 #orca not converged
            elif line[39:44] == 'ERROR':
               not_converged = 1 #orca not converged
            else:
                continue
        file.close()
    if energy == 0:
        not_converged = 1

    return energy, not_converged
