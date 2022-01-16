set pbc_x_nm 5.727885925302992
set pbc_y_nm 5.734745668926102
set pbc_z_nm 9.293705284074134

set pbc_x [expr $pbc_x_nm * 10]
set pbc_y [expr $pbc_y_nm * 10]
set pbc_z [expr $pbc_z_nm * 10]

set pbc_x_half [expr $pbc_x / 2]
set pbc_y_half [expr $pbc_y / 2]
set pbc_z_half [expr $pbc_z / 2]

set sel_cha [atomselect top "resname cha and chain L" frame last] 
set geo_center [measure center $sel_cha weight mass]

set geo_center_x [lindex $geo_center 0]
set geo_center_y [lindex $geo_center 1]
set geo_center_z [lindex $geo_center 2]

set sel_all [atomselect top "all" frame last]

set move_x [expr $pbc_x_half - $geo_center_x]
set move_y [expr $pbc_y_half - $geo_center_y]
set move_z [expr $pbc_z_half - $geo_center_z]

$sel_all moveby [list $move_x $move_y $move_z]

pbc set [list $pbc_x $pbc_y $pbc_z]

pbc box -on

pbc wrap -compound residue
