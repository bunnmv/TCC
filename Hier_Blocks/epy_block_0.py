"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.basic_block):  # other base classes are basic_block, decim_block, interp_block
    """
    ATTENTION!

    This blocks works with unpacked bits in the input and in the output.
    """
    def __init__(self, access_code=None, payload_length=100):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.basic_block.__init__(
            self,
            name='My Frammer',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=[np.uint8]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.access_code = access_code
        self.payload_length = payload_length

    def general_work(self, input_items, output_items):
        if len(input_items[0]) < 8*self.payload_length:
            return 0

        access_code_binary = np.array([int(b) for b in self.access_code], dtype=np.uint8)

        payload = input_items[0][: 8*self.payload_length]
        packet = np.concatenate([access_code_binary, payload])

        if len(output_items[0]) < len(packet):
            return 0

        output_items[0][: len(packet)] = packet

        self.consume(0, 8*self.payload_length)

        return len(packet)
