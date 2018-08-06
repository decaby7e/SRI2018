#!/bin/bash


TCPPORT="$1"
PCAPNAME="$2"

tshark -i s1-eth1 -P -w $PCAPNAME.pcap -F pcap -f "tcp port $TCPPORT"
