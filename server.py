import socket

s = socket.socket()

# in bracket we need to mention the type of ip and the type of network,like ipv4/ipv6 and for network is it TCP or UDP connection
print('Socket Created')
s.bind(('localhost',9999))
#here in bracket we will put the ipadd and the port

s.listen(3)
#here in bracket we will have to mention the number of connection my server will work at once,for here my server will work with only 3 connections
print('Waiting for connections')

while True:
    c,addr = s.accept()
    # here c means the client socket, so in this case out server socket is accepting the client socket and the address also

    name=c.recv(1024).decode()
    print("Connected Successfully with",addr,name)

    c.send(bytes('Welcome to My World','utf-8'))
    c.close()