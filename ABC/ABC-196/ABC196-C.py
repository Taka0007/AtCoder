N = int(input())
for i in range(10**12):
    if int(str(i)*2)>N:
        print(i-1)
        break