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


for {set atom_index 0} {$atom_index < [$sel_all num]} {incr atom_index} {

set atom_sel [atomselect top "index $atom_index" frame last]

set atom_x [$atom_sel get x]
if {$atom_x > [expr $geo_center_x + $pbc_x_half]} {
$atom_sel set x [expr $atom_x - $pbc_x]
} elseif {$atom_x < [expr $geo_center_x - $pbc_x_half]} {
$atom_sel set x [expr $atom_x + $pbc_x]
}

set atom_y [$atom_sel get y]
if {$atom_y > [expr $geo_center_y + $pbc_y_half]} {
$atom_sel set y [expr $atom_y - $pbc_y]
} elseif {$atom_y < [expr $geo_center_y - $pbc_y_half]} {
$atom_sel set y [expr $atom_y + $pbc_y]
}

set atom_z [$atom_sel get z]
if {$atom_z > [expr $geo_center_z + $pbc_z_half]} {
$atom_sel set z [expr $atom_z - $pbc_z]
} elseif {$atom_z < [expr $geo_center_z - $pbc_z_half]} {
$atom_sel set z [expr $atom_z + $pbc_z]
}
}

