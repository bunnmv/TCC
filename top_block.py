#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed May 16 10:05:25 2018
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
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from tx_outer_CE import tx_outer_CE  # grc-generated hier_block
from tx_outer_dummy import tx_outer_dummy  # grc-generated hier_block
import RWN
import numpy as np
import pmt
import sip
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
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
        # Variables
        ##################################################
        self.packetCounterLength = packetCounterLength = 1
        self.infoLength = infoLength = 22*30
        self.samp_rate_0 = samp_rate_0 = 32000
        self.samp_rate = samp_rate = 32000
        self.packetLength = packetLength = (infoLength+packetCounterLength+4)
        self.len_tag_name_2 = len_tag_name_2 = "len_key2"
        self.len_tag_name = len_tag_name = "len_key"
        self.dataLength = dataLength = (infoLength+packetCounterLength)
        self.access_code = access_code = '0101110111101101' * 3
        self.FEC = FEC = 0

        ##################################################
        # Blocks
        ##################################################
        self._FEC_options = (0, 1, )
        self._FEC_labels = ('Dummy', 'Rate 1/2 C.C', )
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
        self.top_layout.addWidget(self._FEC_group_box)
        self.tx_outer_dummy_0 = tx_outer_dummy(
            dataLength=dataLength,
            infoLength=infoLength,
            len_tag_name=len_tag_name,
            packetCounterLength=packetCounterLength,
            packetLength=packetLength,
        )
        self.tx_outer_CE_0 = tx_outer_CE(
            dataLength=dataLength,
            infoLength=infoLength,
            len_tag_name=len_tag_name_2,
            packetCounterLength=packetCounterLength,
            packetLength=packetLength,
        )
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Conv", #name
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
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "len_key")
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
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate*1000,True)
        self.blocks_tag_gate_0_0 = blocks.tag_gate(gr.sizeof_char * 1, False)
        self.blocks_tag_gate_0_0.set_single_key("")
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_char * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, packetLength*8, len_tag_name)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 2*packetLength*8, len_tag_name_2)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_char*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/Users/marcusbunn/Documents/engtelecom/TCC/programming/SDR/2600-0.txt', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.RWN_selector_3_1_bb_0 = RWN.selector_3_1_bb(FEC, True)
        self.RWN_selector_1_3_bb_1_0 = RWN.selector_1_3_bb(FEC, False)
        self.RWN_selector_1_3_bb_1 = RWN.selector_1_3_bb(FEC, False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.RWN_selector_1_3_bb_1, 2), (self.blocks_null_sink_0, 0))
        self.connect((self.RWN_selector_1_3_bb_1, 1), (self.tx_outer_CE_0, 0))
        self.connect((self.RWN_selector_1_3_bb_1, 0), (self.tx_outer_dummy_0, 0))
        self.connect((self.RWN_selector_1_3_bb_1_0, 2), (self.blocks_null_sink_0_0, 0))
        self.connect((self.RWN_selector_1_3_bb_1_0, 1), (self.blocks_tag_gate_0, 0))
        self.connect((self.RWN_selector_1_3_bb_1_0, 0), (self.blocks_tag_gate_0_0, 0))
        self.connect((self.RWN_selector_3_1_bb_0, 0), (self.RWN_selector_1_3_bb_1_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.RWN_selector_3_1_bb_0, 2))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_tag_gate_0_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.RWN_selector_1_3_bb_1, 0))
        self.connect((self.tx_outer_CE_0, 0), (self.RWN_selector_3_1_bb_0, 1))
        self.connect((self.tx_outer_dummy_0, 0), (self.RWN_selector_3_1_bb_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
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

    def get_infoLength(self):
        return self.infoLength

    def set_infoLength(self, infoLength):
        self.infoLength = infoLength
        self.set_packetLength((self.infoLength+self.packetCounterLength+4))
        self.set_dataLength((self.infoLength+self.packetCounterLength))
        self.tx_outer_dummy_0.set_infoLength(self.infoLength)
        self.tx_outer_CE_0.set_infoLength(self.infoLength)

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*1000)

    def get_packetLength(self):
        return self.packetLength

    def set_packetLength(self, packetLength):
        self.packetLength = packetLength
        self.tx_outer_dummy_0.set_packetLength(self.packetLength)
        self.tx_outer_CE_0.set_packetLength(self.packetLength)
        self.blocks_stream_to_tagged_stream_0_0.set_packet_len(self.packetLength*8)
        self.blocks_stream_to_tagged_stream_0_0.set_packet_len_pmt(self.packetLength*8)
        self.blocks_stream_to_tagged_stream_0.set_packet_len(2*self.packetLength*8)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(2*self.packetLength*8)

    def get_len_tag_name_2(self):
        return self.len_tag_name_2

    def set_len_tag_name_2(self, len_tag_name_2):
        self.len_tag_name_2 = len_tag_name_2
        self.tx_outer_CE_0.set_len_tag_name(self.len_tag_name_2)

    def get_len_tag_name(self):
        return self.len_tag_name

    def set_len_tag_name(self, len_tag_name):
        self.len_tag_name = len_tag_name
        self.tx_outer_dummy_0.set_len_tag_name(self.len_tag_name)

    def get_dataLength(self):
        return self.dataLength

    def set_dataLength(self, dataLength):
        self.dataLength = dataLength
        self.tx_outer_dummy_0.set_dataLength(self.dataLength)
        self.tx_outer_CE_0.set_dataLength(self.dataLength)

    def get_access_code(self):
        return self.access_code

    def set_access_code(self, access_code):
        self.access_code = access_code

    def get_FEC(self):
        return self.FEC

    def set_FEC(self, FEC):
        self.FEC = FEC
        self._FEC_callback(self.FEC)
        self.RWN_selector_3_1_bb_0.set_selected(self.FEC)
        self.RWN_selector_1_3_bb_1_0.set_selected(self.FEC)
        self.RWN_selector_1_3_bb_1.set_selected(self.FEC)


def main(top_block_cls=top_block, options=None):

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
