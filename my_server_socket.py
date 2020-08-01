import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)


s.bind(("127.0.0.1", 5000)) #My socket is started from here
s.listen(5) #It communicate with five concurrent client
conn, addr=s.accept()# It returns two thing one is connection object & with the help of this object we can communicate with client who is connected ie sending message or file and another object ie addr object tells server that what is ip address and port number of client.
#s.send()
#s.recv()

conn.send(b"Hey this is server")
print(conn.recv())