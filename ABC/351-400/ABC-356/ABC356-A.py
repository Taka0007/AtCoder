# Problem link    : https://atcoder.jp/contests/abc356/tasks/abc356_a
# Submission link : https://atcoder.jp/contests/abc356/submissions/54141539

# input
N,L,R = map(int,input().split())
Num_lis = []
# construction
for num in range(1,L):
    Num_lis.append(num)
for num in range(R,L-1,-1):
    Num_lis.append(num)
for num in range(R+1,N+1):
    Num_lis.append(num)
# output
print(*Num_lis)
