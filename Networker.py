import socket

class Networker():
	def __init__():
		# For now, just set whether you are the client or the server
		# role = "SERVER"
		role = "CLIENT"

		port = 25000
		
		if role == "SERVER":
			setupServer(port)
		else:
			destIP = "172.16.168.190"
			setupClient(destIP, port)

	def setupServer(self, port):
		ip = socket.gethostbyname(socket.gethostname())
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serversocket.bind(ip, port)
		self.serversocket.listen(2)
		while 1:
			(clientsocket, address) = serversocket.accept()
		    #now do something with the clientsocket
		    #in this case, we'll pretend this is a threaded server
			ct = client_thread(clientsocket)
			
	def setupClient(self, destIP, port):
		self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mySocket.connect((destIP, port))
		while 1:
			print mySocket.read()

class ClientThread:
	def __init__(socket):
		while 1:
			socket.send("HI")