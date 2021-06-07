from rdkit import Chem
import numpy as np
import pandas as pd

data = pd.read_csv('original_data/train_labels.csv')
results = np.zeros((data.shape[0], 100,), dtype=np.int16) # 100 first elements in the Periodic table

for index, row in data.iterrows():
	if index % 100 == 0:
		print('index =', index)
	if row['image_id'][:3] == '000': # for now only train/0/0/0/*.png
		m = Chem.inchi.MolFromInchi(row['InChI'])
		for atom in m.GetAtoms():
			results[index, atom.GetAtomicNum()] += 1
	if index > 10000:
		break

np.save('atom_counts.npy', results)
