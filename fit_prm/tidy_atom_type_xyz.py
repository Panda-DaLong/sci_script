import sys
import pandas as pd

in_file = sys.argv[1]
#in_file is a tinker_format_xyz file from poledit(choose 1)

with open(in_file) as f:
    line = f.readline()
    print(line, end='')

df = pd.read_csv(in_file, dtype=str, sep='\s+', header=None, skiprows=[0], names=list(range(10)))

df[5] = df[5].astype(int) + 500

df.to_string(sys.stdout, header=False, index=False, na_rep='')

