"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class selector_3_1_bb(gr.basic_block):
    def __init__(self, selected=0):
        gr.basic_block.__init__(
            self,
            name='My Selector',
            in_sig=[np.float32, np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.selected = selected
        self.consume_nonselected = True

    def forecast(self, noutput_items, ninput_items_required):
        for i in range(len(ninput_items_required)):
            if i == self.selected:
                ninput_items_required[i] = noutput_items
            else:
                ninput_items_required[i] = 0

    def set_selected(self, selected):
        self.selected = selected

    def general_work(self, input_items, output_items):
        lengths = [len(lst) for lst in input_items + output_items]
        # ~print('My Selector 1-3 bb', lengths)
        L = min(len(input_items[self.selected]), len(output_items[0]))
        output_items[0][:L] = input_items[self.selected][:L]
        for i in range(3):
            if i == self.selected:
                self.consume(i, L)
            elif self.consume_nonselected:
                self.consume(i, len(input_items[i]))
        self.produce(0, L)
        return -2  #gr.WORK_CALLED_PRODUCE
