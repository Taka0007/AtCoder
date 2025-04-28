# Problem link    : https://atcoder.jp/contests/abc341/tasks/abc341_d
# Submission link : https://atcoder.jp/contests/abc341/submissions/50386288


# function GCD & LCM
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)
    
def count_valid_numbers(x, n, m, lcm_nm):
    return x // n + x // m - 2 * (x // lcm_nm)

# binary search
def binary_search(k, n, m, lcm_nm):
    left, right = 1, k * max(n, m)
    while left < right:
        mid = (left + right) // 2
        if count_valid_numbers(mid, n, m, lcm_nm) < k:
            left = mid + 1
        else:
            right = mid
    return left

# input
N, M, K = map(int, input().split())
lcm_nm = lcm(N, M)
answer = binary_search(K, N, M, lcm_nm)
print(answer)