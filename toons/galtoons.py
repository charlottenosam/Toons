# ======================================================================
# Import useful packages

from blobs import *
import pylab as plt
import matplotlib.cm as cm

# ======================================================================

class Galtoons(object):
    """
    NAME
        Galtoons

    PURPOSE
        Represent galaxy data as a set of matplotlib patches. Superimposes
        3 "blobs" to represent halos, disks and bulges.

    COMMENTS

    INITIALISATION
        From scratch.
        
    METHODS AND VARIABLES
        Galtoons.datadict       Dictionary containing dictionaries of galaxy 
                                data (from input file)
        Galtoons.components     Dictionary containing "blobs" created from data
                                in Galtoons.datadict
        Galtoons.plot_toons()   Plots a superposition of up to 3 "blobs" which 
                                represent the galaxies' halos, disks and bulges 
                                if relevant data is supplied.           
    
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
# Initiate the Galtoons class - make bulge, disk and halo Blob objects

    def __init__(self, halos=None, disks=None, bulges=None):        
        
        self.hello = "galtoons says 'hello there'"
        
        # Create dictionary with halos, bulges and disks
        self.datadict = {'halos':halos, 'disks':disks, 'bulges':bulges}
        
        # Set colour bar properties
        self.cbar_properties()
                   
        # Create a 'sortable' dictionary containing the halo, disk and 
        # bulge Blob objects
        self.components = {'a_halos':Blobs(halos), 'b_disks':Blobs(disks), 
                           'c_bulges':Blobs(bulges)}

# -----------------------------------------------------------------------    
# Set properties for colour bar
        
    def cbar_properties(self):
        
        # Initiate values
        self.colour_pars = None
        self.colour_name = None
        
        # Assign values from one of the galaxy components
        for ofTypeX in self.datadict:
            if self.datadict[ofTypeX] is not None:
                if 'colour' in self.datadict[ofTypeX]:
                    self.colour_pars = self.datadict[ofTypeX]['colour']
                if 'colourname' in self.datadict[ofTypeX]:
                    self.colour_name = self.datadict[ofTypeX]['colourname']
                
# -----------------------------------------------------------------------  
# Create a colourbar for the coloured galtoons, with a label if specified
    
    def cbar_make(self):
        
        if self.colour_pars is not None:
            
            dummy_blobs = Blobs(None)
            mycmap, mycmap_r = dummy_blobs.define_cmap()
            mappable = plt.cm.ScalarMappable(cmap=mycmap_r) 
            mappable.set_array(self.colour_pars)
            cbar = plt.colorbar(mappable)
            
            print "Plotting colour bar representing "+self.colour_name+"..."
            
            if self.colour_name is not None:
                cbar.set_label(self.colour_name)

# -----------------------------------------------------------------------                
# Plot galtoons made up of up to 3 blobs:

    def plot_toons(self):

        # Loop over halos, disks and bulges in that order:
        for ofTypeX in sorted(self.components):
            if self.components[ofTypeX].exist:   
                self.components[ofTypeX].plot_blobs()
        
        # Add the colour bar
        self.cbar_make()
