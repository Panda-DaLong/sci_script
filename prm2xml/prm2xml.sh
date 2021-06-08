prm_file=${1:?'prm_file missing.'}
xyz_file=${2:?'xyz_file missing.'}
residue_name=${3:?'residue_name missing.'}

py_dir='./prm2xml/'
path='./'$prm_file'_split/'
xml_file=$residue_name'.xml'

alias py='python'

py $py_dir'prm_split.py' $prm_file

py $py_dir'atom_type_prm2xml.py' $path'atom.prm' > $xml_file 

py $py_dir'residue_prm2xml.py' $xyz_file $residue_name >> $xml_file 

py $py_dir'bond_prm2xml.py' $path'bond.prm' >> $xml_file

py $py_dir'angle_prm2xml.py' $path'angle.prm' >> $xml_file

py $py_dir'torsion_prm2xml.py' $path'torsion.prm' >> $xml_file

py $py_dir'stretchbend_prm2xml.py' $path'strbnd.prm' >> $xml_file

py $py_dir'vdw_prm2xml.py' $path'vdw.prm' >> $xml_file

py $py_dir'multipole_prm2xml.py' $path'multipole.prm' >> $xml_file

py $py_dir'polarize_prm2xml.py' $path'polarize.prm' >> $xml_file

