from socket import *
serverName = '192.168.63.1'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input('input lowercase sentence:')
clientSocket.sendto(str.encode(message),(serverName,serverPort))
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()

