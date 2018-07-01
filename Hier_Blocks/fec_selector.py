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
            name='My Packet Selector',
            in_sig=[np.uint8, np.uint8],
            out_sig=[np.uint8]
        )
        self.selected_port = selected_port
        self.data_length = data_length

    def forecast(self, noutput_items, ninput_items_required):
        if self.selected_port == 0:
            ninput_items_required[0] = self.data_length
            ninput_items_required[1] = 0
        else:
            ninput_items_required[0] = 0
            ninput_items_required[1] = self.data_length

    def general_work(self, input_items, output_items):
        L = min(len(input_items[self.selected_port]), len(output_items[0]))

        output_items[0][:L] = input_items[self.selected_port][:L]

        self.consume(self.selected_port,L)

        self.produce(0,L)
        return -2 #gr.WORK_CALLED_PRODUCE
