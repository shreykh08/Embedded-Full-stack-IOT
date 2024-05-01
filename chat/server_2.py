import socket
import sys
import threading

#server credentials 
IP = socket.gethostbyname(socket.gethostname())
PORT = 54322

#global varibales
BUFFER = 1024
FORMAT = 'UTF-8'
client_list = []
name_list = []


try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((IP,PORT))
    s.listen()
    print(f" Server is listening for the clients at {IP} : {PORT}")

except socket.error as e:
    print(f"Error in socket creation : {e}")
    sys.exit()

def broadcast(msg):
    for c in client_list:
        c.send(msg.encode(FORMAT))

def client_handle(conn):
    while True:
        try:
            msg = conn.recv(BUFFER).decode(FORMAT) #Received the message from the client
            broadcast(msg) #we broadcsted id to all the clients rather than printing it for the privacy concerns.

            """if any client producesa ny error remove it from the chatroom.
            Now we need to remove the socket and username as well from the list before closig the handle."""
        
        except:
            index = client_list(conn)
            client_list.remove(conn)
            user = name_list(index)
            broadcast(f"{user} has left the chat ")
            name_list.remove(user)
            break #Handle is closed now a we comeout of the while loop.

while True:
    try:

        conn, addr = s.accept()  #we are accepting the connection request by the client
        print(f"{addr} Successfully connected with the server 👍:) ") #once the client is connected it will give its address.

        conn.send("uname".encode(FORMAT)) #we sent a keyword to ask the user_name of the client
    
        #we will take the username of the client.
        uname = conn.recv(BUFFER).decode(FORMAT)
    


        """Now to send the messages to everyone we need to save the sockets of the different clients 
           So we create a list and save the sockets of every client """
             
        client_list.append(conn)
        name_list.append(uname) #saved all the usernames of the clients.
       

        # FEATURE : (not necessary) whenever a new user joins,it notifies everyone so we broadcast this.
        broadcast(f" {uname} joined the chat")

        #taiyariyan poori ho gayi
        #now create a client thread.This will be responsible for the next steps.

        client_thread = threading.Thread(target = client_handle , args = (conn,))#earlier we used to give the socket and the address but now only one parameter because we will recognise the user with their username.We are  not giving the second parameter so we have to give null.

        client_thread.start()
        # active_connections = threading.activeCount()-1 # gives the active count of the users 


    except Exception as e:
        print(f" Error in creating thread : {e}")
        break

    #Now if we need to deliberately close the server then
    except KeyboardInterrupt:
        print("Server is closed")


    