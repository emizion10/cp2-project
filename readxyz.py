

#######read xyz file######

def readxyz_function(filename):
   symbols = []
   coordinates = [] 
         
   with open(filename,'r') as file:
        for line_number, line in enumerate(file):
            if line_number == 0:
                num_atoms = int(line)
            elif line_number == 1:
                comment = line
            else:
                atomic_symbol, x, y, z = line.split() 
                symbols.append(atomic_symbol)
                coordinates.append([float(x), float(y), float(z)])
        file.close()
   return num_atoms, comment, symbols, coordinates
    