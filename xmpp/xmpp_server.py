#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import getpass

import argparse

import sleekxmpp

import redis_lib


class EchoBot(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password):
        super().__init__(jid, password)
        self.add_event_handler('session_start', self.start)
        self.add_event_handler('message', self.message)

    def start(self, event):
        self.send_presence()
        self.get_roster()

    def message(self, msg):
        # if msg['type'] in ('normal', 'chat'):
        #     msg.reply("Thanks for sending:\n%(body)s" % msg).send()
        # 这里写对信息的处理操作

        redis_lib.save_data('embed_sample', msg['body'])


if __name__ == '__main__':

    # Setup the command line arguments.
    parser = argparse.ArgumentParser(description='XMPP Service')

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

    args = parser.parse_args()

    # Setup logging.
    logging.basicConfig(level=args.loglevel,
                        format='%(levelname)-8s %(message)s')

    if args.jid is None:
        args.jid = input("Username: ")
    if args.password is None:
        args.password = getpass.getpass("Password: ")

    xmpp = EchoBot(args.jid, args.password)
    xmpp.register_plugin('xep_0030')  # Service Discovery
    xmpp.register_plugin('xep_0004')  # Data Forms
    xmpp.register_plugin('xep_0060')  # PubSub
    xmpp.register_plugin('xep_0199')  # XMPP Ping

    if xmpp.connect():
        xmpp.process(block=True)
        print('Done.')
    else:
        print('Unable to connect.')
