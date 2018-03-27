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
        self.aux_position = 0

    def work(self, input_items, output_items): 
    	"""example: multiply with constant"""       
    	# if self.counter_length > 0: # packet counter has to be greater then one
     #    	output_items[0][:self.counter_length] = input_items[0][ :self.counter_length]
     #    	output_items[0][self.counter_length:self.payload_length] = 89 # prints Y
        	
     #    	output_items[1][ :self.counter_length] = 88 # sync blocks needs same quantity of itens on the output. Prints 'X'
     #    	output_items[1][self.counter_length:self.payload_length] = input_items[0][self.counter_length:self.payload_length]
     #    else:
     #    	output_items[0][:] = 0
     #    	output_items[1][:] = 0

        	#i*payload_length
        #when loop counter resets work funtion is called again
    	input_len = len(input_items[0]);
    	sample = input_len/(self.payload_length+self.counter_length)
    	data_length = (self.payload_length+self.counter_length)
    	data_period = 0
        for i in range(0,len(input_items[0])):
        	if i == 0 and self.aux_position  > 0 : # counter has been reset
    			data_period = self.aux_position  #new 0 index = rest of samples before shift
    			print(data_period)
    		else:
    			data_period = self.aux_position+data_length 
        	if (i+1) % data_period == 0:
        		output_items[0][i] = input_items[0][i]
        		output_items[1][i] = 43 # prints + on the data stream
        		# print(i+1)
        		# print(input_items[0][i])
        		self.aux_position = (input_len-(i+1)) # stores last correct data before counter reset
        	else:
        		output_items[0][i] = 43 # prints + on the counter stream
        		output_items[1][i] = input_items[0][i]
    		# print(i)
    		# print(self.aux_position)
        return len(output_items[0])
