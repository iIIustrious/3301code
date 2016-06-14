#!/usr/bin/env python3
#Will join the irc and warn us whent he watched onion comes back online
import sys
import socket
import string
import time
 
HOST = "irc.freenode.net"
PORT = 6667
 
NICK = "iiibot"
IDENT = "iiibot"
REALNAME = "iiibot"
MASTER = "iii"
CHANNEL = "#cicadasolvers"
 
readbuffer = ""
 
s=socket.socket( )
s.connect((HOST, PORT))
 
s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
s.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), 
"UTF-8"))
s.send(bytes("JOIN #smiteclub\r\n", "UTF-8"));
s.send(bytes("PRIVMSG %s :Hello Master!\r\n" % MASTER, "UTF-8"))
time.sleep(5)
s.send(bytes("PRIVMSG %s : an onion is back up\r\n" % "#cicadasolvers", "UTF-8"))
time.sleep(20)
