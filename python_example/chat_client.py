from socket import *
from threading import *

def clientRecv() :
	while True :
		RecvMsg = clientSocket.recv(1024)
		print "server : " + RecvMsg 
	clientSocket.close()

print "Client Network Init...."

serverName = "127.0.0.1"
serverPort = 7777
conn = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect( conn )

print "Server conneted!"

Thread(target = clientRecv).start()

try :
	while True :
		sendMsg = raw_input()
		clientSocket.send( sendMsg )
except :	
	clientSocket.close()
	exit()
