import speech_recognition as sr
from googlesearch import search

print("Enter Your Choice : ")
ch=int(input("1)TEXT\t2)VOICE"))
if ch==2:
        r=sr.Recognizer()

        with sr.Microphone() as source:
                print("Listening....");
                data=r.listen(source)
                print("Searching...")
                try:
                        query=r.recognize_google(data)
                except:
                        pass;
elif ch==1:
        query=input("Type the Query: ")
else :
        print("Invalid")
        exit

url=[]

for i in search(query,stop=10):
        print(i)
        url.append(i)

print(url)