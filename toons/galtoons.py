# ======================================================================

import pylab as plt
import numpy as np
import math
from matplotlib.patches import Ellipse

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
    def normdata(self, vectordata):

        unitarea = np.sqrt(np.sum(vectordata*vectordata))
      #  area = vectordata/unitarea   
        return unitarea
        

           

# ----------------------------------------------------------------------
# CAM: I'm not sure how useful these dictionaries are...

# Plot ellipse toons
    def plot_toons(self, x, y, diskdata, bulgedata, colour):
        # define dictionaries for bulges and disks
        mybulge = {'area':bulgedata, 'colour':colour, 'eccentricity':0.3}
        mydisk = {'area':diskdata, 'colour':colour, 'eccentricity':0.8}
        
        # need to work out appropriate size for the toons
        normarea = self.normdata(mydisk['area'] + mybulge['area'])
        scale = 3 / normarea
              
        # define PI
        PI = 3.14159265359
        
        # plot on the current axes
        ax = plt.gca()
        
# CAM is there a better way to do the plotting so that I don't
# just repeat myself, some kind of loop?   
     
        # plot disks
        squashdisk = math.sqrt(1 - mydisk['eccentricity']*mydisk['eccentricity'])     
        for i in range(len(mydisk['area'])):
            b = squashdisk * math.sqrt(scale * mydisk['area'][i] / PI)
            a = squashdisk * b
            ax.add_patch(Ellipse((x[i], y[i]), a, b, 
                                facecolor=colour, edgecolor="black", 
                                alpha=0.5, angle=-70.0))


        # plot bulges
        squashbulge = math.sqrt(1 - mybulge['eccentricity']*mybulge['eccentricity'])     
        for i in range(len(mybulge['area'])):
            b = squashbulge * math.sqrt(scale * mybulge['area'][i] / PI)
            a = squashbulge * b
            ax.add_patch(Ellipse((x[i], y[i]), a, b, 
                                facecolor="blue", edgecolor="black", 
                                alpha=0.5, angle=-70.0))
    
