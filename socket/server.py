
##############################
##### PYTHON NETWORKING ######
##############################

import socket
import sys

def create_socket():
    try:
        global a
        a = [30, 40, 50, 60, 70, 80, 90, 100, 110]
        global host
        global port 
        global s
        host = ""
        port = 5050 # not use it
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("socket error" + str(msg))
#########################################
# binding the socket with listening and connection
'''
is it enough to connect computer with socket? NO
Why do need bindto a host & port with socket?
it might be able to open line of communication with socket,
but it's really need to know about info about computer or device
it is supposed to communicating with

'''
def bind_socket():
    try:
        global host
        global port 
        global s
        
        print("Binding the port   " , (port))
        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("socket binding error"+ str(msg)+"\n"+"retrying...")
        bind_socket()

################################

# Established connection with client(socket must be listening)
#accept connection
def socket_accept():
    conn, addr = s.accept() #(object of connection,list Ip to a port)
    print("connectin has been established  "+ " | IP | "+ addr[0]+" | port | "+str(addr[1]))
    send_command(conn) 

#############################################

# Send command to client/victim or friend

def send_command(conn):
    while True:
        print("The number of packets sent is: {} \n" .format(str(len(a))))
        
        y = []
        for i in range(len(a)):
          
            print(a[i])
            y+=[a[i]]
            z = (str(y))
            
            z=(z.encode())
        conn.send(bytearray(z))

        conn.close()
        sys.exit()

    
###############################################

if __name__ == '__main__' :
    create_socket()
    bind_socket()
    socket_accept()