import sys
from xml.etree.ElementTree import parse


#xml_file is a forcefield file
xml_file = sys.argv[1]


#parse xml_file
xml = parse(xml_file)

root = xml.getroot()

params = ['c0', 'd1', 'd2', 'd3', 'q11', 'q21', 'q22', 'q31', 'q32', 'q33']


def reset_param(multipole):
    for param in params:
        multipole.set(param, "0")


for multipole in root.iterfind('AmoebaMultipoleForce/Multipole'):
    reset_param(multipole)


out_file = 'out-' + xml_file

xml.write(out_file, encoding='utf-8')

