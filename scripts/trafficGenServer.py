#!/usr/bin/python

import socket, csv, time, random, sys

###Variables###

#Network Variables
s = socket.socket()
host = '192.168.122.208'
port = 5161

#File Variables
startPos = sys.argv[1] #File position; entered as first parameter

###Testing Operations###

#Bind IP/Port to socket
s.bind((host, port))

#Listen for connections
s.listen(5)
c, addr = s.accept()
print 'NETWORK: Got connection from', addr

#Server
filename = str('data/output_' + str(startPos) + '.csv')
print 'STATUS: Currently on file', filename

with open(filename) as f:
	readCSV = csv.reader(f, delimiter=',')
	
	rowCount = 0
	for row in readCSV:
		print 'STATUS: Currently on row ', rowCount
		print 'NETWORK: Sent', c.send(row[5])
		time.sleep(random.uniform(0.01, 0.1))
		print 'NETWORK: Recevied', c.recv(1024)
		rowCount=rowCount + 1
	c.close()
