import socket
import sys  #if anything wrong happens then it would be helpful to terminate the code hence imported
import threading
IP=socket.gethostbyname(socket.gethostname())
port=54322
buffer=1024
format='utf-8'
client_list=[]
name_list=[]
def broadcast(msg):
    for c in client_list:
        c.send(msg.encode(format))

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((IP,port))#ip, port is passed as a tuple
           
    s.listen()
    print(f"Server is listening for sockets at {IP}: {port}")
except socket.error as e:
    print(f"Error in creation of socket {e}")
    sys.exit()
        
def client_handle(conn):
    while True:
        try:
            msg=conn.recv(buffer).decode(format)
            #to recieve the msg
            broadcast(msg)
        except:
            index=client_list(index) #it will tell the connection index in the connection list and hence it would be the same for the name index
            client_list.remove(conn)#remove the connection from the client_list
            user_name=name_list(index)
            broadcast(f"{user_name} has left the chat")
            #we have to broadcast that the particular user has left the meeting or the chat room
            name_list.remove(user_name)
            #remove the user from the name list
            break
            
            
while True:
    try:
        conn,addr=s.accept()
        print(f"{addr} connected with server")
        conn.send("uname".encode(format))   #connection, which will send the data to the other part
        uname=conn.recv(buffer).decode(format)
        
        client_list.append(conn)  #this line would give an error as it does not know which type of the data would come to it, so we declare this variable above
        name_list.append(uname)  #to append the user name in the name _list
        broadcast(f"{uname} joined the chat")  #broadcast is not an builtin function we have to define it, used to broadcast the msg to all
        
        client_thread=threading.Thread(target=client_handle,args=(conn,))  #conn is socket which we provide, left with comma as it would pass a null arg.
        #thread created with the above given function
        active_connections=threading.active_count()-1  
        #active count function is used to count the number of active user on the network
    except Exception as e:
        print(f" Error in creating thread {e}")
    except KeyboardInterrupt as e:
        print("Server is closed")
        break