num=int(input("enter the mobile no.:"))
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum)
