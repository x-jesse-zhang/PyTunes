import socket

class Networker():
	def __init__(self):
		# For now, just set whether you are the client or the server
		role = "SERVER"
		# role = "CLIENT"

		port = 25000
		
		if role == "SERVER":
			self.setupServer(port)
		else:
			destIP = "172.16.168.190"
			self.setupClient(destIP, port)

	def setupServer(self, port):
		print "running server"
		ip = socket.gethostbyname(socket.gethostname())
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serversocket.bind((ip, port))
		serversocket.listen(2)
		print "got to listen"
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

nt = Networker()