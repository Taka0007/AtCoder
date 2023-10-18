S   = input()
num = []
for i in S:
    num.append(int(i))
ans = 45 - sum(num)
print(ans)