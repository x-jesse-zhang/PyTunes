import socket

class Networker():
	def __init__():
		# For now, just set whether you are the client or the server
		role = "SERVER"
		# role = "CLIENT"

		port = 25000
		
		if role == "SERVER":
			setupServer(port)
		else
			destIP = "172."
			setupClient(destIP, port)

	def setupServer(self, port):
		ip = socket.gethostbyname(socket.gethostname())
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serversocket.bind(ip, port)
		self.serversocket.listen(2)

	def setupClient(self, destIP, port):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((destIP, port))