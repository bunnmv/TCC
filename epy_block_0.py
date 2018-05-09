"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.basic_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, select_port=0.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.basic_block.__init__(
            self,
            name='Modulation Selector',   # will show up in GRC
            in_sig=[np.complex64,np.complex64,np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.select_port = select_port

    def general_work(self, input_items, output_items):
        """example: multiply with constant"""
        arrived_items = len(input_items[self.select_port])
        # print(arrived_items)
        # print(len(output_items[0]))
        # if len(output_items[0]) < arrived_items:
        #     return 0

        if self.select_port == 0:
        	output_items[0][:]= input_items[0][:len(output_items[0])]
        elif self.select_port == 1:
        	output_items[0][:] = input_items[1][:len(output_items[0])]
        else:
        	output_items[0][:] = input_items[2][:len(output_items[0])]
        	
        self.consume(0,len(input_items[0]))
        self.consume(1,len(input_items[1]))
        self.consume(2,len(input_items[2]))

        return len(output_items[0])
