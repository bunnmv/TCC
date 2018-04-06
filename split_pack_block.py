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
        self.last_run_position = 0
        self.offset_position = 0
        self.data_period = (self.payload_length+self.counter_length)
        self.runs = 0 #flag that controls how many times the work function has been called

    def work(self, input_items, output_items): 
    	# """example: multiply with constant"""  
    
		#when loop counter resets work funtion is called again
    	input_len = len(input_items[0]);
    	self.offset_position = self.last_run_position # offset of the samples from last run

    	
    	# print('offset run ->{}' .format(self.offset_position))
    	# print('Input -> {}' .format(input_len))
    	# print('Work function calls -> {}' .format(self.runs))
        for i in range(0,input_len):
        	if i == 0 and self.runs == 0: #first run
        		output_items[0][i] = input_items[0][i] # copy payload
        		output_items[1][i] = 95 # prints _ on the data stream
        		# print('Packet Counter first Run-> {}' .format(input_items[0][i]))
        		self.last_run_position = input_len-(i+1)# stores last correct relative index before counter reset
        		self.offset_position = self.last_run_position # offset of the samples from last run
        	else:
	        	if (i+1+self.offset_position) % self.data_period == 0:
	        		output_items[0][i] = input_items[0][i]
	        		output_items[1][i] = 95 # prints _ on the data stream
	        		self.last_run_position = input_len-(i+1)# stores last correct relative index before counter reset
	        		# print('Packet Counter -> {}' .format(input_items[0][i]))
	        		# print('Loop index -> {}' .format(i))
	        	else:
	        		output_items[0][i] = 95 # prints _ on the counter stream
	        		output_items[1][i] = input_items[0][i]

	self.runs += 1
        return len(output_items[0])
