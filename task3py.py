from math import sqrt
om2=[]
def om(list,x=0,y=0):
    listt=[]
    for i in range(list):
        sum=(int(input()))
        listt.append(sum)
    for j in listt:
        z=sqrt(j)
        if z%1==0:
            if j>x and j<y:
                om2.append(j)
list=int(input())
x=int(input())
y=int(input())
om(list,x,y)
print(om2)

