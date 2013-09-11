# ======================================================================
# Import useful packages

from blobs import *
import pylab as plt, numpy as np
import matplotlib.cm as cm

# ======================================================================

class Galtoons(object):
    """
    NAME
        Galtoons

    PURPOSE
        Represent galaxy data as a set of matplotlib patches, with
        3 "blobs" to represent halos, disks and bulges superimposed on
        each other.

    COMMENTS

    INITIALISATION
        
        For example:
        
           mytoons = toons.Galtoons(bulges=mybulges,disks=mydisks,halos=None)
        
        where e.g. "mybulges" is a dictionary:
        
           mybulges = {'name':'bulge', 
                          'x':totalmass, 
                          'y':urcolour, 
                          'z':redshift, 
                       'size':bulgemass, 
                 'brightness':luminosity, 
                     'colour':urcolour, 
                 'colourname':'u-r magnitude'}
        
    METHODS AND VARIABLES
        Galtoons.data           Dictionary containing dictionaries of 
                                galaxy data (from input args)
        Galtoons.components     Dictionary containing "blobs" created 
                                from Galtoons.data
        Galtoons.plot()         Plots a superposition of up to 3 "blobs" which 
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
# Initiate the Galtoons class - make bulge, disk and halo Blob objects

    def __init__(self, halos=None, disks=None, bulges=None):        
        
        self.hello = "galtoons says 'hello there'"
        
        # Create dictionary with the input halo, bulge and disk data:
        self.data = {}
        if halos != None: self.data['halos'] = halos
        if disks != None: self.data['disks'] = disks
        if bulges != None: self.data['bulges'] = bulges
        # NB. The data directory only has non-trivial entries, so it 
        # can be used to loop over components efficiently.
        
        # Set colour bar properties
        self.cbar_properties()
                   
        # Create a 'sortable' dictionary containing the halo, disk and 
        # bulge Blob objects
        self.components = {'halos':Blobs(halos), 
                           'disks':Blobs(disks), 
                          'bulges':Blobs(bulges)}
                           
        return

# -----------------------------------------------------------------------    
# Set properties for colour bar
        
    def cbar_properties(self):
        
        # Initiate values
        self.colour_pars = None
        self.colour_name = None
        
        # Assign values from one of the galaxy components
        for ofTypeX in self.data:
            if self.data[ofTypeX] is not None:
                if 'colour' in self.data[ofTypeX]:
                    self.colour_pars = self.data[ofTypeX]['colour']
                if 'colourname' in self.data[ofTypeX]:
                    self.colour_name = self.data[ofTypeX]['colourname']
                
# -----------------------------------------------------------------------  
# Create a colourbar for the coloured galtoons, with a label if specified
    
    def cbar_make(self):
        
        if self.colour_pars is not None:
            
            dummy_blobs = Blobs(None)
            mycmap, mycmap_r = dummy_blobs.define_cmap()
            mappable = plt.cm.ScalarMappable(cmap=mycmap_r) 
            mappable.set_array(self.colour_pars)
            cbar = plt.colorbar(mappable)
                        
            if self.colour_name is not None:
                cbar.set_label(self.colour_name)

# -----------------------------------------------------------------------                
# Plot galtoons made up of up to 3 blobs. Plot them one by one, so that 
# the components overlap properly - and always plot the components in
# halo, disk, bulge order. If redshift (or some other z coordinate) is 
# present, plot in descending order of z.

    def plot(self):

        
        # First sort by z, if it's present:
        index = None
        for ofTypeX in self.data:
            if 'z' in self.data[ofTypeX]:
                 index = np.argsort(self.data[ofTypeX]['z'])
                 index = index[::-1]
                 break
        if index == None:
            index = np.array(range(len(self.data[ofTypeX]['x'])))
        
        # Now loop over galtoons, plotting them one by one:
        for k in index:
             for ofTypeX in ['halos','disks','bulges']:
                  if self.components[ofTypeX].exist:   
                       # print "Plotting the ",ofTypeX," of galtoon number ",k
                       self.components[ofTypeX].plot(member=k)
        
        # Add the colour bar:
        self.cbar_make()
