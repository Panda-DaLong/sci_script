import sys
import pandas as pd

in_file = sys.argv[1]

df = pd.read_table(in_file, dtype=object, sep='\s+', header=None, skiprows=list(range(4)))

energy = df[1]

energy.to_csv(sys.stdout, index=False)
