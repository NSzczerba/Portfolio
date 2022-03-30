This repository consists of a range of small to large projects that I have worked. 

# March 30th, 2022
**This repository was created and I have added a few projects.**

**webserver.py** is a simple apache2 webserver I created using the python language on Google Cloud's VM service. The webserver uses a TCP connection and listens on port 12000. The web client will send a GET request to the webserver for a specific html file, and if the file is accessable to the webserver, it will return it to client. If no such file exists, the webserver will send html displaying to the client that no file exists.

**proxy.py** is a simple apache2 proxy server I created using the python language on Google Cloud's VM service. The proxy uses a TCP connection and listens on port 12001. A web client will send a request for a specific website, and the proxy will receive the GET request from the client. The proxy server will use that GET request to retrieve the desired website and return it to the user.

**sender.py** and **listener.py** are an example of a simple UDP connection, where the listner.py file will listen on all IP addresses and port 12000 for any incoming traffic. The sender.py file will send out a message on port 12000, which the listener.py file will pick up and display the information of the message to the screen. The listener.py will send an acknowledgment back to the sender.py file on what it received. **Located in UDP Connection Files folder**
