#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block Amc
# Generated: Sat May 19 19:16:35 2018
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
from gnuradio import analog
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
from my_rx_inner import my_rx_inner  # grc-generated hier_block
from my_tx_inner import my_tx_inner  # grc-generated hier_block
from optparse import OptionParser
from rx_outer import rx_outer  # grc-generated hier_block
from tx_outer import tx_outer  # grc-generated hier_block
import RWN
import numpy as np
import per_calc_port_select
import pmt
import sip
import threading
import time
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
        self.symbol_rate = symbol_rate = 384000
        self.samp_rate = samp_rate = 4*288e3
        self.packet_counter = packet_counter = 1
        self.info_length = info_length = 500
        self.sps_float = sps_float = samp_rate / symbol_rate
        self.packet_length = packet_length = (info_length+packet_counter+4)
        self.access_code_dummy = access_code_dummy = '1010001000010010'
        self.sps = sps = int(sps_float)
        self.restart_call = restart_call = True
        self.port = port = 0
        self.nfilts = nfilts = 32
        self.full_frame_bits_dummy = full_frame_bits_dummy = packet_length*8 + len(access_code_dummy)
        self.full_frame_bits_conv = full_frame_bits_conv = packet_length*2*8 + len(access_code_dummy)
        self.fec_choice = fec_choice = 0
        self.excess_bw = excess_bw = 0.8
        self.theta = theta = 0
        self.sdr_rate = sdr_rate = 8*288e3
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, excess_bw, 45*nfilts)
        self.restart_check = restart_check = 0
        self.restart = restart = 0
        self.mod_choice = mod_choice = port*restart_call
        self.len_tag_name_rx = len_tag_name_rx = "len_key2"
        self.len_tag_name = len_tag_name = "len_key"
        self.is_conv = is_conv = fec_choice == 0
        self.frame_bits = frame_bits = packet_length*8 + packet_length*8*fec_choice
        self.fec_position = fec_position = 0
        self.fec_options = fec_options = [0,0,1]
        self.fec_len_menu = fec_len_menu = [full_frame_bits_conv,full_frame_bits_dummy]
        self.data_length = data_length = (info_length+packet_counter)

        self.constellation_qpsk = constellation_qpsk = digital.constellation_qpsk().base()


        self.constellation_bpsk = constellation_bpsk = digital.constellation_bpsk().base()


        self.constellation_8psk = constellation_8psk = digital.constellation_8psk().base()

        self.channel_rotation = channel_rotation = 0
        self.channel_noise = channel_noise = 0
        self.access_code_conv = access_code_conv = '0101110111101101'


        self.DE = DE = fec.dummy_encoder_make(packet_length*8)



        self.DD = DD = fec.dummy_decoder.make(packet_length*8)



        self.CE = CE = fec.cc_encoder_make(packet_length*8, 7, 2, ([79,109]), 0, fec.CC_STREAMING, False)



        self.CD = CD = fec.cc_decoder.make(packet_length*8, 7, 2, ([79,109]), 0, -1, fec.CC_STREAMING, False)


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
        self.probe3 = blocks.probe_signal_b()
        self.probe2 = blocks.probe_signal_b()
        self.probe = blocks.probe_signal_b()
        self._mod_choice_options = (0, 1, 2, )
        self._mod_choice_labels = ('DBPSK', 'DQPSK', 'D8PSK', )
        self._mod_choice_group_box = Qt.QGroupBox('Modulation')
        self._mod_choice_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._mod_choice_button_group = variable_chooser_button_group()
        self._mod_choice_group_box.setLayout(self._mod_choice_box)
        for i, label in enumerate(self._mod_choice_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._mod_choice_box.addWidget(radio_button)
        	self._mod_choice_button_group.addButton(radio_button, i)
        self._mod_choice_callback = lambda i: Qt.QMetaObject.invokeMethod(self._mod_choice_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._mod_choice_options.index(i)))
        self._mod_choice_callback(self.mod_choice)
        self._mod_choice_button_group.buttonClicked[int].connect(
        	lambda i: self.set_mod_choice(self._mod_choice_options[i]))
        self.top_grid_layout.addWidget(self._mod_choice_group_box, 0,4,1,1)
        self._fec_choice_options = (0, 1, )
        self._fec_choice_labels = ('Rate 1/2 C.C', 'Dummy', )
        self._fec_choice_group_box = Qt.QGroupBox('FEC')
        self._fec_choice_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._fec_choice_button_group = variable_chooser_button_group()
        self._fec_choice_group_box.setLayout(self._fec_choice_box)
        for i, label in enumerate(self._fec_choice_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._fec_choice_box.addWidget(radio_button)
        	self._fec_choice_button_group.addButton(radio_button, i)
        self._fec_choice_callback = lambda i: Qt.QMetaObject.invokeMethod(self._fec_choice_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._fec_choice_options.index(i)))
        self._fec_choice_callback(self.fec_choice)
        self._fec_choice_button_group.buttonClicked[int].connect(
        	lambda i: self.set_fec_choice(self._fec_choice_options[i]))
        self.top_grid_layout.addWidget(self._fec_choice_group_box, 0,5,1,1)
        self._channel_rotation_range = Range(0, 2*np.pi, 0.1, 0, 200)
        self._channel_rotation_win = RangeWidget(self._channel_rotation_range, self.set_channel_rotation, "channel_rotation", "counter_slider", float)
        self.top_grid_layout.addWidget(self._channel_rotation_win, 0,2,1,1)
        self._channel_noise_range = Range(0, 2, 0.01, 0, 200)
        self._channel_noise_win = RangeWidget(self._channel_noise_range, self.set_channel_noise, "channel_noise", "counter_slider", float)
        self.top_grid_layout.addWidget(self._channel_noise_win, 0,3,1,1)
        self.tx_outer_0_0 = tx_outer(
            access_code=access_code_dummy,
            data_length=data_length,
            encoder=DE,
            len_tag_name=len_tag_name,
        )
        self.tx_outer_0 = tx_outer(
            access_code=access_code_conv,
            data_length=data_length,
            encoder=DE,
            len_tag_name=len_tag_name,
        )
        self.rx_outer_0_0 = rx_outer(
            access_code=access_code_dummy,
            decoder=DD,
            len_tag_name_rx=len_tag_name_rx,
            packet_length=packet_length,
        )
        self.rx_outer_0 = rx_outer(
            access_code=access_code_conv,
            decoder=DD,
            len_tag_name_rx=len_tag_name_rx,
            packet_length=packet_length,
        )

        def _restart_check_probe():
            while True:
                val = self.probe3.level()
                try:
                    self.set_restart_check(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (0.5 + samp_rate/1e7))
        _restart_check_thread = threading.Thread(target=_restart_check_probe)
        _restart_check_thread.daemon = True
        _restart_check_thread.start()


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

        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"After CRC", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "len_key2")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_win, 1,1,5,5)
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
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_1_win, 6,3,1,5)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("PER")

        labels = ['', '', '', '', '',
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
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 6,1,1,2)
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
        self.tab_layout_0.addWidget(self._qtgui_const_sink_x_0_win)
        self.probe4 = blocks.probe_signal_b()
        self.per_calc_port_select = per_calc_port_select.blk(window_size=20, modulus=256, average_length=10)
        self.my_tx_inner_0_1 = my_tx_inner(
            constellation=constellation_8psk,
            rolloff=excess_bw,
            sps=sps,
        )
        self.my_tx_inner_0_0 = my_tx_inner(
            constellation=constellation_qpsk,
            rolloff=excess_bw,
            sps=sps,
        )
        self.my_tx_inner_0 = my_tx_inner(
            constellation=constellation_bpsk,
            rolloff=excess_bw,
            sps=sps,
        )
        self.my_rx_inner_0_1 = my_rx_inner(
            constellation=constellation_8psk,
            phase_rot_after_costas_loop=theta,
            rolloff=excess_bw,
            sps=sps,
        )
        self.my_rx_inner_0_0 = my_rx_inner(
            constellation=constellation_qpsk,
            phase_rot_after_costas_loop=theta,
            rolloff=excess_bw,
            sps=sps,
        )
        self.my_rx_inner_0 = my_rx_inner(
            constellation=constellation_bpsk,
            phase_rot_after_costas_loop=theta,
            rolloff=excess_bw,
            sps=sps,
        )

        def _fec_position_probe():
            while True:
                val = self.probe.level()
                try:
                    self.set_fec_position(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (0.3))
        _fec_position_thread = threading.Thread(target=_fec_position_probe)
        _fec_position_thread.daemon = True
        _fec_position_thread.start()

        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=channel_noise,
        	frequency_offset=1e-4,
        	epsilon=1.001,
        	taps=(1*np.exp(1j*channel_rotation), ),
        	noise_seed=0,
        	block_tags=True
        )
        self.blocks_vector_source_x_0 = blocks.vector_source_b(np.arange(0,256), True, 1, [])
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_tag_gate_0_0 = blocks.tag_gate(gr.sizeof_char * 1, False)
        self.blocks_tag_gate_0_0.set_single_key("")
        self.blocks_stream_mux_2 = blocks.stream_mux(gr.sizeof_char*1, (data_length*is_conv,data_length*fec_choice))
        self.blocks_stream_mux_1_0 = blocks.stream_mux(gr.sizeof_char*1, (full_frame_bits_dummy, full_frame_bits_dummy))
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_char*1, (packet_counter, info_length))
        self.blocks_keep_m_in_n_1_0 = blocks.keep_m_in_n(gr.sizeof_char, full_frame_bits_dummy, full_frame_bits_dummy*2, full_frame_bits_dummy*fec_choice)
        self.blocks_keep_m_in_n_0_0 = blocks.keep_m_in_n(gr.sizeof_char, info_length, data_length, packet_counter)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_char, packet_counter, data_length, 0)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/Users/marcusbunn/Documents/engtelecom/TCC/programming/SDR/2600-0.txt', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/header_counter.txt', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/payload.txt', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.analog_const_source_x_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, port)
        self.RWN_selector_3_1_ff_0 = RWN.selector_3_1_ff(mod_choice, True)
        self.RWN_selector_3_1_cc_1 = RWN.selector_3_1_cc(mod_choice, True)
        self.RWN_selector_3_1_cc_0 = RWN.selector_3_1_cc(mod_choice, True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.RWN_selector_3_1_cc_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.RWN_selector_3_1_cc_1, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.RWN_selector_3_1_ff_0, 0), (self.rx_outer_0, 0))
        self.connect((self.RWN_selector_3_1_ff_0, 0), (self.rx_outer_0_0, 0))
        self.connect((self.analog_const_source_x_1, 0), (self.qtgui_number_sink_0_1, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.per_calc_port_select, 0))
        self.connect((self.blocks_keep_m_in_n_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_1_0, 0), (self.blocks_tag_gate_0_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.tx_outer_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.tx_outer_0_0, 0))
        self.connect((self.blocks_stream_mux_1_0, 0), (self.blocks_keep_m_in_n_1_0, 0))
        self.connect((self.blocks_stream_mux_2, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.blocks_stream_mux_2, 0), (self.blocks_keep_m_in_n_0_0, 0))
        self.connect((self.blocks_stream_mux_2, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.blocks_stream_mux_2, 0), (self.probe2, 0))
        self.connect((self.blocks_stream_mux_2, 0), (self.probe3, 0))
        self.connect((self.blocks_tag_gate_0_0, 0), (self.my_tx_inner_0, 0))
        self.connect((self.blocks_tag_gate_0_0, 0), (self.my_tx_inner_0_0, 0))
        self.connect((self.blocks_tag_gate_0_0, 0), (self.my_tx_inner_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.my_rx_inner_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.my_rx_inner_0_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.my_rx_inner_0_1, 0))
        self.connect((self.my_rx_inner_0, 1), (self.RWN_selector_3_1_cc_1, 0))
        self.connect((self.my_rx_inner_0, 0), (self.RWN_selector_3_1_ff_0, 0))
        self.connect((self.my_rx_inner_0_0, 1), (self.RWN_selector_3_1_cc_1, 1))
        self.connect((self.my_rx_inner_0_0, 0), (self.RWN_selector_3_1_ff_0, 1))
        self.connect((self.my_rx_inner_0_1, 1), (self.RWN_selector_3_1_cc_1, 2))
        self.connect((self.my_rx_inner_0_1, 0), (self.RWN_selector_3_1_ff_0, 2))
        self.connect((self.my_tx_inner_0, 0), (self.RWN_selector_3_1_cc_0, 0))
        self.connect((self.my_tx_inner_0_0, 0), (self.RWN_selector_3_1_cc_0, 1))
        self.connect((self.my_tx_inner_0_1, 0), (self.RWN_selector_3_1_cc_0, 2))
        self.connect((self.per_calc_port_select, 1), (self.probe, 0))
        self.connect((self.per_calc_port_select, 1), (self.probe4, 0))
        self.connect((self.per_calc_port_select, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.rx_outer_0, 0), (self.blocks_stream_mux_2, 0))
        self.connect((self.rx_outer_0_0, 0), (self.blocks_stream_mux_2, 1))
        self.connect((self.tx_outer_0, 0), (self.blocks_stream_mux_1_0, 0))
        self.connect((self.tx_outer_0_0, 0), (self.blocks_stream_mux_1_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block_amc")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.set_sps_float(self.samp_rate / self.symbol_rate)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sps_float(self.samp_rate / self.symbol_rate)
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_packet_counter(self):
        return self.packet_counter

    def set_packet_counter(self, packet_counter):
        self.packet_counter = packet_counter
        self.set_packet_length((self.info_length+self.packet_counter+4))
        self.set_data_length((self.info_length+self.packet_counter))
        self.blocks_keep_m_in_n_0_0.set_offset(self.packet_counter)
        self.blocks_keep_m_in_n_0.set_m(self.packet_counter)

    def get_info_length(self):
        return self.info_length

    def set_info_length(self, info_length):
        self.info_length = info_length
        self.set_packet_length((self.info_length+self.packet_counter+4))
        self.set_data_length((self.info_length+self.packet_counter))
        self.blocks_keep_m_in_n_0_0.set_m(self.info_length)

    def get_sps_float(self):
        return self.sps_float

    def set_sps_float(self, sps_float):
        self.sps_float = sps_float
        self.set_sps(int(self.sps_float))

    def get_packet_length(self):
        return self.packet_length

    def set_packet_length(self, packet_length):
        self.packet_length = packet_length
        self.set_full_frame_bits_dummy(self.packet_length*8 + len(self.access_code_dummy))
        self.rx_outer_0_0.set_packet_length(self.packet_length)
        self.rx_outer_0.set_packet_length(self.packet_length)
        self.set_full_frame_bits_conv(self.packet_length*2*8 + len(self.access_code_dummy))
        self.set_frame_bits(self.packet_length*8 + self.packet_length*8*self.fec_choice)

    def get_access_code_dummy(self):
        return self.access_code_dummy

    def set_access_code_dummy(self, access_code_dummy):
        self.access_code_dummy = access_code_dummy
        self.set_full_frame_bits_dummy(self.packet_length*8 + len(self.access_code_dummy))
        self.tx_outer_0_0.set_access_code(self.access_code_dummy)
        self.rx_outer_0_0.set_access_code(self.access_code_dummy)
        self.set_full_frame_bits_conv(self.packet_length*2*8 + len(self.access_code_dummy))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, 45*self.nfilts))
        self.my_tx_inner_0_1.set_sps(self.sps)
        self.my_tx_inner_0_0.set_sps(self.sps)
        self.my_tx_inner_0.set_sps(self.sps)
        self.my_rx_inner_0_1.set_sps(self.sps)
        self.my_rx_inner_0_0.set_sps(self.sps)
        self.my_rx_inner_0.set_sps(self.sps)

    def get_restart_call(self):
        return self.restart_call

    def set_restart_call(self, restart_call):
        self.restart_call = restart_call
        self.set_mod_choice(self.port*self.restart_call)

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port
        self.set_mod_choice(self.port*self.restart_call)
        self.analog_const_source_x_1.set_offset(self.port)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, 45*self.nfilts))

    def get_full_frame_bits_dummy(self):
        return self.full_frame_bits_dummy

    def set_full_frame_bits_dummy(self, full_frame_bits_dummy):
        self.full_frame_bits_dummy = full_frame_bits_dummy
        self.set_fec_len_menu([self.full_frame_bits_conv,self.full_frame_bits_dummy])
        self.blocks_keep_m_in_n_1_0.set_offset(self.full_frame_bits_dummy*self.fec_choice)
        self.blocks_keep_m_in_n_1_0.set_m(self.full_frame_bits_dummy)
        self.blocks_keep_m_in_n_1_0.set_n(self.full_frame_bits_dummy*2)

    def get_full_frame_bits_conv(self):
        return self.full_frame_bits_conv

    def set_full_frame_bits_conv(self, full_frame_bits_conv):
        self.full_frame_bits_conv = full_frame_bits_conv
        self.set_fec_len_menu([self.full_frame_bits_conv,self.full_frame_bits_dummy])

    def get_fec_choice(self):
        return self.fec_choice

    def set_fec_choice(self, fec_choice):
        self.fec_choice = fec_choice
        self.set_is_conv(self.fec_choice == 0)
        self._fec_choice_callback(self.fec_choice)
        self.set_frame_bits(self.packet_length*8 + self.packet_length*8*self.fec_choice)
        self.blocks_keep_m_in_n_1_0.set_offset(self.full_frame_bits_dummy*self.fec_choice)

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, 45*self.nfilts))
        self.my_tx_inner_0_1.set_rolloff(self.excess_bw)
        self.my_tx_inner_0_0.set_rolloff(self.excess_bw)
        self.my_tx_inner_0.set_rolloff(self.excess_bw)
        self.my_rx_inner_0_1.set_rolloff(self.excess_bw)
        self.my_rx_inner_0_0.set_rolloff(self.excess_bw)
        self.my_rx_inner_0.set_rolloff(self.excess_bw)

    def get_theta(self):
        return self.theta

    def set_theta(self, theta):
        self.theta = theta
        self.my_rx_inner_0_1.set_phase_rot_after_costas_loop(self.theta)
        self.my_rx_inner_0_0.set_phase_rot_after_costas_loop(self.theta)
        self.my_rx_inner_0.set_phase_rot_after_costas_loop(self.theta)

    def get_sdr_rate(self):
        return self.sdr_rate

    def set_sdr_rate(self, sdr_rate):
        self.sdr_rate = sdr_rate

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_restart_check(self):
        return self.restart_check

    def set_restart_check(self, restart_check):
        self.restart_check = restart_check

    def get_restart(self):
        return self.restart

    def set_restart(self, restart):
        self.restart = restart

    def get_mod_choice(self):
        return self.mod_choice

    def set_mod_choice(self, mod_choice):
        self.mod_choice = mod_choice
        self._mod_choice_callback(self.mod_choice)
        self.RWN_selector_3_1_ff_0.set_selected(self.mod_choice)
        self.RWN_selector_3_1_cc_1.set_selected(self.mod_choice)
        self.RWN_selector_3_1_cc_0.set_selected(self.mod_choice)

    def get_len_tag_name_rx(self):
        return self.len_tag_name_rx

    def set_len_tag_name_rx(self, len_tag_name_rx):
        self.len_tag_name_rx = len_tag_name_rx
        self.rx_outer_0_0.set_len_tag_name_rx(self.len_tag_name_rx)
        self.rx_outer_0.set_len_tag_name_rx(self.len_tag_name_rx)

    def get_len_tag_name(self):
        return self.len_tag_name

    def set_len_tag_name(self, len_tag_name):
        self.len_tag_name = len_tag_name
        self.tx_outer_0_0.set_len_tag_name(self.len_tag_name)
        self.tx_outer_0.set_len_tag_name(self.len_tag_name)

    def get_is_conv(self):
        return self.is_conv

    def set_is_conv(self, is_conv):
        self.is_conv = is_conv

    def get_frame_bits(self):
        return self.frame_bits

    def set_frame_bits(self, frame_bits):
        self.frame_bits = frame_bits

    def get_fec_position(self):
        return self.fec_position

    def set_fec_position(self, fec_position):
        self.fec_position = fec_position

    def get_fec_options(self):
        return self.fec_options

    def set_fec_options(self, fec_options):
        self.fec_options = fec_options

    def get_fec_len_menu(self):
        return self.fec_len_menu

    def set_fec_len_menu(self, fec_len_menu):
        self.fec_len_menu = fec_len_menu

    def get_data_length(self):
        return self.data_length

    def set_data_length(self, data_length):
        self.data_length = data_length
        self.tx_outer_0_0.set_data_length(self.data_length)
        self.tx_outer_0.set_data_length(self.data_length)
        self.blocks_keep_m_in_n_0_0.set_n(self.data_length)
        self.blocks_keep_m_in_n_0.set_n(self.data_length)

    def get_constellation_qpsk(self):
        return self.constellation_qpsk

    def set_constellation_qpsk(self, constellation_qpsk):
        self.constellation_qpsk = constellation_qpsk
        self.my_tx_inner_0_0.set_constellation(self.constellation_qpsk)
        self.my_rx_inner_0_0.set_constellation(self.constellation_qpsk)

    def get_constellation_bpsk(self):
        return self.constellation_bpsk

    def set_constellation_bpsk(self, constellation_bpsk):
        self.constellation_bpsk = constellation_bpsk
        self.my_tx_inner_0.set_constellation(self.constellation_bpsk)
        self.my_rx_inner_0.set_constellation(self.constellation_bpsk)

    def get_constellation_8psk(self):
        return self.constellation_8psk

    def set_constellation_8psk(self, constellation_8psk):
        self.constellation_8psk = constellation_8psk
        self.my_tx_inner_0_1.set_constellation(self.constellation_8psk)
        self.my_rx_inner_0_1.set_constellation(self.constellation_8psk)

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

    def get_access_code_conv(self):
        return self.access_code_conv

    def set_access_code_conv(self, access_code_conv):
        self.access_code_conv = access_code_conv
        self.tx_outer_0.set_access_code(self.access_code_conv)
        self.rx_outer_0.set_access_code(self.access_code_conv)

    def get_DE(self):
        return self.DE

    def set_DE(self, DE):
        self.DE = DE
        self.tx_outer_0_0.set_encoder(self.DE)
        self.tx_outer_0.set_encoder(self.DE)

    def get_DD(self):
        return self.DD

    def set_DD(self, DD):
        self.DD = DD
        self.rx_outer_0_0.set_decoder(self.DD)
        self.rx_outer_0.set_decoder(self.DD)

    def get_CE(self):
        return self.CE

    def set_CE(self, CE):
        self.CE = CE

    def get_CD(self):
        return self.CD

    def set_CD(self, CD):
        self.CD = CD


def main(top_block_cls=top_block_amc, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

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
