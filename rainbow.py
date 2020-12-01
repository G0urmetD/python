import zipfile
import itertools
import string
import hashlib
from threading import Thread
import zipfile


#zipfile = zipfile.ZipFile("H:\Programmieren\rainbow.txt")

def bruteforce():
    myLetters = string.ascii_letters + string.digits + string.punctuation
    for i in range(3,16):
        for j in map(''.join, itertools.product(myLetters, repeat=i)):
            t = Thread(target=crack, args=(zipfile, j))
            t.start()

def dictionary():
    passwords = open("table.txt")
    for line in passwords.readlines():
        pwd = line.strip('\n')
        t = Thread(target=crack, args=(zipfile, pwd))
        t.start()

def gen_rainbowtable():
    passwords = open("table.txt")
    output = open("rainbowtable.txt", "w")
    for line in passwords.readlines():
        pwd = line.strip('\n')
        hash = hashlib.sha512(str.encode(pwd) + "#" + pwd + "\n")
        output.write(hash.hexdigest())
    output.close()
    passwords.close()

def crack(zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print('Success: Password is ' + pwd)
    except:
        pass

gen_rainbowtable()
