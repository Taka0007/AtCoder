N, A, B = map(int, input().split())
ans = 0

for i in range(1, N + 1):
    judge = 0
    
    for digit in str(i):
        judge += int(digit)
        
    if A <= judge <= B:
        ans += i

print(ans)
