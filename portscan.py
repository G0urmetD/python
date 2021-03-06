#!/usr/bin/env python

# ----------------------------------------------- #
# Scanner for complete port range
# 
# ----------------------------------------------- #


import socket
import sys
from datetime import datetime

target = "example"
targetIP = socket.gethostbyname(target)

tstart = datetime.now()

try:
    for p in range(1, 45000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((targetIP, p))
        if res == 0:
            print("Offene Verbindung in Port " + str(p))
        sock.close()
except Exception:
    print("There was an error.")
    sys.exit()

tend = datetime.now()
diff = tend - tstart

print("Scan completed in " + str(diff))