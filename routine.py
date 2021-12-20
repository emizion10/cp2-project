from xyz_to_orca import xyz_to_orca
from strech_molecule import strech_molecule


filename = input('Enter the Filename(xyz) ? ')
strech_molecule(filename)
xyz_to_orca('streched_'+filename)
