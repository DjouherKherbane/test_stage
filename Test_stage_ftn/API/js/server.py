#1.creer la cle et le certificat du server avec la commande :  " openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 "
#2.creer le fichier server.py:" gedit server.py"


from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import socketserver
import sys


host = ('localhost', int(sys.argv[1]))

httpd = HTTPServer(host, SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket,
                               keyfile="key.pem",
                               certfile='cert.pem',server_side=True)


url = "https://"+str(host[0])+":"+str(host[1])+"/"


print('HTTPS server started') 
print('........................')
print("Server running on : ")
print(url)
print('........................')

httpd.serve_forever()


#3.Executer avec :"sudo python3 server.py 4000" 

