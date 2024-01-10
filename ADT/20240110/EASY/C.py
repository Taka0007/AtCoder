# input
N,M = map(int,input().split())
lis = []

# Graph input
for i in range(M):
    lis.append(list(map(int,input().split())))

# def functiuon
# i番目の都市と結ばれている道路を都市を昇順で返す
def solve(i):
    ans = []
    