N = int(input())
max_point = -1
max_index = -1
poem_set = set()

for i in range(N):
    s,t = map(str,input().split())
    if s not in poem_set:
        poem_set.add(s)
        if max_point < int(t):
            max_index = i+1
            max_point = int(t)
            
print(max_index)