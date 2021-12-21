from xyz_to_orca import xyz_to_orca
from stretch_molecule import stretch_molecule


filename = input('Enter the Filename(xyz) ? ')
stretch_molecule(filename)
xyz_to_orca('stretched_'+filename)
