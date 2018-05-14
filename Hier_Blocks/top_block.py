#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon May 14 15:19:31 2018
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from tx_outer_CE import tx_outer_CE  # grc-generated hier_block
from tx_outer_dummy import tx_outer_dummy  # grc-generated hier_block
import RWN
import my_framer_bpsk
import numpy as np
import pmt
import sip
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, hdr_format=digital.header_format_default(digital.packet_utils.default_access_code, 0)):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.hdr_format = hdr_format

        ##################################################
        # Variables
        ##################################################
        self.packetCounterLength = packetCounterLength = 1
        self.infoLength = infoLength = 22*10
        self.packetLength = packetLength = (infoLength+packetCounterLength+4)
        self.access_code = access_code = '0101110111101101' * 3
        self.sps = sps = 4
        self.samp_rate = samp_rate = 32000
        self.psk = psk = digital.psk_constellation(2,digital.mod_codes.NO_CODE, True)
        self.len_tag_name = len_tag_name = "len_key"
        self.frameLength = frameLength = packetLength+len(access_code)
        self.excess_bw = excess_bw = 0.35
        self.dataLength = dataLength = (infoLength+packetCounterLength)

        ##################################################
        # Blocks
        ##################################################
        self.tx_outer_dummy_0 = tx_outer_dummy(
            dataLength=dataLength,
            frameLength=frameLength,
            infoLength=infoLength,
            packetCounterLength=packetCounterLength,
            packetLength=packetLength,
            len_tag_name=len_tag_name,
        )
        self.tx_outer_CE_0 = tx_outer_CE(
            dataLength=dataLength,
            frameLength=frameLength,
            infoLength=infoLength,
            packetCounterLength=packetCounterLength,
            packetLength=packetLength,
            len_tag_name=len_tag_name,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Dummy", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.my_framer_bpsk = my_framer_bpsk.blk(access_code=access_code, payload_length=dataLength, tag_name=len_tag_name)
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=psk.base(),
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=excess_bw,
          verbose=True,
          log=False,
          )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0.2,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate*100,True)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, len_tag_name, 0)
        self.blocks_repack_bits_bb_0_0_0_0_0_0 = blocks.repack_bits_bb(1, 8, len_tag_name, False, gr.GR_MSB_FIRST)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_char*1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/Users/marcusbunn/Documents/engtelecom/TCC/programming/SDR/2600-0.txt', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_char_to_float_1_1_0_0_0 = blocks.char_to_float(1, 1)
        self.RWN_selector_3_1_bb_0 = RWN.selector_3_1_bb(0, True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.RWN_selector_3_1_bb_0, 0), (self.blocks_char_to_float_1_1_0_0_0, 0))
        self.connect((self.RWN_selector_3_1_bb_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.RWN_selector_3_1_bb_0, 0), (self.my_framer_bpsk, 0))
        self.connect((self.blocks_char_to_float_1_1_0_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.RWN_selector_3_1_bb_0, 2))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0_0_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.blocks_repack_bits_bb_0_0_0_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.tx_outer_CE_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.tx_outer_dummy_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.my_framer_bpsk, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.tx_outer_CE_0, 0), (self.RWN_selector_3_1_bb_0, 1))
        self.connect((self.tx_outer_dummy_0, 0), (self.RWN_selector_3_1_bb_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_packetCounterLength(self):
        return self.packetCounterLength

    def set_packetCounterLength(self, packetCounterLength):
        self.packetCounterLength = packetCounterLength
        self.set_packetLength((self.infoLength+self.packetCounterLength+4))
        self.set_dataLength((self.infoLength+self.packetCounterLength))
        self.tx_outer_dummy_0.set_packetCounterLength(self.packetCounterLength)
        self.tx_outer_CE_0.set_packetCounterLength(self.packetCounterLength)

    def get_infoLength(self):
        return self.infoLength

    def set_infoLength(self, infoLength):
        self.infoLength = infoLength
        self.set_packetLength((self.infoLength+self.packetCounterLength+4))
        self.set_dataLength((self.infoLength+self.packetCounterLength))
        self.tx_outer_dummy_0.set_infoLength(self.infoLength)
        self.tx_outer_CE_0.set_infoLength(self.infoLength)

    def get_packetLength(self):
        return self.packetLength

    def set_packetLength(self, packetLength):
        self.packetLength = packetLength
        self.set_frameLength(self.packetLength+len(self.access_code))
        self.tx_outer_dummy_0.set_packetLength(self.packetLength)
        self.tx_outer_CE_0.set_packetLength(self.packetLength)

    def get_access_code(self):
        return self.access_code

    def set_access_code(self, access_code):
        self.access_code = access_code
        self.set_frameLength(self.packetLength+len(self.access_code))
        self.my_framer_bpsk.access_code = self.access_code

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*100)

    def get_psk(self):
        return self.psk

    def set_psk(self, psk):
        self.psk = psk

    def get_len_tag_name(self):
        return self.len_tag_name

    def set_len_tag_name(self, len_tag_name):
        self.len_tag_name = len_tag_name
        self.tx_outer_dummy_0.set_len_tag_name(self.len_tag_name)
        self.tx_outer_CE_0.set_len_tag_name(self.len_tag_name)
        self.my_framer_bpsk.tag_name = self.len_tag_name

    def get_frameLength(self):
        return self.frameLength

    def set_frameLength(self, frameLength):
        self.frameLength = frameLength
        self.tx_outer_dummy_0.set_frameLength(self.frameLength)
        self.tx_outer_CE_0.set_frameLength(self.frameLength)

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_dataLength(self):
        return self.dataLength

    def set_dataLength(self, dataLength):
        self.dataLength = dataLength
        self.tx_outer_dummy_0.set_dataLength(self.dataLength)
        self.tx_outer_CE_0.set_dataLength(self.dataLength)
        self.my_framer_bpsk.payload_length = self.dataLength


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

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
