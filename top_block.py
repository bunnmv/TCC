#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Mar 28 11:42:18 2018
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
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import pmt
import split_pack_block
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
        self.infoLength = infoLength = 22
        self.payloadLength = payloadLength = infoLength+packetCounterLength
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.frameLength = frameLength = int(payloadLength+12)
        self.snr = snr = 0
        self.samp_rate = samp_rate = 32000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 45*nfilts)
        self.order_costas = order_costas = 8
        self.excess_bw = excess_bw = 0.35

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
        self.split_pack_block = split_pack_block.blk(counter_length=packetCounterLength, payload_length=infoLength)
        self.fec_extended_tagged_encoder_0 = fec.extended_tagged_encoder(encoder_obj_list=CE, puncpat='11', lentagname='len_key', mtu=payloadLength)
        self.fec_extended_tagged_decoder_0 = self.fec_extended_tagged_decoder_0 = fec_extended_tagged_decoder_0 = fec.extended_tagged_decoder(decoder_obj_list=CD, ann=None, puncpat='11', integration_period=10000, lentagname='len_key2', mtu=payloadLength)
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, 'len_key')
        self.digital_pfb_clock_sync_xxx_0_0 = digital.pfb_clock_sync_ccf(sps, 6.82/100, (rrc_taps), nfilts, nfilts/2, 1.5, 1)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(6.82/100, order_costas, False)
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_ff_ts(digital.packet_utils.default_access_code,
          0, 'len_key2')
        self.digital_constellation_soft_decoder_cf_0 = digital.constellation_soft_decoder_cf(MO)
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=MO,
          differential=False,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.35,
          verbose=True,
          log=False,
          )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=snr,
        	frequency_offset=1e-4,
        	epsilon=1.001,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_vector_source_x_0 = blocks.vector_source_b(numpy.arange(65, 91,1), True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'len_key', 0)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, payloadLength, "len_key")
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_char*1, (packetCounterLength, infoLength))
        self.blocks_repack_bits_bb_0_0_0_0_0_0 = blocks.repack_bits_bb(1, 8, 'len_key', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0_0 = blocks.repack_bits_bb(8, 1, 'len_key', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(1, 8, 'len_key2', False, gr.GR_MSB_FIRST)
        self.blocks_head_0 = blocks.head(gr.sizeof_char*1, 1000)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/sender.txt', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/test2.txt', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(True)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/Users/marcusbunn/Desktop/test.txt', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.split_pack_block, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0, 0), (self.fec_extended_tagged_encoder_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0_0_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0_0_0, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_repack_bits_bb_0_0_0_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.digital_pfb_clock_sync_xxx_0_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.digital_constellation_soft_decoder_cf_0, 0), (self.digital_correlate_access_code_xx_ts_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.fec_extended_tagged_decoder_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_constellation_soft_decoder_cf_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.fec_extended_tagged_decoder_0, 0), (self.blocks_repack_bits_bb_0_0_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0, 0), (self.blocks_repack_bits_bb_0_0_0_0_0_0, 0))
        self.connect((self.split_pack_block, 1), (self.blocks_file_sink_0_0, 0))
        self.connect((self.split_pack_block, 0), (self.blocks_file_sink_0_0_0, 0))

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
        self.set_payloadLength(self.infoLength+self.packetCounterLength)
        self.split_pack_block.counter_length = self.packetCounterLength

    def get_infoLength(self):
        return self.infoLength

    def set_infoLength(self, infoLength):
        self.infoLength = infoLength
        self.set_payloadLength(self.infoLength+self.packetCounterLength)
        self.split_pack_block.payload_length = self.infoLength

    def get_payloadLength(self):
        return self.payloadLength

    def set_payloadLength(self, payloadLength):
        self.payloadLength = payloadLength
        self.set_frameLength(int(self.payloadLength+12))
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.payloadLength)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.payloadLength)

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

    def get_frameLength(self):
        return self.frameLength

    def set_frameLength(self, frameLength):
        self.frameLength = frameLength

    def get_snr(self):
        return self.snr

    def set_snr(self, snr):
        self.snr = snr
        self.channels_channel_model_0.set_noise_voltage(self.snr)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0_0.update_taps((self.rrc_taps))

    def get_order_costas(self):
        return self.order_costas

    def set_order_costas(self, order_costas):
        self.order_costas = order_costas

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

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
