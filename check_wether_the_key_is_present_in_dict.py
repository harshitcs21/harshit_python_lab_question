d={}
x=int(input())
for i  in range (x):
    k=int(input())
    v=int(input())
    d.update({k:v})
key=int(input())
for i in d.keys():
    if i==key:
        print('present')
        break
    else:
        print('not  present')
