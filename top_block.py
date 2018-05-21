#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun May 20 20:23:33 2018
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
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
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
        self.packetCounterLength = packetCounterLength = 0
        self.infoLength = infoLength = 22*10
        self.packetLength = packetLength = (infoLength+packetCounterLength+4)
        self.frameLength = frameLength = packetLength
        self.sps = sps = 4
        self.samp_rate = samp_rate = 3200000
        self.psk2 = psk2 = digital.psk_constellation(4,digital.mod_codes.NO_CODE, True)
        self.psk = psk = digital.psk_constellation(2,digital.mod_codes.NO_CODE, True)
        self.excess_bw = excess_bw = 0.35
        self.dataLength = dataLength = (infoLength+packetCounterLength)
        self.FEC = FEC = 0


        self.DE = DE = fec.dummy_encoder_make(frameLength*8)



        self.DD = DD = fec.dummy_decoder.make(frameLength*8)



        self.CE = CE = fec.cc_encoder_make(frameLength*8, 7, 2, ([79,109]), 0, fec.CC_STREAMING, False)



        self.CD = CD = fec.cc_decoder.make(frameLength*8, 7, 2, ([79,109]), 0, -1, fec.CC_STREAMING, False)


        ##################################################
        # Blocks
        ##################################################
        self._FEC_options = (0, 1, )
        self._FEC_labels = ('CC 1/2', 'Dummy', )
        self._FEC_group_box = Qt.QGroupBox("FEC")
        self._FEC_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._FEC_button_group = variable_chooser_button_group()
        self._FEC_group_box.setLayout(self._FEC_box)
        for i, label in enumerate(self._FEC_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._FEC_box.addWidget(radio_button)
        	self._FEC_button_group.addButton(radio_button, i)
        self._FEC_callback = lambda i: Qt.QMetaObject.invokeMethod(self._FEC_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._FEC_options.index(i)))
        self._FEC_callback(self.FEC)
        self._FEC_button_group.buttonClicked[int].connect(
        	lambda i: self.set_FEC(self._FEC_options[i]))
        self.top_grid_layout.addWidget(self._FEC_group_box, 0,2,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
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
        self.fec_extended_tagged_encoder_0_0 = fec.extended_tagged_encoder(encoder_obj_list=DE, puncpat='11', lentagname='len_key', mtu=packetLength)
        self.fec_extended_tagged_encoder_0 = fec.extended_tagged_encoder(encoder_obj_list=CE, puncpat='11', lentagname='len_key', mtu=packetLength)
        self.fec_extended_tagged_decoder_0_0 = self.fec_extended_tagged_decoder_0_0 = fec_extended_tagged_decoder_0_0 = fec.extended_tagged_decoder(decoder_obj_list=DD, ann=None, puncpat='11', integration_period=10000, lentagname='len_key', mtu=packetLength)
        self.fec_extended_tagged_decoder_0 = self.fec_extended_tagged_decoder_0 = fec_extended_tagged_decoder_0 = fec.extended_tagged_decoder(decoder_obj_list=CD, ann=None, puncpat='11', integration_period=10000, lentagname='len_key', mtu=packetLength)
        self.digital_map_bb_0_0 = digital.map_bb((-1,1))
        self.digital_map_bb_0 = digital.map_bb((-1,1))
        self.digital_crc32_bb_1 = digital.crc32_bb(True, "len_key", True)
        self.digital_crc32_bb_0 = digital.crc32_bb(False, "len_key", True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, dataLength, "len_key")
        self.blocks_stream_mux_1 = blocks.stream_mux(gr.sizeof_char*1, (packetLength*8, packetLength*8))
        self.blocks_repack_bits_bb_0_0_0_0 = blocks.repack_bits_bb(8, 1, 'len_key', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(1, 8, 'len_key', False, gr.GR_MSB_FIRST)
        self.blocks_keep_m_in_n_0_0 = blocks.keep_m_in_n(gr.sizeof_char, packetLength*8, packetLength*8*2, packetLength*8*FEC)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/Users/marcusbunn/Documents/engtelecom/TCC/programming/SDR/2600-0.txt', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/header_counter.txt', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(True)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_and_const_xx_0 = blocks.and_const_bb(0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_and_const_xx_0, 0), (self.blocks_stream_mux_1, 1))
        self.connect((self.blocks_char_to_float_0, 0), (self.fec_extended_tagged_decoder_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.fec_extended_tagged_decoder_0_0, 0))
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_keep_m_in_n_0_0, 0), (self.blocks_repack_bits_bb_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.digital_crc32_bb_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0, 0), (self.fec_extended_tagged_encoder_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0, 0), (self.fec_extended_tagged_encoder_0_0, 0))
        self.connect((self.blocks_stream_mux_1, 0), (self.blocks_keep_m_in_n_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.digital_crc32_bb_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.digital_crc32_bb_0, 0), (self.blocks_repack_bits_bb_0_0_0_0, 0))
        self.connect((self.digital_crc32_bb_1, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.digital_crc32_bb_1, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.fec_extended_tagged_decoder_0, 0), (self.blocks_stream_mux_1, 0))
        self.connect((self.fec_extended_tagged_decoder_0_0, 0), (self.blocks_and_const_xx_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0_0, 0), (self.digital_map_bb_0_0, 0))

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

    def get_infoLength(self):
        return self.infoLength

    def set_infoLength(self, infoLength):
        self.infoLength = infoLength
        self.set_packetLength((self.infoLength+self.packetCounterLength+4))
        self.set_dataLength((self.infoLength+self.packetCounterLength))

    def get_packetLength(self):
        return self.packetLength

    def set_packetLength(self, packetLength):
        self.packetLength = packetLength
        self.set_frameLength(self.packetLength)
        self.blocks_keep_m_in_n_0_0.set_offset(self.packetLength*8*self.FEC)
        self.blocks_keep_m_in_n_0_0.set_m(self.packetLength*8)
        self.blocks_keep_m_in_n_0_0.set_n(self.packetLength*8*2)

    def get_frameLength(self):
        return self.frameLength

    def set_frameLength(self, frameLength):
        self.frameLength = frameLength

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_psk2(self):
        return self.psk2

    def set_psk2(self, psk2):
        self.psk2 = psk2

    def get_psk(self):
        return self.psk

    def set_psk(self, psk):
        self.psk = psk

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_dataLength(self):
        return self.dataLength

    def set_dataLength(self, dataLength):
        self.dataLength = dataLength
        self.blocks_stream_to_tagged_stream_0_0.set_packet_len(self.dataLength)
        self.blocks_stream_to_tagged_stream_0_0.set_packet_len_pmt(self.dataLength)

    def get_FEC(self):
        return self.FEC

    def set_FEC(self, FEC):
        self.FEC = FEC
        self._FEC_callback(self.FEC)
        self.blocks_keep_m_in_n_0_0.set_offset(self.packetLength*8*self.FEC)

    def get_DE(self):
        return self.DE

    def set_DE(self, DE):
        self.DE = DE

    def get_DD(self):
        return self.DD

    def set_DD(self, DD):
        self.DD = DD

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
