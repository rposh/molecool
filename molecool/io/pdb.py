# -*- coding: utf-8 -*-
"""
Functions for reading and writing pdb files

Created on Wed Dec 16 13:59:49 2020

@author: poshr
"""

import numpy as np

def open_pdb(f_loc):
    with open(f_loc) as f:
        data = f.readlines()
    c = []
    sym = []
    for l in data:
        if 'ATOM' in l[0:6] or 'HETATM' in l[0:6]:
            sym.append(l[76:79].strip())
            c2 = [float(x) for x in l[30:55].split()]
            c.append(c2)
    coords = np.array(c)
    return sym, coords
