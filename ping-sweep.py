#! /usr/bin/python

import subprocess
import os
import multiprocessing
import sys

nrange = "192.168.1."

for i range(1, 254):
    address = nrange + str(i)
    res = subprocess.call(['fping', '-c', '3', '-w', '3', address])
    if res == 0:
        print address
    else:
        pass