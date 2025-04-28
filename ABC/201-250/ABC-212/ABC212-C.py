import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = float('inf')

for i in range(N):
    num = bisect.bisect_left(B, A[i])
    if num < M:
        ans = min(ans, abs(A[i] - B[num]))
    if num > 0:
        ans = min(ans, abs(A[i] - B[num - 1]))

print(ans)