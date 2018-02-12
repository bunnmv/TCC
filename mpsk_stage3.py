#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Mpsk Stage3
# Generated: Mon Feb 12 10:41:13 2018
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
from gnuradio import audio
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy as np
import sip
import sys
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
        self.sps = sps = 2
        self.nfilts = nfilts = 32
        self.timing_loop_bw = timing_loop_bw = 6.82/100
        self.time_offset = time_offset = 1.00
        self.taps = taps = [1.0 + 0.0j, ]
        self.samp_rate = samp_rate = 48e3
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 45*nfilts)

        self.qpsk2 = qpsk2 = digital.constellation_8psk().base()

        self.noise_volt = noise_volt = 0.0001
        self.excess_bw = excess_bw = 0.75
        self.delay = delay = 9


        self.DE = DE = fec.dummy_encoder_make(2048)



        self.DD = DD = fec.dummy_decoder.make(2048)



        self.CC_D = CC_D = fec.cc_decoder.make(2048, 7, 2, ([79,109]), 0, -1, fec.CC_STREAMING, False)



        self.CC = CC = fec.cc_encoder_make(2048, 7, 2, ([79,109]), 0, fec.CC_STREAMING, False)


        ##################################################
        # Blocks
        ##################################################
        self._timing_loop_bw_range = Range(0.0, 0.2, 0.01, 6.82/100, 200)
        self._timing_loop_bw_win = RangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, 'Time: BW', "slider", float)
        self.top_grid_layout.addWidget(self._timing_loop_bw_win, 0,3,1,1)
        self._time_offset_range = Range(0.999, 1.001, 0.0001, 1.00, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, 'Timing Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._time_offset_win, 0,2,1,1)
        self._noise_volt_range = Range(0, 10, 0.01, 0.0001, 200)
        self._noise_volt_win = RangeWidget(self._noise_volt_range, self.set_noise_volt, 'Noise Voltage', "counter_slider", float)
        self.top_grid_layout.addWidget(self._noise_volt_win, 0,0,1,1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

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
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	2048, #size
        	'', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()

        labels = ['Timing Recov.', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [0.5, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win, 1,2,1,2)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	2048, #size
        	'', #name
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

        labels = ['RX Data', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [0.5, 1.0, 1.0, 1.0, 1.0,
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 1,0,1,2)
        self.low_pass_filter_0 = filter.fir_filter_fff(2, firdes.low_pass(
        	1, samp_rate, 20e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.fec_extended_encoder_0 = fec.extended_encoder(encoder_obj_list=DE, threading= None, puncpat='11')
        self.fec_extended_decoder_0 = fec.extended_decoder(decoder_obj_list=DD, threading= None, ann=None, puncpat='11', integration_period=10000)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps*1.00, timing_loop_bw, (rrc_taps), nfilts, nfilts/2, 1.5, 1)
        self.digital_constellation_soft_decoder_cf_0 = digital.constellation_soft_decoder_cf(qpsk2)
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
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise_volt,
        	frequency_offset=0,
        	epsilon=time_offset,
        	taps=(taps),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/Users/marcusbunn/Documents/engtelecom/SDR/bob.wav', True)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, int(np.power(2,7)-1))
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 127.0)
        self.audio_sink_0 = audio.sink(48000, '', True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.fec_extended_encoder_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.digital_constellation_soft_decoder_cf_0, 0), (self.fec_extended_decoder_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_constellation_soft_decoder_cf_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.fec_extended_decoder_0, 0), (self.blocks_pack_k_bits_bb_0_0, 0))
        self.connect((self.fec_extended_encoder_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.audio_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_time_sink_x_1, 0))

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
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_loop_bw)

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset
        self.channels_channel_model_0.set_timing_offset(self.time_offset)

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.channels_channel_model_0.set_taps((self.taps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 20e3, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_qpsk2(self):
        return self.qpsk2

    def set_qpsk2(self, qpsk2):
        self.qpsk2 = qpsk2

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt
        self.channels_channel_model_0.set_noise_voltage(self.noise_volt)

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay

    def get_DE(self):
        return self.DE

    def set_DE(self, DE):
        self.DE = DE

    def get_DD(self):
        return self.DD

    def set_DD(self, DD):
        self.DD = DD

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
