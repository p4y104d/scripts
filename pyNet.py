#!/usr/bin/env python
# -*- coding: ascii -*-
import sys,os
from scapy.all import *
import optparse

def get():
    parser = optparse.OptionParser('usa:python p4yNet.py -S <IP spoof> -T <IP Target> -P <payload>')
    parser.add_option('-S', dest='srcHost', type='string', help='Specific IP spoof')
    parser.add_option('-T', dest='tgtHost', type='string', help='Specific IP Target')
    parser.add_option('-P', dest='pyl', type='string', help='Specific the message')
    (options, args) = parser.parse_args()
    source = options.srcHost
    target = options.tgtHost
    pay = options.pyl
    if source == None or target == None or pay == None:
        print(parser.usage)
	exit(0)
    else:
    	print "| La IP spoof es: ", source + "| La IP target es: ", target + "| El mensaje es: ", pay
	
	packet = IP(src=source,dst=target)/ICMP()/pay

	send(packet)
	hexdump(packet)
      	exit(0)


def main():
    get()
    
main()
