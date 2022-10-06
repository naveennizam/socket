
import socket
from colorama import Fore  , Style #pip install colorama

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname() 
port = 5050
s.connect((host,port))



data = s.recv(1024)
we=(data.decode(('utf-8')))

res = we.strip('][,').split(',')
print("The number of packets recieved is: {} \n"  .format(str(len(res))))

([list((i,res[i])) for i in range(len(res))])# to make list with index & value
for i in range(len(res)):
    print(res[i])

pre = res[5] 
k = 5
res[k] = -1

for j in range(len(res)):
             
    print("Received frame is: " , res[j])
    

for j in range(len(res)):               

    if (res[j] == -1): 
        print("Request to retransmit packet no " , (j+1) , " again!!")
        print()    
        print(Fore.YELLOW,"Received frame is: " , pre)
        print(Style.RESET_ALL)
       
print("quit, System close!")


