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
        self.data_length = (self.payload_length+self.counter_length)

    def work(self, input_items, output_items): 
        # """example: multiply with constant"""  
        # data_length = (self.payload_length+self.counter_length)     
        # if self.counter_length > 0: # packet counter has to be greater then one
        #   output_items[0][:] = 43
     #      output_items[0][:data_length:] = input_items[0][:data_length:]
     #      #output_items[0][self.counter_length:self.payload_length] = 43 # prints +
            
     #      output_items[1][:data_length:] = 43 # sync blocks needs same quantity of itens on the output. Prints '+'
     #      output_items[1][self.counter_length:self.payload_length] = input_items[0][self.counter_length:self.payload_length]
     #    else:
     #      output_items[0][:] = 0
     #      output_items[1][:] = 0

     #    #when loop counter resets work funtion is called again
        input_len = len(input_items[0]);
        self.offset_position = self.last_run_position # offset of the samples from last run
        print('offset run ->{}' .format(self.offset_position))
        print('Input ->{}' .format(input_len))
        #self.data_period = self.data_length-self.offset_position

        for i in range(0,input_len):
            # if self.last_run_position > 0:
            #   self.data_period = self.data_length-self.offset_position
            # else:
            #   self.data_period = self.data_length
    #       if i == 0: # counter reset or first itaration
    #           if self.last_run_position > 0: # counter has been reset
    #               data_period = data_length-self.last_run_position # offset of the samples from last run
    #               self.offset_position = data_period
    #               #self.last_run_position = 0 # resets the auxiliar
    #               print('Data period - 1 ->{}' .format(data_period))
    #               # print('Input len1 {}' .format(input_len))
    #               # print('last run1 {}' .format(self.last_run_position))
    #               print('offset run - 1 ->{}' .format(self.offset_position))
    #       else:
                # data_period = self.offset_position+data_length
                #print('Data period - 2 -> {}' .format(data_period))
                # print('Input len2 {}' .format(input_len))
                # print('last run2 {}' .format(self.last_run_position))
                #print('offset run - 2 -> {}' .format(self.offset_position))
            if (i+1+self.offset_position) % self.data_period == 0:
                output_items[0][i] = input_items[0][i]
                output_items[1][i] = 43 # prints + on the data stream
                self.last_run_position = input_len-(i+1)# stores last correct relative index before counter reset
                #self.offset_position = 0 # after the first time, the offset returns to zero, as the period goes back to data_length
                print('Data period on % ->{} i -> {} input -> {} offset ->{}' .format(self.data_period,i,input_items[0][i],self.offset_position))
                #self.data_period = self.data_length
                #print('last run on set {}' .format(self.last_run_position))
            else:
                output_items[0][i] = 43 # prints + on the counter stream
                output_items[1][i] = input_items[0][i]

        return len(output_items[0])
