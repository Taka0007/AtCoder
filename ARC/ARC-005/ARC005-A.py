N = int(input())
S = list(map(str,input().split()))
S[-1] = S[-1][:-1]

ans = S.count("TAKAHASHIKUN") + S.count("Takahashikun") + S.count("takahashikun")
print(ans)