from rdkit import Chem
import numpy as np
import pandas as pd
import time

t = time.time()

LENGTH = 1000000  	# number of molecules to analyze in the train dataset
N_ATOMS = 11  		# number of considered atoms (only frequently found ones)

data = pd.read_csv('original_data/train_labels.csv')
if LENGTH > data.shape[0]:
    exit(1, 'LENGTH is bigger than the data size')

"""
result_index returns index in the result array if the given atomic number
	is present. Otherwise, returns N_ATOMS, which is the index of the last
	element in the results array. This is supposed to work fast. Before saving,
	the last column of results will be deleted since it may contain summed number
	of other atoms present in the molecule.
"""
result_index = N_ATOMS * np.ones(100, dtype=int)
for index, atomic_num in enumerate([5,  6,  7,  8,  9, 14, 15, 16, 17, 35, 53]):
	result_index[atomic_num] = index
#print(result_index)

results = np.zeros((LENGTH, N_ATOMS + 1), dtype=np.int16)

for index, row in data.iterrows():
	if index % 10000 == 0: # auxilary output to see the progress
		print('index =', index)
	if index >= LENGTH:
		break
	
	m = Chem.inchi.MolFromInchi(row['InChI'])
	for atom in m.GetAtoms():
		results[index, result_index[atom.GetAtomicNum()] ] += 1
	
np.save('data/pretrain2/atom_counts.npy', results[:,:-1])

print('Program took {:.2f} seconds.'.format(time.time() - t))