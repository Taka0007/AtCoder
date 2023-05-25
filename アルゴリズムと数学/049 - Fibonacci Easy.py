N = int(input())
fibo = [0]*(N+1)
div = 10**9 + 7
fibo[0] = 1
fibo[1] = 1

for i in range(2,N):
    fibo[i] = (fibo[i-1]+fibo[i-2])%div

print(fibo[N-1])