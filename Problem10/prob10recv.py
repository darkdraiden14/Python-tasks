#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444  # 0  -  1024

#creating udp socket
#             ip type v4 , uDp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# fitting ip and port with udp socket
s.bind((recv_ip,recv_port))

choice = raw_input("Enter your Choice : 1.TWO way 2)ONE way")
# recv data from sender
if choice=="1": 
    while 4>3:
        data=s.recvfrom(120)
        if data[0] =="Y":
            break
        print("message from sender: ",data[0])
        print("Sender IP + Port --socket:",data[1])
        # reply to sender
        msg=raw_input("Enter your reply :")
        s.sendto(msg,data[1])
    
elif choice == "2":
    while 4>3:
        data=s.recvfrom(120)
        if data[0] =="Y":
            break
        print("message from sender: ",data[0])
        print("Sender IP + Port --socket:",data[1])
    
else:
    print("Enter valid choice:")

s.close()
