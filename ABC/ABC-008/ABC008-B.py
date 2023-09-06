N = int(input())
vote = dict()

for i in range(N):
    S = input()
    
    if S not in vote:
        vote[S] = 1
    else:
        vote[S] += 1

vote2 = sorted(vote.items(), key=lambda x:x[1],reverse=True)
print(vote2[0][0])