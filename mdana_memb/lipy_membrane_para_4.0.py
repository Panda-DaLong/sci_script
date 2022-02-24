import sys
import numpy as np
import MDAnalysis as mda
from lipyphilic.lib.assign_leaflets import AssignLeaflets
from lipyphilic.lib.memb_thickness import MembThickness
from lipyphilic.lib.area_per_lipid import AreaPerLipid
from lipyphilic.lib.order_parameter import SCC


#In_File:
#box_file is pbc_box file which is an out_file of OpenMM
box_file = sys.argv[1]
#tra_trans_file is trajectory file from mdana_membrane_center.py 
tra_trans_file = sys.argv[2]


#Part_1:
def grep_box_dim(str1):

    lst1 = str1.split()

    box_x_nm = lst1[2][8:-1]
    box_y_nm = lst1[6][2:-1]
    box_z_nm = lst1[10][2:-2]

    box_nm = []
    for i in [box_x_nm, box_y_nm, box_z_nm]:
        box_nm.append(float(i))
                                            
    box_nm = np.array(box_nm)

    box_angstrom = box_nm * 10

    box_direct = np.array((90, 90, 90))

    box_dim = np.concatenate((box_angstrom, box_direct))

    return box_dim

all_box_dim = []

with open(box_file) as f:
        
    #skip box_dim of step 0
    line = f.readline()

    for line in f:

        box_dim = grep_box_dim(line)

        all_box_dim.append(box_dim)

u = mda.Universe(tra_trans_file)

for ts in u.trajectory:
    ts.dimensions = all_box_dim[u.trajectory.frame]


#Part_2:
leaflets = AssignLeaflets(
    universe=u,
    lipid_sel="name P" 
    )

leaflets.run()


#Part_3:
memb_thickness = MembThickness(
    universe=u,
    leaflets=leaflets.leaflets,
    lipid_sel="name P"
    )

memb_thickness.run()

np.savetxt('memb_thickness.txt', memb_thickness.memb_thickness)


#Part_4:
areas = AreaPerLipid(
    universe=u,
    leaflets=leaflets.leaflets,
    lipid_sel="name P"
    )

areas.run()

np.savetxt('areas.txt', areas.areas)


#Part_5-1:
tail_sel_str_sn1 = "resname DOP and (name C21"
for i in range(2, 19):
    tail_sel_str_sn1 += " or name C2{}".format(str(i))
tail_sel_str_sn1 += ")"

print(tail_sel_str_sn1)

scc_sn1 = SCC(
    universe=u,
    tail_sel=tail_sel_str_sn1
    )

print(scc_sn1.tails)

scc_sn1.run()

np.savetxt('scc_sn1.txt', scc_sn1.SCC)

#Part_5-2:
tail_sel_str_sn2 = "resname DOP and (name C31"
for i in range(2, 19):
    tail_sel_str_sn2 += " or name C3{}".format(str(i))
tail_sel_str_sn2 += ")"

print(tail_sel_str_sn2)

scc_sn2 = SCC(
    universe=u,
    tail_sel=tail_sel_str_sn2
    )

print(scc_sn2.tails)

scc_sn2.run()

np.savetxt('scc_sn2.txt', scc_sn2.SCC)

#Part_5-3:
scc_sn_average = SCC.weighted_average(scc_sn1, scc_sn2)

np.savetxt('scc_sn_average.txt', scc_sn_average.SCC)

