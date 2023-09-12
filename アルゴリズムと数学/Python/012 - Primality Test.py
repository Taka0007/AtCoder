def prime(N):
    if N==1:
        return False
    elif N==2:
        return True
        
    for i in range(2, int(N**(1/2))+2 ):
        if N%i==0:
            return False
    else:
        return True
        
N = int(input())

if prime(N):
    print('Yes')
else:
    print('No')