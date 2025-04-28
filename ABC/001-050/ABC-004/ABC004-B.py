st_list = []

for _ in range(4):
    s = input()
    s = s[::-1]
    st_list.append(s)
    
for i in range(1,5):
    print(st_list[-i])