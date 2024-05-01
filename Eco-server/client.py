import socket
import sys

HOST = '10.10.144.253'#socket.gethostbyname(socket.gethostname())
#you can also write your ip instead HOST

PORT = 45

BUFFER = 1024
FORMAT = 'UTF-8'

#funtion to create socket and communicate with the server

def create_socket():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((HOST,PORT))
        print(f"Hehe,Connection established")
        return s
        """In this as we are talking about the connection oriented sockets so we directly connect the socket with the server ip and the server port instead of binding it."""
    except socket.error as e:
        print(f"Error in creation socket {e}")
        sys.exit()

    except KeyboardInterrupt:
        print("Keyboard INterrupt")
        sys.exit()



def send_receiveToServer(s):
    while True:
        try:
            s.send(input(">>Chalo yrr likh do kuch....").encode(FORMAT))
            msg = s.recv(BUFFER)
            if not msg:
                print("No message form the client")
                break
            print(msg.decode(FORMAT))
                   
        except socket.error as e:
            print(f"Error in creation socket {e}")
            sys.exit()

        except KeyboardInterrupt:
            print("Keyboard INterrupt")
            sys.exit()

if __name__ == "__main__":
    s = create_socket()
    send_receiveToServer(s)


    """
    -> Problem that we faces it that our server used to listen only one client at a time
    -> To solve this we will be usig the multi-threading concept.
    -> We'll feel that the threads are being executing parallely but actually true concurrency is not posssible.
    -> Switching takes place too faster that you are not able to recognise it that you had to wait for it.
    """
