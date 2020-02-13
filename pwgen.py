#!/usr/bin/python3

import random
import time

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?><.#*&%$§)(][='

length = input('password length? ')
length = int(length)

print("""[*] Generate random passwords.......""")

time.sleep(2)

for p in range(10):
    password = ''
    
    for c in range(length):
        password += random.choice(chars)
    print(password)
