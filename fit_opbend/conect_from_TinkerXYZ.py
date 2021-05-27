import sys
import pandas as pd

conect_file = sys.argv[1]

df = pd.read_csv(conect_file, dtype=object, sep='\s+', header=None, skiprows=[0])

df = df.iloc[:, 5:]
df = df.fillna('')

df.to_csv(sys.stdout, sep=' ', index=False, header=False)
