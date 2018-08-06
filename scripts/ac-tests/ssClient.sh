#!/bin/bash

FILEINDEX=$1

#Client procedures
sslocal -c $HOME/anon-apps/Shadowsocks/shadowsocksClient.json &> /dev/null &
mv /etc/proxychains.conf /etc/proxychains.conf.old
mv /etc/proxychains-shadowsocks.conf /etc/proxychains.conf
proxychains $HOME/class-testing/scripts/trafficGenClient.py $FILEINDEX

#Cleanup
mv /etc/proxychains.conf /etc/proxychains-shadowsocks.conf
mv /etc/proxychains.conf.old /etc/proxychains.conf
killall sslocal
