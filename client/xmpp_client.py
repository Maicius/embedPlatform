#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import time
import datetime
import logging

import getpass
import argparse

import serial
import sleekxmpp

from embed_nju.util.jedis import pop_raw_data
from embed_nju.util.constant import RAW_LIGHT_KEY


class SendMsgBot(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password, recipient):
        super().__init__(jid, password)

        self.recipient = recipient
        self.add_event_handler('session_start', self.start)

    def start(self, event):
        self.send_presence()
        self.get_roster()

        # 读取光线数据
        while True:
            light = pop_raw_data(RAW_LIGHT_KEY)
            self.send_message(mto=self.recipient,
                              mbody=light,
                              mtype='chat')

        self.disconnect(wait=True)


def start_xmpp_client():
    xmpp = SendMsgBot('romeo@nju-forum.top', '1234', 'juliet@nju-forum.top')
    xmpp.register_plugin('xep_0030')  # Service Discovery
    xmpp.register_plugin('xep_0199')  # XMPP Ping

    if xmpp.connect():
        xmpp.process(block=True)
        print('Done.')
    else:
        print('Unable to connect.')


if __name__ == '__main__':

    # Setup the command line arguments.
    parser = argparse.ArgumentParser(description="XMPP Bot")

    # Output verbosity options.
    parser.add_argument('-q', '--quiet', help='set logging to ERROR',
                        action='store_const', dest='loglevel',
                        const=logging.ERROR, default=logging.INFO)

    parser.add_argument('-d', '--debug', help='set logging to DEBUG',
                        action='store_const', dest='loglevel',
                        const=logging.DEBUG, default=logging.INFO)

    parser.add_argument('-v', '--verbose', help='set logging to COMM',
                        action='store_const', dest='loglevel',
                        const=5, default=logging.INFO)

    # JID and password options.
    parser.add_argument("-j", "--jid", dest="jid",
                        help="JID to use")
    parser.add_argument("-p", "--password", dest="password",
                        help="password to use")
    parser.add_argument("-t", "--to", dest="to",
                        help="JID to send the message to")

    args = parser.parse_args()

    # Setup logging.
    logging.basicConfig(level=args.loglevel,
                        format='%(levelname)-8s %(message)s')

    if args.jid is None:
        args.jid = input("Username: ")
    if args.password is None:
        args.password = getpass.getpass("Password: ")
    if args.to is None:
        args.to = input("Send To: ")

    xmpp = SendMsgBot(args.jid, args.password, args.to)
    xmpp.register_plugin('xep_0030')  # Service Discovery
    xmpp.register_plugin('xep_0199')  # XMPP Ping

    if xmpp.connect():
        xmpp.process(block=True)
        print('Done.')
    else:
        print('Unable to connect.')
