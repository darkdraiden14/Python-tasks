#!/bin/python3
import os
import crypt
username=input("Enter your Username : ")
flag=0
num=[0,1,2,3,4,5,6,7,8,9]
for i in username:
	if i in str(num):
		flag=1
if(flag==1):
	print("Invalid User Name")
else:
	password="hello"+username
	encPass = crypt.crypt(password,"22") #Encrypting Password
	os.system("useradd -p " + encPass +" "+username)
	print("User Added!")

