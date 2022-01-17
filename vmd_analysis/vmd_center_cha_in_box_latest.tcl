set in_file "G:/Temp_Files/temp_quadruple_cha/in_lipid/md_2/tcl_test_center/pbc_box_nm.txt"
set in_channel [open $in_file r]

while { [gets $in_channel line] >= 0 } {
scan $line "%f %f %f" pbc_x_nm pbc_y_nm pbc_z_nm
puts "$pbc_x_nm $pbc_y_nm $pbc_z_nm"
}

close $in_channel

set pbc_box_nm [list $pbc_x_nm $pbc_y_nm $pbc_z_nm]
set pbc_box [vecscale $pbc_box_nm 10]
set pbc_box_half [vecscale $pbc_box 0.5]


set sel_cha [atomselect top "resname cha and chain L" frame last] 
set geo_center [measure center $sel_cha weight mass]
set sel_all [atomselect top "all" frame last]

$sel_all moveby [vecsub $pbc_box_half $geo_center]

pbc set $pbc_box
pbc box -on
pbc wrap -compound residue
