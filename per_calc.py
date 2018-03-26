"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block  - This block takes the packet numbers of the received window size packets and calculates the quantity of the lost packets
       As for today, it only works for window sizes multiples of the length of the data.
    """

    def __init__(self, window_size=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='PER Calculator',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.window_size = window_size
        self.controller = 0 # This is the index for the window size
        self.errors = 0 # the nunber of lost packets in the window size

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        for i in range(0 ,len(input_items[0])):
        	if self.controller < self.window_size:
        		#if input_items[0][aux] - input_items[0][i] > 1:
        		if i > 0: # First sample is lost
	        		if input_items[0][i] - input_items[0][i-1] > 1:
	        			self.errors +=1 # future packet number jumps one so it means one packet is lost.
        			self.controller += 1
        		output_items[0][i] = 0
        	else:
        		if self.errors > 0:
        			output_items[0][i] = float((self.errors)/(self.window_size)) #Relative error to the observed window
        		else:
        			output_items[0][i] = 0
        		self.controller = 0 #resets the control
        		self.errors = 0 #resets the errors
        return len(output_items[0])
