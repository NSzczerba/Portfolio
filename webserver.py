#webserver.py
import socket

#create a socket and listen for a connection then accept it and receive its request
with socket.socket() as s:
 s.bind(("0.0.0.0", 12000))
 s.listen(1)
 print("listening for a connection")
 conn, addr = s.accept()
 print("connected to: ", addr)
 request = conn.recv(2048)
 print(request.decode())

 #find the target file name by splitting the get request and then open the file that corresponds with the get request
 filename = request.split()[1].decode()
 if filename[1:] == '' or filename[1:] == 'index.html':
  f = open('index.html')
 elif filename[1:] == 'file1.html':
  f = open('file1.html')
 elif filename[1:] == 'file2.html':
  f = open('file2.html')
 else: #If no html file exists, print to screen telling user that no file exists
  msg = '<h1>The requested URL was not found on this server.</h1>'
  conn.send('HTTP/1.0 200 OK\r\n\r\n'.encode())
  for i in range(0, len(msg)):
   conn.send(msg[i].encode())
  conn.close()
  s.close()
  print("webserver complete")
  exit()

 #put the contents of the correct file into a variable then send the contents to the client then close the connection and port when done
 msg = f.read()
 f.close()

 conn.send('HTTP/1.0 200 OK\r\n\r\n'.encode())
 for i in range(0, len(msg)):
  conn.send(msg[i].encode())

 conn.close()
 s.close()
 print("webserver complete")
