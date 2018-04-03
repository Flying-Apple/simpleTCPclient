from socket import *
import http.server
import socketserver
import sys
import time

total = len(sys.argv)
cmdargs = str(sys.argv)

serverPort = int(sys.argv[1]); # input port number
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print( "The server is ready to receive")
header=''
#Handler = http.server.SimpleHTTPRequestHandler				# from docs.python.org/3/library/http.server.html
def headerdefine(code):
    hd = ''
    if (code == 200):
        hd = 'HTTP/1.1 200 OK\n'
    elif(code == 404):
        hd = 'HTTP/1.1 404 Not Found\n'
    current_date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
    hd += 'Date: ' + current_date +'\n'
    hd += 'Server: Simple-Python-HTTP-Server\n'
    hd += 'Connection: close\n\n' 
    return hd.encode()

''''
with socketserver.TCPServer(("", serverPort), Handler) as httpd: #a simple http server
    print("serving at port", serverPort)
    httpd.serve_forever()								#listen to port and ready to handle request
	
'''

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.decode().split()
    #print(capitalizedSentence)
    print(capitalizedSentence)
    if capitalizedSentence[1] =='/':
        header = headerdefine(200)
        requested = '/index.html'
        indexpage = open('index.html','rb')
        response = indexpage.read()
        connectionSocket.send(header+response)
    else:
        header = headerdefine(404)
        response = b"<html><body><p>Error 404: File not found</p><p>Python HTTP server</p></body></html>"
        connectionSocket.send(header+response)
    if capitalizedSentence[1] =='/yoda.png':
        header = headerdefine(200)
        yoda = open('yoda.png', 'rb')
        response = yoda.read()
        #print(response)
        connectionSocket.send(header+response)

    #print(response)
    #print(capitalizedSentence)
  
    connectionSocket.close()
