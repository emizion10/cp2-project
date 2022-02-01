
# Read energy function
def readenergy_function(filename):
    energy = 0 
    with open(filename, "r") as file:
        for  line in enumerate(file):
            if line[0:25] == 'FINAL SINGLE POINT ENERGY':
                energy = line[32:]
            else:
                continue
        file.close()
    return energy