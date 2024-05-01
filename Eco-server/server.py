import socket
import sys

HOST = socket.gethostbyname(socket.gethostname())
#you can also write your ip instead HOST

PORT = 554
#you have 64,536 ports available in your laptop
#port 22 - SSH
#port 25 - TELNET
#port 80 - Web Applications

BUFFER = 1024
FORMAT = 'UTF-8'#we are using this format for encoding and decoding.It converts the string data to bytes and bytes to string format.

#funtion to create socket and listen to the clients
def create_socket():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        """normally we give three parametes 
        In this two parameters are passed the first one tells the family of the socket i.e. IPV4 or IPV6.
        AF_INET : This address family provides interprocess communication between processes that run on the same system 
                or on different systems.
        SOCK_STREAM tells the type of the socket also known as extreme socket i.e. The TCP socket.
        if we have to use use udp soclet we use SOCK_DATAGRAM """

        s.bind((HOST,PORT))
        """when we bind we pass tuple into it as it is immutable and stablises the ip address.
        As we cannot change the ip address in between and where we cannot restart we use the concept of static ip"""
        s.listen()
        """Now Server starts listening the clients.At a time it will listen to only one client as connection oriented.We can also 
        pass how many people will wait in the queue to be listened."""

        """while communication we use socket of the client"""

        print(f"Server is listening to clients ko at {HOST}:{PORT}")
        return s

    except socket.error as e:
        print(f"Error in creation socket {e}")
        sys.exit()

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        sys.exit()

    """Error logging - Whenever our program crashesa / terminates at any point we can save our progress and the exception into a file."""

def handle_client(s):
    while True:
        try:
            client , addr = s.accept() 
            """when your server accepts the client request it'll give you two things client address and socket of client """
            print(f"Client connected from {addr[0]}:{addr[1]}")
            while 1:
                msg = client.recv(BUFFER)
                """when we receive we have a BUFFER limit as initialised above.RECV is a blocking API.
                Data is in the form of bytes on the network and we read in string format so we need to encode it"""

                """Encode method converts the given data into bytes before transferring it to the network as the data on the network is in bytes form."""
                
                if not msg:
                    print("No message form the client")
                    break
                print(msg.decode(FORMAT))
                client.send(msg)
        
        except socket.error as e:
            print(f"Error in creation socket {e}")
            sys.exit()

        except KeyboardInterrupt:
            print("Keyboard INterrupt")
            sys.exit()

if __name__ == "__main__":
    s = create_socket()
    handle_client(s)
