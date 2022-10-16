# Socket in Python
<img src = 'https://tse3.mm.bing.net/th?id=OIP.dVpjkNOQoBjANryFKbNQuwAAAA&pid=Api&P=0'> 

## SOCKET
Sockets act as bidirectional communications channel where they are endpoints of it.sockets may communicate within the process, between different process and also process on different places.
- s = socket.socket((socket.AF_INET, socket.SOCK_STREAM))
- socket.AF_INET(IP4) , socket.SOCK_STREAM (use TCP/IP)

## Server socket methods
	
- s.bind – This method binds address hostname, port number to socket	
- s.listen – This method setups and start TCP listener	
- s.accept – This passively accepts client connection, waiting until connection arrives blocking

## Client socket methods

- s.connect – This method actively initiates TCP server connection

## General socket methods 	
Data must be in string  (encode and decode method use in it)
- s.recv – This method receives TCP message	
- s.send – This method transmits TCP message
- s.close – This method closes socket	
- s.gethostname – Returns a hostname