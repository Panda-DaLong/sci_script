import sys
import numpy as np
import pandas as pd

dist_infile = sys.argv[1]
r6_infile = sys.argv[2]

dist = pd.read_table(dist_infile, sep='\s+', header=None, skiprows=[0])
r6 = pd.read_table(r6_infile, sep='\s+', header=None, skiprows=[0])

dist_3 = dist[3]
r6_3 = r6[3]

sin_3 = dist_3 / r6_3
arcsin_3 = np.arcsin(sin_3)
angle = 180 / np.pi * arcsin_3
angle = angle.round(4)

angle.to_csv(sys.stdout, index=False)
