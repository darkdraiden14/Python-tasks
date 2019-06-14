choice=input("Enter your choice : 1)touch (create single file)\n 2)touch (create multiple files)\n 3) touch -c 4) touch -a\n 5)touch -m")

#Touch single file
if choice=='1':
	files=input("Enter File Name : ")	
	f=open(files ,'w')
	f.close()
	print("You have successfully created a File")

#Touch multiple file
elif choice=='2':
	num=int(input("Number of files you want to create :"))
	listOfFile=[]
	for i in range(num):
		listOfFile.append(input(f"Enter file name {i}: "))
	for files in listOfFile:
		f=open(files,'w')
		f.close()
	print("You have successfully created a File")

#touch -c which means it does not create any file
elif choice=='3':
	files=input("enter file name : ")
	print("Nothing happened")
	exit()
else:
	print("Choose valid INPUT")

#More to come
