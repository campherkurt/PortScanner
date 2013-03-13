#!/usr/bin/env python
'''
DISCLAIMER: This program is for educational use only.
Don't use it to crack a real server. You could get
into a lot of trouble. This is just a simple demo
to show how to use telnetlib in combination with files.
Use it at your own risk!
'''
import os
import argparse
import threading
from sys import exit
from telnetlib import Telnet

def main(host, portFrom, portTo, timeout, connections, outputFile = 'ports_open.txt'):
	""" Reads the dictionary and attempts to connect with the username and password on each line

	Keyword arguments:
	host -- Host to scan for open ports
	portFrom -- Port number to scan from (default 1)
	portTo -- Port number to scan to (default 10000)
	timeout -- Timeout in seconds (default 30)
	outputFile -- Output filename to write open ports found to
	"""
	print "Starting\n"
	portTo += 1
	for port in range(portFrom,portTo):
		try:
			#make sure we only create connections when we have theads available
			#print threading.activeCount()
			while threading.activeCount() > connections:
				t.join(1)

			t = threading.Timer(int(threading.activeCount()/(connections/2)),attempt, args=(host, port,timeout, outputFile))

			t.start()
		except Exception, e:
			try:
				e[1]
				code, reason = e.args
				print "[ERROR] %s (%d)" %(reason,code)
			except IndexError:
				print "[ERROR] %s " %(e.args[0])
			except (KeyboardInterrupt, SystemExit):
				t.cancel()
				exit(0)


def attempt(host, port, timeout, outputFile):
	try:
		tn = Telnet(host,port,timeout)
		tn.open(host,port,timeout)
		tn.close()
		print "[!] Port %d seems to be open on %s" %(port,host)
		file = open(outputFile, 'a') #writes to file
		file.write("%s:%d \n"%(host,port))
		file.close()
	except Exception, e:
		try:
			e[1]
			code, reason = e.args
			print "[ERROR] %s on %s:%d (%d)" %(reason,host,port,code)
		except IndexError:
			print "[ERROR] %s on %s:%d " %(e.args[0],host,port)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Telnet port scanner')
	parser.add_argument('-s','--source', dest='host', action='store',default='localhost', help='Host to scan, default localhost')
	parser.add_argument('-f','--from', dest='portFrom', action='store',default=1, help='Port to start scanning at, default 1')
	parser.add_argument('-t','--to', dest='portTo', action='store',default=10000, help='Port to stop scanning at, default 10000')
	parser.add_argument('-i','--timeout', dest='timeout', action='store',default=30, help='Timeout in seconds, default 30 seconds')
	parser.add_argument('-c','--connections', dest='connections', action='store',default=5, help='Concurrent connections, default 5')
	parser.add_argument('-o','--output', dest='output', action='store',default=None, help='Output file name, where source open ports gets saved')
	args = parser.parse_args()

	if args.output is None:
		args.output = "%s_ports_open.txt" %(args.host)

	try:
		main(args.host, int(args.portFrom), int(args.portTo),int(args.timeout), int(args.connections), str(args.output))
	except (KeyboardInterrupt, SystemExit):
		print "\nStopped\n"