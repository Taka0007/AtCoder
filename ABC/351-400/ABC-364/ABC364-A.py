# Problem link    : https://atcoder.jp/contests/abc364/tasks/abc364_a
# Submission link : https://atcoder.jp/contests/abc364/submissions/56218274

# input
N = int(input())
S = []
for _ in range(N):
    s = input()
    S.append(s)
# declare valuables
ate_sweet = False
ans = 'Yes'
# prosessing
for i in range(N):
    if S[i] == 'sweet':
        if ate_sweet:
            if i != N-1:
                ans = 'No'
                break
            else:
                break
        else:
            ate_sweet = True
    else:
        ate_sweet = False
# output
print(ans)
