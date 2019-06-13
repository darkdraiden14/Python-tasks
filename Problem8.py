#!/usr/bin/python3

import os
import shutil
import gtts

#Creating file in order to store commands
file=open("ListOfCommand","a")
#Take commands as a input from User
cmmnd=input("Enter the Shell Comand:")
file.write(cmmnd)

#Execute the Command
if(shutil.which(cmmnd)):
    print("Command Founnd , Output of given Command is :\n")
    os.system(cmmnd)

else:
    print("The Command you have entered Does Not exist")
file.close()


#To read the Commands entered by User
file1=open("ListOfCommand","r")

print("\nYou have entered following commands So far:\n")
print(file1.read())

file1.close()
