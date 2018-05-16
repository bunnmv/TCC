"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt


class blk(gr.basic_block):  # other base classes are basic_block, decim_block, interp_block
    def __init__(self, access_code=None, payload_length=100, threshold=0,tag_name="len_key2"):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.basic_block.__init__(
            self,
            name='My Correlator Block',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.access_code = access_code
        self.payload_length = payload_length
        self.threshold = threshold
        self.tag_name = tag_name

        self.mode = 'find'

        self.set_min_output_buffer(2**16)

        self.set_tag_propagation_policy(0)


    def general_work(self, input_items, output_items):
        if self.mode == 'output':
            return self.general_work_output(input_items, output_items)
        elif self.mode == 'find':
            return self.general_work_find(input_items, output_items)

    def general_work_output(self, input_items, output_items):
        L_in = len(input_items[0])
        L_out = len(output_items[0])
        L_payload = self.payload_length # in bits

        if L_in < L_payload or L_out < L_payload:
            return 0


        self.add_item_tag(0, # Port number
            self.nitems_written(0), # Offset
            pmt.intern(self.tag_name), # Key
            pmt.to_pmt(L_payload) # Value
        )
        output_items[0][:L_payload] = input_items[0][:L_payload]
        self.consume(0, L_payload)

        # ~print('Outputted {} items.'.format(L_payload))

        self.mode = 'find'

        return L_payload

    def general_work_find(self, input_items, output_items):
        L_in = len(input_items[0])

        if L_in < len(self.access_code) :
            return 0

        access_code_binary = np.array([int(b) for b in self.access_code], dtype=np.int)
        input_decoded = np.array(input_items[0] > 0, dtype=np.int)

        corr = np.correlate(2*input_decoded-1, 2*access_code_binary-1)
        matches = np.flatnonzero(corr >= len(self.access_code) - self.threshold)
        if len(matches) == 0:
            self.consume(0, L_in - len(self.access_code))
        else:
            self.consume(0, matches[0] + len(self.access_code))
            self.mode = 'output'

        return 0
