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

    def __init__(self, window_size=1, modulus=1,average_length=10):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='PER Calculator',   # will show up in GRC
            in_sig=[np.int8],
            out_sig=[np.float32,np.int8]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.window_size = window_size
        self.average_length = average_length
        self.modulus = modulus
        self.history = np.zeros(self.average_length)
        self.set_history(window_size)

    def calc_average_per(self,new_per):
        
        self.history = np.roll(self.history,1)
        
        self.history[0] = new_per

        average_per = np.mean(self.history)

    	if  0 <= average_per <= 0.35:

            selected_port = 2

        elif 0.35 < average_per <= 0.65:

            selected_port = 1

        else:

            selected_port = 0

        # print("History {} , Average {}".format(self.history,average_per))
        return average_per,selected_port


    def work(self, input_items, output_items):

        consumed = (len(input_items[0])-self.window_size+1)
        if  consumed < self.window_size:
            return 0    
        for i in range(0 , consumed):
            # if self.window_size+i < len(input_items[0]):
            observed = input_items[0][i:self.window_size+i] %256

            errors = sum((np.diff(observed) % self.modulus)-1)

            per = max((float(errors)/(self.window_size+errors)),0)
            print("Observed {}".format(observed))
            print("PER {}".format(per))
            output_items[0][i],output_items[1][i] = self.calc_average_per(per)

        return len(output_items[0])
