# -*- coding: utf-8 -*-
"""
Functions of analyzing/measuring molecules

Created on Wed Dec 16 13:51:03 2020

@author: poshr
"""

from .atom_data import atomic_weights

from .measure import calculate_distance

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    
    # Find the bonds in a molecule
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds

def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.
    
    Parameters
    ----------
    symbols : list
        A list of elements.
    
    Returns
    -------
    mass : float
        The mass of the molecule
    """
    
    mass = 0.0
    for atom in symbols:
        mass += atomic_weights[atom]
    
    return mass