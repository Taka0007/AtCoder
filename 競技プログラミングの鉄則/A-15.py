# 二分探索の定義
def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


N = int(input())
A = list(map(int,input().split()))

# 座標圧縮後の配列の定義
B = [0]*N

# 元の配列の重複を削除し、ソートした配列Tの宣言
T = list(set(A))
T.sort()

for i in range(N):
    B[i] = binary_search(T,A[i])
    B[i] += 1
print(*B)