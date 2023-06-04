N = int(input())
num_dic = []
min_id = 10*10
min_num = 10**10

for i in range(N):
        a,b = input().split()
        b = int(b)
        li = [a,b]
        num_dic.append(li)

if N==2:
    if num_dic[0][1]>num_dic[1][1]:
        print(num_dic[1][0])
        print(num_dic[0][0])
    else:
        print(num_dic[0][0])
        print(num_dic[1][0])
    
else:
    for i in range(N):
        if num_dic[i][1]<= min_num:
            min_id = i
            min_num = num_dic[i][1]

    for i in range(min_id,min_id+N):
        print(num_dic[i%N][0])