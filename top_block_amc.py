#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block Amc
# Generated: Fri May 11 11:15:20 2018
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
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from rx_inner_8psk import rx_inner_8psk  # grc-generated hier_block
from rx_inner_bpsk import rx_inner_bpsk  # grc-generated hier_block
from rx_inner_qpsk import rx_inner_qpsk  # grc-generated hier_block
from rx_outer_convolutional import rx_outer_convolutional  # grc-generated hier_block
from rx_outer_dummy import rx_outer_dummy  # grc-generated hier_block
from tx_inner_8psk import tx_inner_8psk  # grc-generated hier_block
from tx_inner_bpsk import tx_inner_bpsk  # grc-generated hier_block
from tx_inner_qpsk import tx_inner_qpsk  # grc-generated hier_block
from tx_outer_CE import tx_outer_CE  # grc-generated hier_block
from tx_outer_dummy import tx_outer_dummy  # grc-generated hier_block
import RWN
import numpy as np
import pmt
import sip
from gnuradio import qtgui


class top_block_amc(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block Amc")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block Amc")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block_amc")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.packetCounterLength = packetCounterLength = 1
        self.infoLength = infoLength = 22*10
        self.sps = sps = 4
        self.packetLength = packetLength = (infoLength+packetCounterLength+4)
        self.nfilts = nfilts = 32
        self.excess_bw = excess_bw = 0.35
        self.theta = theta = 0
        self.samp_rate = samp_rate = 3200000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, excess_bw, 45*nfilts)
        self.frameLength = frameLength = packetLength+12
        self.dataLength = dataLength = (infoLength+packetCounterLength)
        self.channel_rotation = channel_rotation = 0
        self.channel_noise = channel_noise = 0
        self.access_code = access_code = '101010'

        ##################################################
        # Blocks
        ##################################################
        self._theta_range = Range(0, 2*np.pi, np.pi/4, 0, 200)
        self._theta_win = RangeWidget(self._theta_range, self.set_theta, "theta", "counter_slider", float)
        self.top_grid_layout.addWidget(self._theta_win, 0,1,1,1)
        self._channel_rotation_range = Range(0, 2*np.pi, 0.1, 0, 200)
        self._channel_rotation_win = RangeWidget(self._channel_rotation_range, self.set_channel_rotation, "channel_rotation", "counter_slider", float)
        self.top_grid_layout.addWidget(self._channel_rotation_win, 0,2,1,1)
        self._channel_noise_range = Range(0, 2, 0.01, 0, 200)
        self._channel_noise_win = RangeWidget(self._channel_noise_range, self.set_channel_noise, "channel_noise", "counter_slider", float)
        self.top_grid_layout.addWidget(self._channel_noise_win, 0,3,1,1)
        self.tx_outer_dummy_0 = tx_outer_dummy(
            dataLength=dataLength,
            frameLength=frameLength,
            infoLength=infoLength,
            packetCounterLength=packetCounterLength,
            packetLength=packetLength,
        )
        self.tx_outer_CE_0 = tx_outer_CE(
            dataLength=dataLength,
            infoLength=infoLength,
            packetCounterLength=packetCounterLength,
            packetLength=packetLength,
            frameLength=frameLength,
        )
        self.tx_inner_qpsk_0 = tx_inner_qpsk(
            access_code=access_code,
            payloadLength=dataLength,
            roll_off=excess_bw,
            sps=sps,
        )
        self.tx_inner_bpsk_0 = tx_inner_bpsk(
            access_code=access_code,
            payloadLength=dataLength,
            roll_off=excess_bw,
            sps=sps,
        )
        self.tx_inner_8psk_0 = tx_inner_8psk(
            access_code=access_code,
            payloadLength=dataLength,
            roll_off=excess_bw,
            sps=sps,
        )
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'After Costas')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'PER Rate')
        self.top_layout.addWidget(self.tab)
        self.rx_outer_dummy_0 = rx_outer_dummy(
            dataLength=dataLength,
            frameLength=frameLength,
            infoLength=infoLength,
            packetCounterLength=packetCounterLength,
            packetLength=packetLength,
        )
        self.rx_outer_convolutional_0 = rx_outer_convolutional(
            dataLength=1,
            frameLength=0,
            infoLength=1,
            packetCounterLength=1,
            packetLength=0,
        )
        self.rx_inner_qpsk_0 = rx_inner_qpsk(
            excess_bw=excess_bw,
            nfilts=nfilts,
            rrc_taps=rrc_taps,
            sps=sps,
            theta=theta,
        )
        self.rx_inner_bpsk_0 = rx_inner_bpsk(
            excess_bw=excess_bw,
            nfilts=nfilts,
            rrc_taps=rrc_taps,
            sps=sps,
            theta=theta,
        )
        self.rx_inner_8psk_0 = rx_inner_8psk(
            excess_bw=excess_bw,
            nfilts=nfilts,
            rrc_taps=rrc_taps,
            sps=sps,
            theta=theta,
        )
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "len_key2")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['After Decoding', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 1,0,1,4)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=channel_noise,
        	frequency_offset=1e-4,
        	epsilon=1.001,
        	taps=(1*np.exp(1j*channel_rotation), ),
        	noise_seed=0,
        	block_tags=True
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_null_source_2 = blocks.null_source(gr.sizeof_char*1)
        self.blocks_null_source_1 = blocks.null_source(gr.sizeof_char*1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_char*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_keep_m_in_n_0_0 = blocks.keep_m_in_n(gr.sizeof_char, infoLength, dataLength, packetCounterLength)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_char, packetCounterLength, dataLength, 0)
        self.blocks_head_0 = blocks.head(gr.sizeof_char*1, 110000)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/Users/marcusbunn/Documents/engtelecom/TCC/programming/SDR/2600-0.txt', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/header_counter.txt', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/payload.txt', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_char_to_float_1_1_0 = blocks.char_to_float(1, 1)
        self.RWN_selector_3_1_ff_0 = RWN.selector_3_1_ff(0, True)
        self.RWN_selector_3_1_cc_0 = RWN.selector_3_1_cc(0, True)
        self.RWN_selector_3_1_bb_2 = RWN.selector_3_1_bb(0, True)
        self.RWN_selector_3_1_bb_1 = RWN.selector_3_1_bb(0, True)
        self.RWN_selector_3_1_bb_0 = RWN.selector_3_1_bb(0, True)
        self.RWN_selector_1_3_cc_0 = RWN.selector_1_3_cc(0, True)
        self.RWN_selector_1_3_bb_0 = RWN.selector_1_3_bb(0, True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.RWN_selector_1_3_bb_0, 2), (self.blocks_null_sink_0, 0))
        self.connect((self.RWN_selector_1_3_bb_0, 1), (self.tx_outer_CE_0, 0))
        self.connect((self.RWN_selector_1_3_bb_0, 0), (self.tx_outer_dummy_0, 0))
        self.connect((self.RWN_selector_1_3_cc_0, 2), (self.rx_inner_8psk_0, 0))
        self.connect((self.RWN_selector_1_3_cc_0, 0), (self.rx_inner_bpsk_0, 0))
        self.connect((self.RWN_selector_1_3_cc_0, 1), (self.rx_inner_qpsk_0, 0))
        self.connect((self.RWN_selector_3_1_bb_0, 0), (self.tx_inner_8psk_0, 0))
        self.connect((self.RWN_selector_3_1_bb_0, 0), (self.tx_inner_bpsk_0, 0))
        self.connect((self.RWN_selector_3_1_bb_0, 0), (self.tx_inner_qpsk_0, 0))
        self.connect((self.RWN_selector_3_1_bb_1, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.RWN_selector_3_1_bb_1, 0), (self.blocks_keep_m_in_n_0_0, 0))
        self.connect((self.RWN_selector_3_1_bb_2, 0), (self.blocks_char_to_float_1_1_0, 0))
        self.connect((self.RWN_selector_3_1_cc_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.RWN_selector_3_1_ff_0, 0), (self.rx_outer_convolutional_0, 0))
        self.connect((self.RWN_selector_3_1_ff_0, 0), (self.rx_outer_dummy_0, 0))
        self.connect((self.blocks_char_to_float_1_1_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.RWN_selector_3_1_bb_0, 2))
        self.connect((self.blocks_null_source_1, 0), (self.RWN_selector_3_1_bb_1, 2))
        self.connect((self.blocks_null_source_2, 0), (self.RWN_selector_3_1_bb_2, 2))
        self.connect((self.blocks_throttle_0, 0), (self.RWN_selector_1_3_bb_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.RWN_selector_1_3_cc_0, 0))
        self.connect((self.rx_inner_8psk_0, 0), (self.RWN_selector_3_1_ff_0, 2))
        self.connect((self.rx_inner_bpsk_0, 0), (self.RWN_selector_3_1_ff_0, 0))
        self.connect((self.rx_inner_qpsk_0, 0), (self.RWN_selector_3_1_ff_0, 1))
        self.connect((self.rx_outer_convolutional_0, 0), (self.RWN_selector_3_1_bb_1, 1))
        self.connect((self.rx_outer_convolutional_0, 1), (self.RWN_selector_3_1_bb_2, 1))
        self.connect((self.rx_outer_dummy_0, 0), (self.RWN_selector_3_1_bb_1, 0))
        self.connect((self.rx_outer_dummy_0, 1), (self.RWN_selector_3_1_bb_2, 0))
        self.connect((self.tx_inner_8psk_0, 0), (self.RWN_selector_3_1_cc_0, 2))
        self.connect((self.tx_inner_bpsk_0, 0), (self.RWN_selector_3_1_cc_0, 0))
        self.connect((self.tx_inner_qpsk_0, 0), (self.RWN_selector_3_1_cc_0, 1))
        self.connect((self.tx_outer_CE_0, 0), (self.RWN_selector_3_1_bb_0, 1))
        self.connect((self.tx_outer_dummy_0, 0), (self.RWN_selector_3_1_bb_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block_amc")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_packetCounterLength(self):
        return self.packetCounterLength

    def set_packetCounterLength(self, packetCounterLength):
        self.packetCounterLength = packetCounterLength
        self.set_packetLength((self.infoLength+self.packetCounterLength+4))
        self.set_dataLength((self.infoLength+self.packetCounterLength))
        self.tx_outer_dummy_0.set_packetCounterLength(self.packetCounterLength)
        self.tx_outer_CE_0.set_packetCounterLength(self.packetCounterLength)
        self.rx_outer_dummy_0.set_packetCounterLength(self.packetCounterLength)
        self.blocks_keep_m_in_n_0_0.set_offset(self.packetCounterLength)
        self.blocks_keep_m_in_n_0.set_m(self.packetCounterLength)

    def get_infoLength(self):
        return self.infoLength

    def set_infoLength(self, infoLength):
        self.infoLength = infoLength
        self.set_packetLength((self.infoLength+self.packetCounterLength+4))
        self.set_dataLength((self.infoLength+self.packetCounterLength))
        self.tx_outer_dummy_0.set_infoLength(self.infoLength)
        self.tx_outer_CE_0.set_infoLength(self.infoLength)
        self.rx_outer_dummy_0.set_infoLength(self.infoLength)
        self.blocks_keep_m_in_n_0_0.set_m(self.infoLength)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, 45*self.nfilts))
        self.tx_inner_qpsk_0.set_sps(self.sps)
        self.tx_inner_bpsk_0.set_sps(self.sps)
        self.tx_inner_8psk_0.set_sps(self.sps)
        self.rx_inner_qpsk_0.set_sps(self.sps)
        self.rx_inner_bpsk_0.set_sps(self.sps)
        self.rx_inner_8psk_0.set_sps(self.sps)

    def get_packetLength(self):
        return self.packetLength

    def set_packetLength(self, packetLength):
        self.packetLength = packetLength
        self.set_frameLength(self.packetLength+12)
        self.tx_outer_dummy_0.set_packetLength(self.packetLength)
        self.tx_outer_CE_0.set_packetLength(self.packetLength)
        self.rx_outer_dummy_0.set_packetLength(self.packetLength)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, 45*self.nfilts))
        self.rx_inner_qpsk_0.set_nfilts(self.nfilts)
        self.rx_inner_bpsk_0.set_nfilts(self.nfilts)
        self.rx_inner_8psk_0.set_nfilts(self.nfilts)

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, 45*self.nfilts))
        self.tx_inner_qpsk_0.set_roll_off(self.excess_bw)
        self.tx_inner_bpsk_0.set_roll_off(self.excess_bw)
        self.tx_inner_8psk_0.set_roll_off(self.excess_bw)
        self.rx_inner_qpsk_0.set_excess_bw(self.excess_bw)
        self.rx_inner_bpsk_0.set_excess_bw(self.excess_bw)
        self.rx_inner_8psk_0.set_excess_bw(self.excess_bw)

    def get_theta(self):
        return self.theta

    def set_theta(self, theta):
        self.theta = theta
        self.rx_inner_qpsk_0.set_theta(self.theta)
        self.rx_inner_bpsk_0.set_theta(self.theta)
        self.rx_inner_8psk_0.set_theta(self.theta)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.rx_inner_qpsk_0.set_rrc_taps(self.rrc_taps)
        self.rx_inner_bpsk_0.set_rrc_taps(self.rrc_taps)
        self.rx_inner_8psk_0.set_rrc_taps(self.rrc_taps)

    def get_frameLength(self):
        return self.frameLength

    def set_frameLength(self, frameLength):
        self.frameLength = frameLength
        self.tx_outer_dummy_0.set_frameLength(self.frameLength)
        self.tx_outer_CE_0.set_frameLength(self.frameLength)
        self.rx_outer_dummy_0.set_frameLength(self.frameLength)

    def get_dataLength(self):
        return self.dataLength

    def set_dataLength(self, dataLength):
        self.dataLength = dataLength
        self.tx_outer_dummy_0.set_dataLength(self.dataLength)
        self.tx_outer_CE_0.set_dataLength(self.dataLength)
        self.tx_inner_qpsk_0.set_payloadLength(self.dataLength)
        self.tx_inner_bpsk_0.set_payloadLength(self.dataLength)
        self.tx_inner_8psk_0.set_payloadLength(self.dataLength)
        self.rx_outer_dummy_0.set_dataLength(self.dataLength)
        self.blocks_keep_m_in_n_0_0.set_n(self.dataLength)
        self.blocks_keep_m_in_n_0.set_n(self.dataLength)

    def get_channel_rotation(self):
        return self.channel_rotation

    def set_channel_rotation(self, channel_rotation):
        self.channel_rotation = channel_rotation
        self.channels_channel_model_0.set_taps((1*np.exp(1j*self.channel_rotation), ))

    def get_channel_noise(self):
        return self.channel_noise

    def set_channel_noise(self, channel_noise):
        self.channel_noise = channel_noise
        self.channels_channel_model_0.set_noise_voltage(self.channel_noise)

    def get_access_code(self):
        return self.access_code

    def set_access_code(self, access_code):
        self.access_code = access_code
        self.tx_inner_qpsk_0.set_access_code(self.access_code)
        self.tx_inner_bpsk_0.set_access_code(self.access_code)
        self.tx_inner_8psk_0.set_access_code(self.access_code)


def main(top_block_cls=top_block_amc, options=None):

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
