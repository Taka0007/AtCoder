# input
N,M = map(int,input().split())
A   = list(map(int,input().split()))
# calculation
count = 0
while len(set(A))==M:
    del A[-1]
    count += 1
# output
print(count)