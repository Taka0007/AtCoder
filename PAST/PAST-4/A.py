import math

A,B,C=map(int,input().split())
List=[A,B,C]
List.sort()
answer=List[1]

if answer==A:
    print("A")

elif answer==B:
    print("B")

else:
    print("C")
