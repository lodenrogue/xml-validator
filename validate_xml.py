#!/usr/bin/env python3

import sys
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ParseError


if len(sys.argv) == 1:
    print('Must include target file as parameter')
    exit(1)

target_file = sys.argv[1]
lines = ''

with open(target_file) as f:
    for line in f.readlines():
       lines += line

try:
    ET.fromstring(lines)
    print('Input is valid')

except ParseError as ex:
    print('Input is not valid. Cause: {}'.format(ex))
