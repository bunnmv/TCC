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

    def __init__(self, window_size=1, modulus=1):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='PER Calculator',   # will show up in GRC
            in_sig=[np.int8],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.window_size = window_size
        self.modulus = modulus

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        # print("input size -> {}".format(len(input_items[0])))
        consumed = (len(input_items[0]-self.window_size+1))
        if len(input_items[0]) < self.window_size:
            return 0    
            # per = erros + window_size
        for i in range(0 ,consumed):
            observed = input_items[0][i:self.window_size+i]
            errors = sum((np.diff(observed) % self.modulus)-1)
            output_items[0][i]= float(errors)/(self.window_size+errors)
            # if output_items[0][i] <= 1 and output_items[0][i] >= 0:
            	# print("Erros ->{}" .format(output_items[0][i]))
        # self.consume(0,consumed)
        return len(output_items[0])
