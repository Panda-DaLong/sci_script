set pbc_x_nm 5.727885925302992
set pbc_y_nm 5.734745668926102
set pbc_z_nm 9.293705284074134

set pbc_x [expr $pbc_x_nm * 10]
set pbc_y [expr $pbc_y_nm * 10]
set pbc_z [expr $pbc_z_nm * 10]

set sel_cha [atomselect top "resname cha and chain L" frame last] 

set sel_all [atomselect top "all" frame last]

pbc set [list $pbc_x $pbc_y $pbc_z]

pbc box -on

pbc wrap -centersel $sel_all -center com -compound residue
