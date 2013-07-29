# Header documentation goes here!

# Licence information goes here!

# ======================================================================

import pylab as plt
import numpy as np
import math
from matplotlib.patches import Ellipse
 
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
            a = 0.8 * 0.5 * math.sqrt(vectordata[i] / PI)
            b = 0.8 * 4 * a
            ax.add_patch(Ellipse((x[i], y[i]), a, b, 
                                facecolor=colour, edgecolor="black", 
                                alpha=0.5, angle=-45.0))

    
