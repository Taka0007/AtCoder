A = input()
B = int(input())

ans = A[ (B%(len(A))) - 1 ]
print(ans)