# TCC

These files represent the first steps towards the objective of our research, which is to develop a LOS radio link utilizing adaptative coding and modulation
and bit interleaved coded modulation.Even more, the files are mainly flowgraphs from gnuradio companion followed by the respective python files.
At first, we begin by testing the exemples availalble at gr-ditital/packet/examples, where we plan to transfer a .txt file over the channel by sending
frames that are made by a header and a payload, where each may have its own modulation and coding scheme. Later, our goal is to develop a block responsible
for controlling the modulation and coding schemes of the payload by reading a reverse channel containing either the BER or FER of the received information.
As so, the BER or FER, will be compared to a trashold that will be utilized to control the modulation and coding schemes.

I plan to keep this folder updated weekly, feel free to contact me at bunnmv@gmail.com 
