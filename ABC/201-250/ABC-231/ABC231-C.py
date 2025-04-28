# Problem link    : https://atcoder.jp/contests/abc231/tasks/abc231_c
# Submission link : https://atcoder.jp/contests/abc231/submissions/56235652

# input
N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
X = []
for _ in range(Q):
    x = int(input())
    X.append(x)

# binary search
def search(A, x):
    left  = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] < x:
            left = mid + 1
        else:
            right = mid
    return len(A) - left

for x in X:
    print(search(A,x))
