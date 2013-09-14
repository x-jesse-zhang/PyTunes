import socket
import time

class Networker():
	def __init__(self):
		# For now, just set whether you are the client or the server
		# role = "SERVER"
		role = "CLIENT"

		port = 50000
		
		if role == "SERVER":
			self.setupServer(port)
		else:
			#destIP = "172.16.221.236"  #JESSE
			#destIP = "172.16.158.84"   #SAM
			#destIP = "172.16.168.190"  #STEPHEN
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
			ct = ClientThread(clientsocket)
			
	def setupClient(self, destIP, port):
		self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.mySocket.connect((destIP, port))
		print self.mySocket.recv(2)

class ClientThread:
	def __init__(self,socket):
		socket.send(time.time() + 10)
		print "finished"

nt = Networker()