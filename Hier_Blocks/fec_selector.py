"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""
import numpy as np
from gnuradio import gr

class selector_3_1_bb(gr.basic_block):
    def __init__(self, selected_port=0, data_length = 501):
        gr.basic_block.__init__(
            self,
            name='Simple Selector',
            in_sig=[np.uint8, np.uint8],
            out_sig=[np.uint8]
        )
        self.selected_port = selected_port
        self.data_length = data_length

    def forecast(self, noutput_items, ninput_items_required):
        for i in range(len(ninput_items_required)):
            if i == self.selected_port:
                ninput_items_required[i] = self.data_length
            else:
                ninput_items_required[i] = 0

    def general_work(self, input_items, output_items):
        L = min(len(input_items[self.selected_port]), len(output_items[0]))

        output_items[0][:L] = input_items[self.selected_port][:L]

        self.consume(self.selected_port,L)

        self.produce(0,L)
        return -2 #gr.WORK_CALLED_PRODUCE
