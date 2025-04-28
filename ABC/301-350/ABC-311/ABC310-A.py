N = int(input())
S = input()
ans_set = set(S[0])

for i in range(1,N):
    ans_set.add(S[i])
    
    if len(ans_set)==3:
        ans = i+1
        break

print(ans)