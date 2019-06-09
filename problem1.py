#!/bin/python3

import datetime

name=input("Enter your name:")
age=int(input("Enter your age:"))

y=datetime.datetime.now()

<<<<<<< HEAD
if age==95:
    print("Congrats!, You are already 95..")

elif age >95:
    print(f"You have already crossed the age 95 in year :{((95-age)+y.year)}")

else:
    print(f'Your age will 95 in year {((95-age)+y.year)}')
