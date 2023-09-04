N = int(input())
mod = 10**7 + 9
ans = ((pow(4,N+1,mod)-1)%mod)//3
print(ans)