#Part_1
set in_file "C:/Users/24113/Panda_Li/center_cha/center/mdana_test_center/vmd_npt_1.box"
set in_channel [open $in_file r]

set box_nm {}

while { [gets $in_channel line] >= 0 } {
scan $line "%f,%f,%f" pbc_x_nm pbc_y_nm pbc_z_nm
lappend box_nm [list $pbc_x_nm $pbc_y_nm $pbc_z_nm]
}

close $in_channel


#Part_2
set sel_cha [atomselect top "resname cha and chain L"] 
set sel_all [atomselect top "all"]

for { set i 0 } { $i < 100 } { incr i } {
$sel_cha frame $i
$sel_all frame $i

set pbc_box_nm [lindex $box_nm $i]
set pbc_box [vecscale $pbc_box_nm 10]
set pbc_box_half [vecscale $pbc_box 0.5]

set geo_center [measure center $sel_cha weight mass]
puts $geo_center
$sel_all moveby [vecsub $pbc_box_half $geo_center]

pbc set $pbc_box -first $i -last $i
pbc wrap -compound residue -first $i -last $i
}

pbc box -on

for { set i 0 } { $i < 100 } { incr i } {
$sel_cha frame $i
$sel_all frame $i

puts [pbc get -first $i -last $i]
}


