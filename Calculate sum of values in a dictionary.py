dict={}
size=int(input("enter the size of the dict:"))
for i in range (size):
    keys=int(input())
    values=int(input())
    dict.update({keys:values})
print(dict)
sum=0
for i in dict.values():
    sum=sum+i
print(sum)
