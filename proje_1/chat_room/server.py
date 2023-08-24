#server=>is a computer that serve other computers
#the server is a holder of content
# request=>Server=>response computer

#Client=>Client is a computer that request for the services from the Server through a Network


#Server vs client
#=>In most cases clients are normal computers,tablets,phones etc
#=>Relatively smaller and cheaper than the server

#TCP and UDP 
#=>TCP and UDP are protocols used for sending packets over the internet
#TCP stans for transformission control Protocol
#UDP stands for User Datagram Protocol

#TCP is slow because of Secure Network

#Faster Communication and Security is not important=> User Datagram Protocol (UDP)


"""In UDP,Sequence of packets is managed by the application layer,UDP is unreliable"""



#Socket=>Socket is a method of communication between the client and the server in a network
#If you need mouth to talk and communicate,so you need Socket to communicate

#Server Socket=>Server bind its  socket with an adress so that diffrent clients can identify
#Socket=>Ip Adress
#      =>Port#


#Chatroom Application 






from threading import Thread
import socket

host = "127.0.0.1"
port = 8080
clients = {}
adresses = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

def handle_clients(conn, address):
    name = conn.recv(1024).decode()
    welcome = "Welcome " + name + " .You can type #quit if you ever want to leave the Chat Room"
    conn.send(bytes(welcome, "utf8"))
    msg = name + " Has recently joined the ChatRoom"
    broadcast(bytes(msg, "utf8"))
    clients[conn] = name

    while True:
        msg = conn.recv(1024)
        if msg != bytes("#quit", "utf8"):
            broadcast(msg, name + ": ")
        else:
            conn.send(bytes("#quit", "utf8"))
            conn.close()
            del clients[conn]
            broadcast(bytes(name + " Has Left the chatroom","utf8"))

def accept_client_connections():
    while True:
        client_conn, client_address = sock.accept()
        print(client_address, "Has connected")
        client_conn.send("Welcome to the ChatRoom,Please type your name to continue.".encode("utf8"))
        adresses[client_conn] = client_address
        Thread(target=handle_clients, args=(client_conn, client_address)).start()

def broadcast(msg, prefix=""):
    for x in clients:
        x.send(bytes(prefix,"utf8")+msg)

if __name__ == "__main__":
    sock.listen(5)
    print("The server is running and is listening to clients requests")
    
    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()















# sock.listen(1)#This basically means taht the socket is continously listening to grant request.
# print("The Server is running and listening to client request")


# conn,adress=sock.accept() #=>This except method basically returns two things.
# #First of all the connection from where the request came from
# #Second is basically the adress of that line

# message="Hey there is something important for you"
# conn.send(message.encode())
# conn.close()
















