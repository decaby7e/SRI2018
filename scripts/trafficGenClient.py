#!/usr/bin/python

import socket, csv, time, random, sys

###Variables###

#Network Variables
s = socket.socket()
# host = '10.0.0.1' Changed for SSH testing w/ lab computer
host = '192.168.122.1'
# port = 5161 Changed for SSH testing w/ lab computer
port = 9090

#File Variables
startPos = sys.argv[1] #File position; entered as first parameter

###Testing Operations###

#Connect to the server
s.connect((host, port))

#Client
filename = str('data/output_' + str(startPos) + '.csv')
print 'STATUS: Currently on file', filename

with open(filename) as f:
	readCSV = csv.reader(f, delimiter=',')

	rowCount = 0
	for row in readCSV:
		print 'STATUS: Currently on row ', rowCount
		print 'NETWORK: Sent', s.send(row[5])
		time.sleep(random.uniform(0.01,0.1))
		print 'NETWORK: Recevied', s.recv(1024)
		rowCount=rowCount + 1
	s.close
