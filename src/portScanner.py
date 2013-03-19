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

outputTimeoutFile = ''
commonOpenPorts = [4, 20, 21, 22, 23, 25, 37, 53, 80, 81, 110, 111, 113, 135, 139, 143, 389, 443, 445, 554, 587, 1002, 1024, 1025, 1026, 1027, 1028, 1029, 1050, 1723, 1863, 3389, 4444, 4567, 4664, 5000, 5678, 7676, 8000, 8080, 8081, 8594, 10000, 18067, 27374, 28960, 30005, 30722, 56789, 62483]

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

			boom = int(threading.activeCount()/((connections+1)/2)*2)
			t = threading.Timer(boom,attempt, args=(host, port,timeout, outputFile))

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


def attempt(host, port, timeout, outputFile, secondCall = False):
	try:
		tn = Telnet(host,port,timeout)
		tn.open(host,port,timeout)
		header = tn.read_some()
		tn.close()
		print "[!] Port %d seems to be open on %s" %(port,host)
		file = open(outputFile, 'a') #writes to file
		file.write("%s:%d"%(host,port))
		if header != "":
			file.write(" - %s"%(header))
		file.write("\n")
		file.close()
	except Exception, e:
		try:
			e[1]
			code, reason = e.args
			print "[ERROR] %s on %s:%d (%d)" %(reason,host,port,code)
		except IndexError:
			if e.args[0] == "timed out" and port in commonOpenPorts:
				if secondCall is False:
					print "[!] extending timeout on common port (%d)" %(port)
					return attempt(host, port, (timeout*2), outputFile, True)
			
			#only write timeouts to the file
			if e.args[0] == "timed out":
				file = open(outputTimeoutFile, 'a') #writes to file
				file.write("%s:%d"%(host,port))
				
				file.write("\n")
				file.close()
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

	outputTimeoutFile = "%s_ports_timeout.txt" %(args.host)

	try:
		main(args.host, int(args.portFrom), int(args.portTo),int(args.timeout), int(args.connections), str(args.output))
	except (KeyboardInterrupt, SystemExit):
		print "\nStopped\n"