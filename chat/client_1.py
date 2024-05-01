import socket
import sys
import threading

#server credentials
IP = '10.10.145.232'#socket.gethostbyname(socket.gethostname())
PORT = 54321

#global variables
BUFFER = 1024
FORMAT = 'UTF-8'

username = input("Enter your user name : ")


try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((IP,PORT))
    print(f" connected with the server... ")
    
    """In this as we are talking about the connection oriented sockets 
    So we directly connect the socket with the server ip and the server port instead of binding it."""
except socket.error as e:
    print(f"Error in creation socket {e}")
    sys.exit()




def send_data():
    while True:
        try:
            msg = f"{username} >> {input('')}"
            s.send(msg.encode(FORMAT))
            #s.send(f" {usernamename} : {input()}".encode(FORMAT)) : if you want to write in one line.

        except Exception as e:
            print(f"Error in sending message.🙁 {e}")
            s.close()
            break

    sys.exit()


def recv_data():
    while True:
        try:
            msg = s.recv(BUFFER).decode(FORMAT)
            print(msg)
            # we will get two messages one from the client and the other from the server.

            if msg == 'uname':
                s.send(username.encode(FORMAT))

            else:
                print(msg)
            

        except Exception as e:
            print(f"Error in receiving message {e}")
            s.close()
            break

    sys.exit()

        




# lets create a threadd now for sending and receiving data

threading.Thread(target = send_data).start() #directly created a thread
threading.Thread(target = recv_data).start()













