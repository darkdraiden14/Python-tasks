
#!/usr/bin/python3
import os

uname=input("Enter your Username : ")
check=0
num=[0,1,2,3,4,5,6,7,8,9]
for c in uname:
	if c in str(num):
		check=1
if check==1:
	print("Invalid User Name")

else:
	psswd="hello"+uname
	os.system("useradd -p " + psswd +" "+uname)

print("You have Successfully added one user")
