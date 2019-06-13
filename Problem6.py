#Python Program which performs similar operation like "CAT" shell command

choice = int(input("Enter you Choice : \n 1. Cat \t2.Cat -b\t3.Cat -s\t4.Cat -E\n:"))


#Normal Reading like cat function
if choice==1:
    file=open("demofile.txt","r")
    print(file.read())
    file.close()

#With -b option
elif choice==2:
    i=1
    file=open("demofile.txt","r")
    #to Store lines of a file in a list
    for lines in file:
        if lines.strip() !="":
            print(str(i)+". "  +lines.strip())
            i+=1
    file.close()

#With -s option
elif choice==3:
    file=open("demofile.txt","r")
    #to Store lines of a file in a list
    for lines in file:
        if lines.strip() !="":
            print(lines.strip())
    file.close()

#with -E option:
