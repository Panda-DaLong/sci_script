import sys
import pandas as pd

in_file = sys.argv[1]
residue_name = sys.argv[2]
atom_num = int(sys.argv[3])

names = pd.Series([residue_name] * atom_num)

df = pd.read_csv(in_file, sep='\s+', header=None, skiprows=[0,1], nrows=atom_num)

df.insert(3, 'residue', names)

print(df.to_string(header=False, index=False))
