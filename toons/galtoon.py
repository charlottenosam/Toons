# Header documentation goes here!

# Licence information goes here!

# ======================================================================

import toons

import numpy as np
import pylab as plt
from matplotlib.patches import Ellipse as disk
from matplotlib.patches import Circle as bulge
 
# ======================================================================

class Galtoon(object):
    """
    NAME
        Galtoon

    PURPOSE
        Creates representative galaxy patches.

    COMMENTS

    INITIALISATION
        From scratch?
    
    METHODS AND VARIABLES
        
    BUGS

    AUTHORS
        Charlotte A. Mason (UCSB)

    HISTORY
      2013-07-18  Started (C Mason)
    """
# ----------------------------------------------------------------------
# Normalise data columns to make toons easier to see - 
# 'area' will be the area of the toon
    def normarea(mydisk):
        
        unitarea = np.linalg.norm(mydisk)
        area = mydisk/unitarea()   
        return area
        
# ----------------------------------------------------------------------


