from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to reveive')
while 1:
	connectionSocket,addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	caplitalizedSentence = sentence.upper()
	connectionSocket.send(caplitalizedSentence)
	connectionSocket.close()

	