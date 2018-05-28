"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import datetime


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block  - This block takes the packet numbers of the received window size packets and calculates the quantity of the lost packets
       As for today, it only works for window sizes multiples of the length of the data.
    """

    def __init__(self, threshold=0.35,window_size=1, modulus=1,average_length=10, reset_call = False, state_tries = 10):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='ACM Controller',   # will show up in GRC
            in_sig=[np.int8],
            out_sig=[np.float32,np.int8]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.window_size = window_size
        self.threshold = threshold # PER threshold that controls the ACM state machine.
        self.average_length = average_length # How many measurements are used to calculate the per.
        self.modulus = modulus # modulus of the packet counter, how log it takes to return to zero.
        self.history = np.zeros(self.average_length) #vector that stores the last average length pers
        self.reset_call = reset_call # resets to BPSK e FEC
        self.state = 0 # 0 = BPSK 1 = QPSK 2 = 8PSK
        self.state_tries = state_tries # how many work calls one state is kept before changing it.
        self.work_calls = 0
        self.reset_control = False #controls reset so it does not happen very often.

        self.set_history(window_size)
    

    def calc_average_per(self,new_per):
        
        #make a param for treshold and to controll permanency on states.
        self.history = np.roll(self.history,1)
        
        self.history[0] = new_per

        average_per = np.mean(self.history)
        # Desired per is max 0.35
        if self.state == 0: #BPSK
            if self.work_calls == self.state_tries:
                self.reset_control = True
                self.work_calls = 0
                if average_per <=self.threshold:
                    self.state = 1
                 
        elif self.state == 1: #QPSK
            if self.work_calls == self.state_tries:
                self.reset_control = True 
                self.work_calls = 0
                if average_per <= self.threshold:
                    self.state = 2
                else:
                    self.state = 1
        else: #8PSK
            if self.work_calls == self.state_tries:
                self.reset_control = True 
                self.work_calls = 0   
                if average_per > self.threshold:
                    self.state = 1
                   

        # print("History {} , Average {}".format(self.history,average_per))
        return average_per


    def work(self, input_items, output_items):
    	# Restarts machine
        if self.reset_call and self.reset_control:
            self.reset_control = False
            self.state = 0
            self.work_calls = 0
            output_items[1][:] = 0 # Must restart port because changing just the state would not work.
            st = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M:%S%p")
            print("RESET at",st)
            return len(output_items[1]) # Must return one so produce is calles. As this is a Sync Block.

        consumed = (len(input_items[0])-self.window_size+1)
        if  consumed < self.window_size:
            return 0

        self.work_calls += 1
        for i in range(0 , consumed):
            # if self.window_size+i < len(input_items[0]):
            observed = input_items[0][i:self.window_size+i] %256

            errors = sum((np.diff(observed) % self.modulus)-1)

            per = max((float(errors)/(self.window_size+errors)),0)
            # print("Observed {}".format(observed))
            # print("PER {}".format(per))
            output_items[0][i] = self.calc_average_per(per)
            output_items[1][i] = self.state
        return len(output_items[0])
