#!/bin/bash

FILEINDEX=$1

#Server procedures
ssserver -c $HOME/anon-apps/Shadowsocks/shadowsocksServer.json &> /dev/null &
$HOME/class-testing/scripts/trafficGenServer.py $FILEINDEX

#Cleanup
killall ssserver
