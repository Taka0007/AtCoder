#     autor: Taka007
#     2021.04.11 start


import math



N = int(input())
num = list(map(int,input().split()))

answer_list = []


for i in range(N):

    k = 0

    while num[i]%2==0:

        num[i] = int(num[i]/2)
        k+=1
    answer_list.append(k)


answer = sum(answer_list)


print(answer)
