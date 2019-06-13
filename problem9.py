#!/usr/bin/Python3
import collections
char = input("Enter Any thing:")

#To check the length of the input String
if len(char)>500:
    char=char[:500]

print(f'You Have Entered: {char}\n')
#1) Print Number of repeated characters in descending order
dictChar={}
for c in char:
    if c in dictChar.keys():
        dictChar[c] +=1
    else:
        dictChar[c] =1

dictChar=sorted(dictChar.items(),reverse=True,key=lambda x :x[1])
print("Number of repeated characters in reverse order:")
print(dictChar)

#2) Repeated words in descending order
listWords=list(char.split())
print("\n")
dictWords ={}
for item, count in collections.Counter(listWords).items():
    if count>1:
        dictWords[item]=count

print("\nThe Repeated Words are:")
print(dictWords)
