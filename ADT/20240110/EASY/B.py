# input
S = list(input())

for i in range(1,len(S)//2+1):
    S[2*i-2],S[2*i-1] = S[2*i-1],S[2*i-2]

# output
print(*S,sep="")