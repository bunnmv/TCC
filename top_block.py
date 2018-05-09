#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed May  9 14:52:29 2018
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import RWN
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
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.value = value = 0
        self.samp_rate = samp_rate = 32000
        self.port = port = 0

        ##################################################
        # Blocks
        ##################################################
        self._port_options = (0, 1, 2, )
        self._port_labels = (str(self._port_options[0]), str(self._port_options[1]), str(self._port_options[2]), )
        self._port_tool_bar = Qt.QToolBar(self)
        self._port_tool_bar.addWidget(Qt.QLabel("port"+": "))
        self._port_combo_box = Qt.QComboBox()
        self._port_tool_bar.addWidget(self._port_combo_box)
        for label in self._port_labels: self._port_combo_box.addItem(label)
        self._port_callback = lambda i: Qt.QMetaObject.invokeMethod(self._port_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._port_options.index(i)))
        self._port_callback(self.port)
        self._port_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_port(self._port_options[i]))
        self.top_layout.addWidget(self._port_tool_bar)
        self.blocks_probe_signal_x_0 = blocks.probe_signal_b()

        def _value_probe():
            while True:
                val = self.blocks_probe_signal_x_0.level()
                try:
                    self.set_value(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _value_thread = threading.Thread(target=_value_probe)
        _value_thread.daemon = True
        _value_thread.start()

        self.RWN_selector_3_1_bb_0 = RWN.selector_3_1_bb(port, True)

        def _variable_function_probe_0_probe():
            while True:
                val = self.RWN_selector_3_1_bb_0.set_selected(value)
                try:
                    self.set_variable_function_probe_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (20))
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()

        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-3, 3)

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
        self.blocks_vector_source_x_0 = blocks.vector_source_b((0, 1), True, 1, [])
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_char*1, samp_rate*100,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate*100,True)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_char*1)
        self.blocks_float_to_char_0_0 = blocks.float_to_char(1, 1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.RWN_selector_3_1_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_char_0_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.RWN_selector_3_1_bb_0, 1))
        self.connect((self.blocks_float_to_char_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.RWN_selector_3_1_bb_0, 2))
        self.connect((self.blocks_throttle_0, 0), (self.RWN_selector_3_1_bb_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_probe_signal_x_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_throttle_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_function_probe_0(self):
        return self.variable_function_probe_0

    def set_variable_function_probe_0(self, variable_function_probe_0):
        self.variable_function_probe_0 = variable_function_probe_0

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate*100)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*100)

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port
        self._port_callback(self.port)
        self.RWN_selector_3_1_bb_0.set_selected(self.port)


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
