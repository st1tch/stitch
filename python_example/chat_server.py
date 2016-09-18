from socket import *
from threading import *

#receive func
def serverRecv() :
	while True :
		Msg = clientSocket.recv(1024)
		print "client : " + str(Msg)
	clientSocket.close()

#server init
print "Server Network Init..."

#set Port, Host
Port = 7777
Host = "127.0.0.1"
conn = ( Host, Port)

#create serversocket
serverSocket = socket(AF_INET, SOCK_STREAM)

#bind port, host
serverSocket.bind( conn )

#listening
serverSocket.listen(5)

#client accept, connect
clientSocket, addr = serverSocket.accept()
print "Connected " + str(addr) + "\n"

#receive thread start
Thread(target = serverRecv).start()

try :
	#send loop
	while True :
		SendMsg = raw_input()
		clientSocket.send(SendMsg)
except :
	#end connection
	clientSocket.close()
	exit()




