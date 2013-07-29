# ======================================================================

import numpy as np
import pylab as plt
from matplotlib.patches import Ellipse as disk
from matplotlib.patches import Circle as bulge 
 
# PJM: I think we will want to represent both bulges and disks as ellipses...

# ======================================================================

class Galtoons(object):
    """
    NAME
        Galtoons

    PURPOSE
        Represent galaxy data as a set of matplotlib patches. 

    COMMENTS

    INITIALISATION
    
    METHODS AND VARIABLES
        
    BUGS

    AUTHORS
        Charlotte A. Mason (UCSB)

    LICENSE
        GPLv2

    HISTORY
      2013-07-18  Started (C Mason)
    """
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

    def __init__(self):        
        self.hello = "hello there"

# -----------------------------------------------------------------------
    def pleasework(self):
        print "well something works"
        
# -----------------------------------------------------------------------

# Normalise data columns to make toons easier to see - 
# 'area' will be the area of the toon
    def normarea(self,mydisk):
        
        print mydisk
        # unitarea = np.linalg.norm(mydisk)
        # PJM: alternatively, you could do:
        unitarea = np.sqrt(np.sum(mydisk*mydisk))
        print unitarea      # 'numpy.float64' object is not callable
        area = mydisk/unitarea   
        return area
        
# ----------------------------------------------------------------------


