"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, select_port=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Modulation Selector',   # will show up in GRC
            in_sig=[np.int8],
            out_sig=[np.int8,np.int8,np.int8]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.select_port = select_port

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        if self.select_port == 0:
        	output_items[0][:] = input_items[0][:]
        	output_items[1][:] = None
        	output_items[2][:] = None
        elif self.select_port == 1:
        	output_items[0][:] = None
        	output_items[1][:] = input_items[0][:]
        	output_items[2][:] = None
        else:
        	output_items[0][:] = None
        	output_items[1][:] = None
        	output_items[2][:] = input_items[0][:]
        return len(output_items[self.select_port])
