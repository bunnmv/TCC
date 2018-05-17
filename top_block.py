#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu May 17 14:41:20 2018
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import RWN
import numpy as np
import per_calc_test_probe
import sip
import sys
import threading
import time
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
        self.restart = restart = 0
        self.port = port = 0
        self.samp_rate = samp_rate = 32000
        self.restart_call = restart_call = restart>0
        self.new_port = new_port = int(np.round((port*2.4)))
        self.keep = keep = 20

        ##################################################
        # Blocks
        ##################################################
        self.probe = blocks.probe_signal_f()
        self.probe2 = blocks.probe_signal_b()

        def _port_probe():
            while True:
                val = self.probe.level()
                try:
                    self.set_port(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (100000))
        _port_thread = threading.Thread(target=_port_probe)
        _port_thread.daemon = True
        _port_thread.start()


        def _restart_probe():
            while True:
                val = self.probe2.level()
                try:
                    self.set_restart(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (0.5))
        _restart_thread = threading.Thread(target=_restart_probe)
        _restart_thread.daemon = True
        _restart_thread.start()

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
        self.qtgui_number_sink_0_1_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_1_0.set_update_time(0.04)
        self.qtgui_number_sink_0_1_0.set_title("New Port")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_1_0.set_min(i, -1)
            self.qtgui_number_sink_0_1_0.set_max(i, 1)
            self.qtgui_number_sink_0_1_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_1_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_1_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_1_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_1_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_1_0.enable_autoscale(False)
        self._qtgui_number_sink_0_1_0_win = sip.wrapinstance(self.qtgui_number_sink_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_1_0_win)
        self.qtgui_number_sink_0_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_1.set_update_time(0.04)
        self.qtgui_number_sink_0_1.set_title("Port")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_1.set_min(i, -1)
            self.qtgui_number_sink_0_1.set_max(i, 1)
            self.qtgui_number_sink_0_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_1.set_label(i, labels[i])
            self.qtgui_number_sink_0_1.set_unit(i, units[i])
            self.qtgui_number_sink_0_1.set_factor(i, factor[i])

        self.qtgui_number_sink_0_1.enable_autoscale(False)
        self._qtgui_number_sink_0_1_win = sip.wrapinstance(self.qtgui_number_sink_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_1_win)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("PER")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.per_calc_test_probe = per_calc_test_probe.blk(window_size=20, modulus=256)
        self._keep_range = Range(5, 20, 1, 20, 200)
        self._keep_win = RangeWidget(self._keep_range, self.set_keep, "keep", "counter_slider", int)
        self.top_layout.addWidget(self._keep_win)
        self.digital_map_bb_0 = digital.map_bb((1,2,3,4,5,6,7,8,9,0))
        self.digital_crc32_bb_0_0 = digital.crc32_bb(False, "packet_len", True)
        self.digital_crc32_bb_0 = digital.crc32_bb(True, "packet_len", True)
        self.blocks_vector_source_x_0 = blocks.vector_source_b(np.arange(256), True, 1, [])
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate*100,True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 10, "packet_len")
        self.blocks_float_to_char_0_1 = blocks.float_to_char(1, 1)
        self.blocks_float_to_char_0_0 = blocks.float_to_char(1, 1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.analog_const_source_x_1_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, restart_call*new_port)
        self.analog_const_source_x_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, port)
        self.analog_const_source_x_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 5)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 10)
        self.RWN_selector_3_1_bb_0 = RWN.selector_3_1_bb(new_port*restart_call, True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.RWN_selector_3_1_bb_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_char_0_0, 0))
        self.connect((self.analog_const_source_x_0_1, 0), (self.blocks_float_to_char_0_1, 0))
        self.connect((self.analog_const_source_x_1, 0), (self.qtgui_number_sink_0_1, 0))
        self.connect((self.analog_const_source_x_1_0, 0), (self.qtgui_number_sink_0_1_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.RWN_selector_3_1_bb_0, 1))
        self.connect((self.blocks_float_to_char_0_0, 0), (self.RWN_selector_3_1_bb_0, 2))
        self.connect((self.blocks_float_to_char_0_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_crc32_bb_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.RWN_selector_3_1_bb_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.digital_crc32_bb_0, 0), (self.per_calc_test_probe, 0))
        self.connect((self.digital_crc32_bb_0, 0), (self.probe2, 0))
        self.connect((self.digital_crc32_bb_0_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_crc32_bb_0, 0))
        self.connect((self.per_calc_test_probe, 0), (self.probe, 0))
        self.connect((self.per_calc_test_probe, 0), (self.qtgui_number_sink_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_restart(self):
        return self.restart

    def set_restart(self, restart):
        self.restart = restart
        self.set_restart_call(self.restart>0)

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port
        self.set_new_port(int(np.round((self.port*2.4))))
        self.analog_const_source_x_1.set_offset(self.port)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*100)

    def get_restart_call(self):
        return self.restart_call

    def set_restart_call(self, restart_call):
        self.restart_call = restart_call
        self.analog_const_source_x_1_0.set_offset(self.restart_call*self.new_port)
        self.RWN_selector_3_1_bb_0.set_selected(self.new_port*self.restart_call)

    def get_new_port(self):
        return self.new_port

    def set_new_port(self, new_port):
        self.new_port = new_port
        self.analog_const_source_x_1_0.set_offset(self.restart_call*self.new_port)
        self.RWN_selector_3_1_bb_0.set_selected(self.new_port*self.restart_call)

    def get_keep(self):
        return self.keep

    def set_keep(self, keep):
        self.keep = keep


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
