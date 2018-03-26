"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block Remover - separetes the data by only passing the counter length samples to output 1, otherwise pass zeros. 
    	Output 1 - Packet Counter
    	Output 2 - Data """

    def __init__(self, counter_length=1.0, payload_length=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Split Packet Counter',   # will show up in GRC
            in_sig=[np.int8],
            out_sig=[np.int8,np.int8]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.counter_length = counter_length
        self.payload_length = payload_length

    def work(self, input_items, output_items): 
    	"""example: multiply with constant"""       
    	if self.counter_length > 0: # packet counter has to be greater then one
        	output_items[0][0:self.counter_length+1] = input_items[0][0:self.counter_length+1]
        	output_items[0][self.counter_length:self.payload_length+1] = 0

        	output_items[1][0:self.counter_length] = 88 # sync blocks needs same quantity of itens on the output. Prints 'X'
        	output_items[1][self.counter_length:self.payload_length+1] = input_items[0][self.counter_length:self.payload_length+1]
        else:
        	output_items[0][:] = 0
        	output_items[1][:] = 0
        return len(output_items[0])
