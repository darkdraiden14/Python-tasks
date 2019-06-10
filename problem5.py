import datetime

name =input("Enter your Name : ")
t=datetime.datetime.now()

if t.hour<12:
	print("Good Morning,",name +"!")
elif t.hour>11 and t.hour<=16:
	print("Good Afternoon,",name+"!")
elif t.hour > 16 and t.hour <=21:
	print("Good Evening,",name+"!")
else:
	print("Good Night,", name+"!")
