#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Apr 24 16:21:50 2018
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
import math
import numpy
import pmt
import sip
import sys
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
        self.nfilts = nfilts = 64
        self.frameLength = frameLength = packetLength+12
        self.excess_bw = excess_bw = 0.35
        self.snr = snr = 0
        self.samp_rate = samp_rate = 32000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, excess_bw, 45*nfilts)
        self.order_costas = order_costas = 8
        self.dataLength = dataLength = (infoLength+packetCounterLength)

        self.MO = MO = digital.constellation_8psk().base()

        self.MO.gen_soft_dec_lut(8)


        self.CE = CE = fec.cc_encoder_make(frameLength*8, 7, 2, ([79,109]), 0, fec.CC_STREAMING, False)



        self.CD = CD = fec.cc_decoder.make(frameLength*8, 7, 2, ([79,109]), 0, -1, fec.CC_STREAMING, False)


        ##################################################
        # Blocks
        ##################################################
        self._snr_range = Range(0, 1, 0.01, 0, 200)
        self._snr_win = RangeWidget(self._snr_range, self.set_snr, "snr", "counter_slider", float)
        self.top_layout.addWidget(self._snr_win)
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
        markers = [-1, -1, -1, -1, -1,
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
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
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
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_win)
        self.fec_extended_tagged_encoder_0 = fec.extended_tagged_encoder(encoder_obj_list=CE, puncpat='11', lentagname='len_key', mtu=packetLength)
        self.fec_extended_tagged_decoder_0 = self.fec_extended_tagged_decoder_0 = fec_extended_tagged_decoder_0 = fec.extended_tagged_decoder(decoder_obj_list=CD, ann=None, puncpat='11', integration_period=10000, lentagname='len_key2', mtu=packetLength)
        self.digital_symbol_sync_xx_0_0 = digital.symbol_sync_cc(digital.TED_SIGNAL_TIMES_SLOPE_ML, sps, 6.82/100, 1.0/math.sqrt(2.0), 1.0, 0.5, 1, digital.constellation_8psk().base(), digital.IR_PFB_MF, nfilts, (rrc_taps))
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, 'len_key')
        self.digital_crc32_bb_0_0 = digital.crc32_bb(True, "len_key2", True)
        self.digital_crc32_bb_0 = digital.crc32_bb(False, "len_key", True)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(6.82/100, order_costas, False)
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_ff_ts(digital.packet_utils.default_access_code,
          0, 'len_key2')
        self.digital_constellation_soft_decoder_cf_0 = digital.constellation_soft_decoder_cf(MO)
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=MO,
          differential=False,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=excess_bw,
          verbose=True,
          log=False,
          )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0,
        	frequency_offset=1e-4,
        	epsilon=1.001,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=0,
        	block_tags=True
        )
        self.blocks_vector_source_x_0 = blocks.vector_source_b(numpy.arange(0,256), True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'len_key', 0)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, dataLength, "len_key")
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_char*1, (packetCounterLength, infoLength))
        self.blocks_repack_bits_bb_0_0_0_0_0_0 = blocks.repack_bits_bb(1, 8, 'len_key', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0_0 = blocks.repack_bits_bb(8, 1, 'len_key', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(1, 8, 'len_key2', False, gr.GR_MSB_FIRST)
        self.blocks_keep_m_in_n_0_0 = blocks.keep_m_in_n(gr.sizeof_char, infoLength, dataLength, packetCounterLength)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_char, packetCounterLength, dataLength, 0)
        self.blocks_head_0 = blocks.head(gr.sizeof_char*1, 110000)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/sender.txt', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/header_counter.txt', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/payload.txt', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_char_to_float_1_1_0 = blocks.char_to_float(1, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_1_1_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.digital_crc32_bb_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0, 0), (self.fec_extended_tagged_encoder_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0_0_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0_0_0, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_crc32_bb_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.digital_symbol_sync_xx_0_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.digital_constellation_soft_decoder_cf_0, 0), (self.digital_correlate_access_code_xx_ts_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.fec_extended_tagged_decoder_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_constellation_soft_decoder_cf_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_1, 0))
        self.connect((self.digital_crc32_bb_0, 0), (self.blocks_repack_bits_bb_0_0_0_0, 0))
        self.connect((self.digital_crc32_bb_0_0, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.digital_crc32_bb_0_0, 0), (self.blocks_keep_m_in_n_0_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.fec_extended_tagged_decoder_0, 0), (self.blocks_char_to_float_1_1_0, 0))
        self.connect((self.fec_extended_tagged_decoder_0, 0), (self.blocks_repack_bits_bb_0_0_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0, 0), (self.blocks_repack_bits_bb_0_0_0_0_0_0, 0))

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
        self.blocks_keep_m_in_n_0_0.set_offset(self.packetCounterLength)
        self.blocks_keep_m_in_n_0.set_m(self.packetCounterLength)

    def get_infoLength(self):
        return self.infoLength

    def set_infoLength(self, infoLength):
        self.infoLength = infoLength
        self.set_packetLength((self.infoLength+self.packetCounterLength+4))
        self.set_dataLength((self.infoLength+self.packetCounterLength))
        self.blocks_keep_m_in_n_0_0.set_m(self.infoLength)

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

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, 45*self.nfilts))

    def get_frameLength(self):
        return self.frameLength

    def set_frameLength(self, frameLength):
        self.frameLength = frameLength

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, 45*self.nfilts))

    def get_snr(self):
        return self.snr

    def set_snr(self, snr):
        self.snr = snr

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

    def get_order_costas(self):
        return self.order_costas

    def set_order_costas(self, order_costas):
        self.order_costas = order_costas

    def get_dataLength(self):
        return self.dataLength

    def set_dataLength(self, dataLength):
        self.dataLength = dataLength
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.dataLength)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.dataLength)
        self.blocks_keep_m_in_n_0_0.set_n(self.dataLength)
        self.blocks_keep_m_in_n_0.set_n(self.dataLength)

    def get_MO(self):
        return self.MO

    def set_MO(self, MO):
        self.MO = MO

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
