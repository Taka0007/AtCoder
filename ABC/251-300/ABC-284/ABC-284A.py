N = int(input())
string = []

for i in range(N):
    a = input()
    string.append(a)
    
string.reverse()

for i in range(N):
    print(string[i])
