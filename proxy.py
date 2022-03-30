import socket
import time

print("starting proxy server")

s = socket.socket()  #get IPv4 TCP socket object
s.bind(("0.0.0.0", 12001))

print("...about to listen...")
s.listen(1)
conn, addr = s.accept()
print("connection accepted from: ", addr)

#print request
request = conn.recv(2048)
print(request)

#forward the http request to actual webserver
url = request.split()[1].decode()
print(url[1:])
d = socket.socket()
d.connect((url[1:], 80))
server_request = 'GET / HTTP/1.1\r\nHOST: %s\r\n\r\n'%url[1:]
d.sendall(server_request.encode())
time.sleep(1)
msg = d.recv(2048)

#send website page to the client
conn.send(msg)

conn.close()
print("connection closed")
s.close()
d.close()
print("socket closed")
print("proxy server complete")
