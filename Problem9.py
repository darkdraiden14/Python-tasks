#To Take input from user
ch = input("Enter any thing:")

#if the length exceeds the limit 
if len(ch) > 500:
    ch=ch[:500]

#making dictionary and here cntForCh stands for (Count For Ch) variable
dictCount={}

for c in ch:
    if c in dictCount.keys():
        dictCount[c] += 1
    else :
        dictCount[c] = 1

list1=list(dictCount.values())
list1.sort(reverse=True)
