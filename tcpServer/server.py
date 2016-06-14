#Server Code
from socket import *
import random
import thread
from Crypto.Random import random

BUFF = 4096
HOST = '127.0.0.1'
PORT = 3301 

def handler(clientsock,addr):
    while 1:
        data = clientsock.recv(BUFF)
        if not data:	break
	clientIn = data.lower().split()
	if clientIn : 
            print repr(addr) + ' recv:' + repr(clientIn[0])
	    if "goodbye" == clientIn[0] : clientsock.send("99 GOODBYE\r\n"); break 
	    elif "quine" == clientIn[0] : clientsock.send(quine())
	    elif "rand" == clientIn[0] : clientsock.send(rand(clientIn[1]))
            elif "base29" == clientIn[0] : clientsock.send(base29(clientIn[1]))
            elif "dh" == clientIn[0] : DH(clientIn[1])
            elif "code" == clientIn[0] : clientsock.send(code())
	    elif "next" == clientIn[0] : next()
            elif "koan" == clientIn[0] : clientsock.send(koan())
	    elif "get" == clientIn[0] : clientsock.send("web browsers are useless here. Good luck")
            else : clientsock.send("02 ERROR\r\n")
    clientsock.close()
    print addr, "- closed connection"

def koan():
    text = "01 OK\r\nA monk asked Zhaozhou to teach him.\r\nZhaozhou asked, 'Have you eaten your meal?'\r\nThe monk replied, 'Yes, I have.'\r\n'Then go wash your bowl', said Zhaozhou.\r\nAt that moment, the monk was enlightened.\r\n.\r\n"
    return text

def next():
    f = open("nextInfo", "a")
    clientsock.send("01 OK\r\n")
    while 1 :
        text = clientsock.recv(BUFF)
        f.write(text)
        if text.strip() == "." : break
    clientsock.send("01 OK\r\n")

def code():
    f = open("serversource", "r")
    text = "01 OK\r\n" + f.read() + ".\r\n"
    return text

def DH(primeMod):
    try : primeMod = int(primeMod)
    except ValueError :
        clientsock.send("02 ERROR\r\n")
        return
    base = int(random.randint(2,9))
    secretInt = int(random.randint(5, 100))
    e = (base^secretInt) % primeMod
    clientsock.send("01 OK " + str(base) + " " + str(e) + "\r\n")
    try : e2 = int(clientsock.recv(BUFF))
    except ValueError :
        clientsock.send("02 ERROR\r\n")
        return
    secret = (e2^secretInt) % primeMod
    clientsock.send("03 DATA " + str(secret) + "\r\n")
    return

def quine():
    f = open("quine.py", "r")
    send = "01 OK\r\n" + f.read() + ".\r\n"
    return send

def rand(number):
    L = "01 OK\r\n"
    try : number = int(number)
    except ValueError : 
        L = L + "02 ERROR\r\n"
        return L
    for i in range(0, number):
	r = random.randint(0, 255)
	L = L + str(r)+ "\r\n"
    L = L + ".\r\n"
    return L

def base29(number):
    digits = "0123456789ABCDEFGHIJKLMNOPQRST"
    newNum = ""
    try : number = int(number)
    except ValueError : 
        return "02 ERROR\r\n"
    while 1:
        i = number % 29
        newNum = digits[i] + newNum
        number = number / 29
        if number == 0: break
    ret = "01 OK " + newNum + "\r\n"
    return ret


if __name__=='__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        print 'waiting for connection... listening on port', PORT
        clientsock, addr = serversock.accept()
        clientsock.send('3301 Good Luck \r\n')
	print '...connected from:', addr
        thread.start_new_thread(handler, (clientsock, addr))
