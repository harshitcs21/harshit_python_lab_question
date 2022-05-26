dict={}
size=int(input())
for i in range(size):
    k=int(input())
    dict1={}
    for j in range(1):
        k1=int(input())
        v1=int(input())
        dict1.update({k1:v1})
    dict.update({k:dict1})
print(dict)
