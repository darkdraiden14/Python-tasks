#!/bin/python3

import datetime

name=input("Enter your name:")
age=int(input("Enter your age:"))

y=datetime.datetime.now()

print(f'Your age will 95 in year {((95-age)+y.year)}')
