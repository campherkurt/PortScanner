# PortScanner

Basic PortScanner written in python, supports multiple connections.
Uses telnet to try and connect to each port. 
Writes all ports found to a text file.

### Useage 

	> ./portScanner.py -h
	usage: telnet.py [-h] [-s HOST] [-f PORTFROM] [-t PORTTO] [-i TIMEOUT]
	                 [-c CONNECTIONS] [-o OUTPUT]

	Telnet port scanner

	optional arguments:
	  -h, --help            show this help message and exit
	  -s HOST, --source HOST
	                        Host to scan, default localhost
	  -f PORTFROM, --from PORTFROM
	                        Port to start scanning at, default 1
	  -t PORTTO, --to PORTTO
	                        Port to stop scanning at, default 10000
	  -i TIMEOUT, --timeout TIMEOUT
	                        Timeout in seconds, default 30 seconds
	  -c CONNECTIONS, --connections CONNECTIONS
	                        Concurrent connections, default 5
	  -o OUTPUT, --output OUTPUT
	                        Output file name, where source open ports gets saved

### Example
Scanning localhost from port 78-81

	> ./portScanner.py -s "localhost" -f 78 -t 81
	Starting

	[ERROR] Connection refused on localhost:78 (61)
	[ERROR] Connection refused on localhost:79 (61)
	[!] Port 80 seems to be open on localhost
	[ERROR] Connection refused on localhost:81 (61)


### DISCLAIMER:

This program is for educational use only.
Don't use it to crack a real server. You could get
into a lot of trouble. This is just a simple demo
to show how to use telnetlib in combination with files.
Use it at your own risk!

### License
MIT-License:

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
