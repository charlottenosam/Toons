# ======================================================================

import pylab as plt
import numpy as np
import math
from matplotlib.patches import Ellipse
 
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

# Normalise data columns to make toons easier to see - 
# 'area' will be the area of the toon
    def normarea(self, vectordata):

        unitarea = np.sqrt(np.sum(vectordata*vectordata))
        area = vectordata/unitarea   
        return area
        
# ----------------------------------------------------------------------

# Plot ellipse toons
    def plot_toons(self, x, y, vectordata, colour):
        PI = 3.14162
        ax = plt.gca()
        for i in range(len(vectordata)):
            a = 0.5 * math.sqrt(vectordata[i] / PI)
            b = 4 * a
            ax.add_patch(Ellipse((x[i], y[i]), a, b, 
                                facecolor=colour, edgecolor="black", 
                                alpha=0.5, angle=-30.0))

    
