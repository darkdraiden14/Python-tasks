#!/usr/bin/Python3
import time
from googlesearch import search

links=[]
web = input("Enter topic to search : ")
for i in search(web,stop=10):
	links.append(i)

print(links)
