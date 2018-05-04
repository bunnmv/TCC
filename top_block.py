#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri May  4 19:38:39 2018
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
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from rx_inner import rx_inner  # grc-generated hier_block
from rx_outer import rx_outer  # grc-generated hier_block
from tx_inner import tx_inner  # grc-generated hier_block
from tx_outer import tx_outer  # grc-generated hier_block
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
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.frameLength = frameLength = packetLength+12
        self.excess_bw = excess_bw = 0.35
        self.M_PSK = M_PSK = 2
        self.theta = theta = 0
        self.samp_rate = samp_rate = 3200000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, excess_bw, 45*nfilts)
        self.psk = psk = digital.psk_constellation(M_PSK,digital.mod_codes.NO_CODE, True)
        self.dataLength = dataLength = (infoLength+packetCounterLength)
        self.channel_rotation = channel_rotation = 0
        self.channel_noise = channel_noise = 0


        self.CE = CE = fec.cc_encoder_make(frameLength*8, 7, 2, ([79,109]), 0, fec.CC_STREAMING, False)



        self.CD = CD = fec.cc_decoder.make(frameLength*8, 7, 2, ([79,109]), 0, -1, fec.CC_STREAMING, False)


        ##################################################
        # Blocks
        ##################################################
        self._theta_range = Range(0, 2*np.pi, np.pi/4, 0, 200)
        self._theta_win = RangeWidget(self._theta_range, self.set_theta, "theta", "counter_slider", float)
        self.top_grid_layout.addWidget(self._theta_win, 0,1,1,1)
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
        self._channel_rotation_range = Range(0, 2*np.pi, 0.1, 0, 200)
        self._channel_rotation_win = RangeWidget(self._channel_rotation_range, self.set_channel_rotation, "channel_rotation", "counter_slider", float)
        self.top_grid_layout.addWidget(self._channel_rotation_win, 0,2,1,1)
        self._channel_noise_range = Range(0, 2, 0.01, 0, 200)
        self._channel_noise_win = RangeWidget(self._channel_noise_range, self.set_channel_noise, "channel_noise", "counter_slider", float)
        self.top_grid_layout.addWidget(self._channel_noise_win, 0,3,1,1)
        self.tx_outer_0 = tx_outer()
        self.tx_inner_0 = tx_inner(
            dataLength=dataLength,
            infoLength=infoLength,
            packetCounterLength=packetCounterLength,
        )
        self.rx_outer_0 = rx_outer(
            dataLength=dataLength,
            infoLength=infoLength,
            packetCounterLength=packetCounterLength,
        )
        self.rx_inner_0 = rx_inner(
            excess_bw=excess_bw,
            mod_init_point=psk.points()[0],
            nfilts=nfilts,
            order_costas=psk.arity(),
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
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("SPS")

        labels = ['SPS', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1.enable_grid(False)
        self.qtgui_const_sink_x_1.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_1.disable_legend()

        labels = ['Costas', '', '', '', '',
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
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_const_sink_x_1_win)
        self.fec_extended_tagged_encoder_0 = fec.extended_tagged_encoder(encoder_obj_list=CE, puncpat='11', lentagname='len_key', mtu=packetLength)
        self.fec_extended_tagged_decoder_0 = self.fec_extended_tagged_decoder_0 = fec_extended_tagged_decoder_0 = fec.extended_tagged_decoder(decoder_obj_list=CD, ann=None, puncpat='11', integration_period=10000, lentagname='len_key2', mtu=packetLength)
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_ff_ts(digital.packet_utils.default_access_code,
          0, 'len_key2')
        self.digital_constellation_soft_decoder_cf_0 = digital.constellation_soft_decoder_cf(psk.base())
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
        	noise_voltage=channel_noise,
        	frequency_offset=1e-4,
        	epsilon=1.001,
        	taps=(1*np.exp(1j*channel_rotation), ),
        	noise_seed=0,
        	block_tags=True
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_head_0 = blocks.head(gr.sizeof_char*1, 110000)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/Users/marcusbunn/Documents/engtelecom/TCC/programming/SDR/2600-0.txt', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/header_counter.txt', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/payload.txt', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_char_to_float_1_1_0 = blocks.char_to_float(1, 1)
        self._M_PSK_options = (2, 4, 8, )
        self._M_PSK_labels = ('DBPSK', 'DQPSK', 'D8PSK', )
        self._M_PSK_group_box = Qt.QGroupBox("M_PSK")
        self._M_PSK_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._M_PSK_button_group = variable_chooser_button_group()
        self._M_PSK_group_box.setLayout(self._M_PSK_box)
        for i, label in enumerate(self._M_PSK_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._M_PSK_box.addWidget(radio_button)
        	self._M_PSK_button_group.addButton(radio_button, i)
        self._M_PSK_callback = lambda i: Qt.QMetaObject.invokeMethod(self._M_PSK_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._M_PSK_options.index(i)))
        self._M_PSK_callback(self.M_PSK)
        self._M_PSK_button_group.buttonClicked[int].connect(
        	lambda i: self.set_M_PSK(self._M_PSK_options[i]))
        self.top_grid_layout.addWidget(self._M_PSK_group_box, 0,4,1,1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_1_1_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.tx_inner_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.rx_inner_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.digital_constellation_soft_decoder_cf_0, 0), (self.digital_correlate_access_code_xx_ts_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.fec_extended_tagged_decoder_0, 0))
        self.connect((self.fec_extended_tagged_decoder_0, 0), (self.blocks_char_to_float_1_1_0, 0))
        self.connect((self.fec_extended_tagged_decoder_0, 0), (self.rx_outer_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0, 0), (self.tx_outer_0, 0))
        self.connect((self.rx_inner_0, 1), (self.digital_constellation_soft_decoder_cf_0, 0))
        self.connect((self.rx_inner_0, 1), (self.qtgui_const_sink_x_1, 0))
        self.connect((self.rx_inner_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.rx_outer_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.rx_outer_0, 1), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.tx_inner_0, 0), (self.fec_extended_tagged_encoder_0, 0))
        self.connect((self.tx_outer_0, 0), (self.digital_constellation_modulator_0, 0))

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
        self.tx_inner_0.set_packetCounterLength(self.packetCounterLength)
        self.rx_outer_0.set_packetCounterLength(self.packetCounterLength)

    def get_infoLength(self):
        return self.infoLength

    def set_infoLength(self, infoLength):
        self.infoLength = infoLength
        self.set_packetLength((self.infoLength+self.packetCounterLength+4))
        self.set_dataLength((self.infoLength+self.packetCounterLength))
        self.tx_inner_0.set_infoLength(self.infoLength)
        self.rx_outer_0.set_infoLength(self.infoLength)

    def get_packetLength(self):
        return self.packetLength

    def set_packetLength(self, packetLength):
        self.packetLength = packetLength
        self.set_frameLength(self.packetLength+12)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, 45*self.nfilts))
        self.rx_inner_0.set_sps(self.sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, 45*self.nfilts))
        self.rx_inner_0.set_nfilts(self.nfilts)

    def get_frameLength(self):
        return self.frameLength

    def set_frameLength(self, frameLength):
        self.frameLength = frameLength

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, 45*self.nfilts))
        self.rx_inner_0.set_excess_bw(self.excess_bw)

    def get_M_PSK(self):
        return self.M_PSK

    def set_M_PSK(self, M_PSK):
        self.M_PSK = M_PSK
        self.set_psk(digital.psk_constellation(self.M_PSK,digital.mod_codes.NO_CODE, True))
        self._M_PSK_callback(self.M_PSK)

    def get_theta(self):
        return self.theta

    def set_theta(self, theta):
        self.theta = theta
        self.rx_inner_0.set_theta(self.theta)

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
        self.rx_inner_0.set_rrc_taps(self.rrc_taps)

    def get_psk(self):
        return self.psk

    def set_psk(self, psk):
        self.psk = psk

    def get_dataLength(self):
        return self.dataLength

    def set_dataLength(self, dataLength):
        self.dataLength = dataLength
        self.tx_inner_0.set_dataLength(self.dataLength)
        self.rx_outer_0.set_dataLength(self.dataLength)

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

    def get_CE(self):
        return self.CE

    def set_CE(self, CE):
        self.CE = CE

    def get_CD(self):
        return self.CD

    def set_CD(self, CD):
        self.CD = CD


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
