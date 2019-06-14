#!/bin/python3

import os
import crypt

uname=input("Enter your Username : ")
check=0
n=[0,1,2,3,4,5,6,7,8,9]
for i in uname:
	if i in str(n):
		check=1
if(check==1):
	print("Invalid User Name (Please don't use numbers")
else:
	psswd="hello"+uname
	encPsswd = crypt.crypt(psswd,"22") 
	os.system("useradd -p " + encPsswd +" "+uname)
	print("You have Successfully added one User")

