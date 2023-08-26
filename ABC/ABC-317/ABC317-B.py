N = int(input())
A = list(map(int,input().split()))
A.sort()

for i in range(N-1):
    if abs(A[i]-A[i+1])>1:
        print(A[i]+1)
        break