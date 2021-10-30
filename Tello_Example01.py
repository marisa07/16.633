#############################
# Tello EDU Sample Program 01 
#
# MIT NEET-AM Autonomous Machines
#
# 08/12/2021
#############################

import threading
import socket
import sys
import time

host = ''
port = 9000
locaddr = (host, port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\nExit . . .\n')
            break

recvThread = threading.Thread(target=recv)
recvThread.start()

try:
    msg = "command";
    # Send data
    msg = msg.encode(encoding="utf-8")
    sent = sock.sendto(msg, tello_address)

    msg = "takeoff";
    # Send data
    msg = msg.encode(encoding="utf-8")
    sent = sock.sendto(msg, tello_address)
    time.sleep(10)

    msg = "go 0 0 100 10";
    # Send data
    msg = msg.encode(encoding="utf-8")
    sent = sock.sendto(msg, tello_address)
    time.sleep(6)

    msg = "ccw 180";
    # Send data
    msg = msg.encode(encoding="utf-8")
    sent = sock.sendto(msg, tello_address)
    time.sleep(6)
    
    msg = "back 100";
    # Send data
    msg = msg.encode(encoding="utf-8")
    sent = sock.sendto(msg, tello_address)
    time.sleep(6)

    # msg = "go -100 0 100 10";
    # # Send data
    # msg = msg.encode(encoding="utf-8")
    # sent = sock.sendto(msg, tello_address)
    # time.sleep(3)

    # msg = "down 20";
    # # Send data
    # msg = msg.encode(encoding="utf-8")
    # sent = sock.sendto(msg, tello_address)
    # time.sleep(3)

    # msg = "up 20";
    # # Send data
    # msg = msg.encode(encoding="utf-8")
    # sent = sock.sendto(msg, tello_address)
    # time.sleep(3)

    # msg = "flip l";
    # # Send data
    # msg = msg.encode(encoding="utf-8")
    # sent = sock.sendto(msg, tello_address)
    # time.sleep(3)

    # msg = "flip r";
    # # Send data
    # msg = msg.encode(encoding="utf-8")
    # sent = sock.sendto(msg, tello_address)
    # time.sleep(3)

    # msg = "cw 90";
    # # Send data
    # msg = msg.encode(encoding="utf-8")
    # sent = sock.sendto(msg, tello_address)
    # time.sleep(3)

    # msgbat = "battery?";
    # # Send data
    # msgbat = msgbat.encode(encoding="utf-8")
    # sent = sock.sendto(msgbat, tello_address)

    msg = "land";
    # Send data
    msg = msg.encode(encoding="utf-8")
    sent = sock.sendto(msg, tello_address)

    # close the socket
    sock.close()

except KeyboardInterrupt:
    print('\n . . .\n')
    sock.close()
