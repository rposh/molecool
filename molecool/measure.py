"""
This module is for functions which perform measurements.
"""

import numpy as np


def calculate_angle(rA, rB, rC, degrees=False):
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta


def calculate_distance(rA, rB):
    """
    Calculates the distance between two points.

    Parameters
    ----------
    rA : np.array
        The coordinates of point A.
    rB : np.array
        The coordinates of point B.

    Returns
    -------
    dist : float
        The distance between rA and rB.

    Examples
    --------
    >>> r1 = np.array([0,0,0])
    >>> r2 = np.array([0,1,0])
    >>> calculate_distance(r1,r2)
    1.0
    """

    d = rA - rB
    dist = np.linalg.norm(d)
    return dist
