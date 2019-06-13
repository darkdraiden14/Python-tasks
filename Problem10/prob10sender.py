#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444  # 0  -  1024

#creating udp socket
#             ip type v4 , uDp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# sending data to target
choice=raw_input("Enter Choice: 1)TWO WAY 2)ONE WAY")

if choice == "1":
    #format : s.sendto(message,((recv_ip,recv_port))
    while 4>3:
        msg=raw_input("Enter you message:")
        s.sendto(msg,(recv_ip,recv_port))
        print(s.recvfrom(50))

        rspns=raw_input("Wanna Quit: Y?N")
        if rspns=="Y":
            s.sendto('Q',(recv_ip,recv_port))

elif choice == "2":
      while 4>3:
          msg=raw_input("Enter you message:")
          s.sendto(msg,(recv_ip,recv_port))
          rspns=raw_input("Wanna Quit: Y?N")
          if rspns=="Y":
              s.sendto('Q',(recv_ip,recv_port))
           
else:
    print("enter valid choice:")


s.close()
