#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Mpsk Stage3
# Generated: Wed Oct 11 14:43:22 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy as np
import osmosdr
import sys
import time
from gnuradio import qtgui


class mpsk_stage3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Mpsk Stage3")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Mpsk Stage3")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "mpsk_stage3")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.nfilts = nfilts = 32
        self.timing_loop_bw = timing_loop_bw = 6.28/100.0
        self.time_offset = time_offset = 1.00
        self.taps = taps = [1.0 + 0.0j, ]
        self.samp_rate = samp_rate = 48000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 45*nfilts)

        self.qpsk2 = qpsk2 = digital.constellation_qpsk().base()

        self.noise_volt = noise_volt = 0.0001
        self.excess_bw = excess_bw = 0.35
        self.delay = delay = 9


        self.CC_D = CC_D = fec.cc_decoder.make(2048, 7, 2, ([79,109]), 0, -1, fec.CC_STREAMING, False)



        self.CC = CC = fec.cc_encoder_make(2048, 7, 2, ([79,109]), 0, fec.CC_STREAMING, False)


        ##################################################
        # Blocks
        ##################################################
        self._timing_loop_bw_range = Range(0.0, 0.2, 0.01, 6.28/100.0, 200)
        self._timing_loop_bw_win = RangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, 'Time: BW', "slider", float)
        self.top_grid_layout.addWidget(self._timing_loop_bw_win, 0,3,1,1)
        self._time_offset_range = Range(0.999, 1.001, 0.0001, 1.00, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, 'Timing Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._time_offset_win, 0,2,1,1)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(2.88e6)
        self.osmosdr_sink_0.set_center_freq(300e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(30, 0)
        self.osmosdr_sink_0.set_bb_gain(30, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self._noise_volt_range = Range(0, 10, 0.01, 0.0001, 200)
        self._noise_volt_win = RangeWidget(self._noise_volt_range, self.set_noise_volt, 'Noise Voltage', "counter_slider", float)
        self.top_grid_layout.addWidget(self._noise_volt_win, 0,0,1,1)
        self.fec_extended_encoder_0 = fec.extended_encoder(encoder_obj_list=CC, threading= None, puncpat='11')
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=qpsk2,
          differential=False,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=excess_bw,
          verbose=False,
          log=False,
          )
        self._delay_range = Range(0, 100, 1, 9, 200)
        self._delay_win = RangeWidget(self._delay_range, self.set_delay, 'Delay time', "counter_slider", int)
        self.top_grid_layout.addWidget(self._delay_win, 0,1,1,1)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/Users/marcusbunn/Documents/engtelecom/SDR/bob.wav', True)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, int(np.power(2,7)-1))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.fec_extended_encoder_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.fec_extended_encoder_0, 0), (self.blocks_pack_k_bits_bb_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "mpsk_stage3")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 45*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 45*self.nfilts))

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_qpsk2(self):
        return self.qpsk2

    def set_qpsk2(self, qpsk2):
        self.qpsk2 = qpsk2

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay

    def get_CC_D(self):
        return self.CC_D

    def set_CC_D(self, CC_D):
        self.CC_D = CC_D

    def get_CC(self):
        return self.CC

    def set_CC(self, CC):
        self.CC = CC


def main(top_block_cls=mpsk_stage3, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
