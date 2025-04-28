N = int(input())
tri = [0,0,1]

if N <= 3:
    print(tri[N-1])

else:
    for i in range(3,N):
        num = (tri[i-1] + tri[i-2] + tri[i-3]) % (10007)
        tri.append(num)
    print(tri[N-1])