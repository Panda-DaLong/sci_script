import sys
import MDAnalysis as mda
from lipyphilic.lib.assign_leaflets import AssignLeaflets
from lipyphilic.lib.memb_thickness import MembThickness


in_file = sys.argv[1]


u = mda.Universe(in_file)


leaflets = AssignLeaflets(
    universe=u,
    lipid_sel="name P" 
    )

leaflets.run()


memb_thickness = MembThickness(
    universe=u,
    leaflets=leaflets.leaflets,
    lipid_sel="name P"
    )

memb_thickness.run()

print(memb_thickness.memb_thickness)

