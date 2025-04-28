B = int(input())
num = 1
ans = -1

while pow(num,num) <= B:
    if pow(num,num) == B:
        ans = num
        break
    num += 1
print(ans)