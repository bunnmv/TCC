"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
from gnuradio import digital


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block

    def __init__(self):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='My Cummulative Phasor',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.last = 1.0

    def work(self, input_items, output_items):
        cum_product = np.cumprod(np.concatenate(([self.last], input_items[0])))
        cum_product /= np.abs(cum_product)
        output_items[0][:], self.last = cum_product[:-1], cum_product[-1]
        return len(input_items[0])
