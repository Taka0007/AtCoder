def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

N   = int(input())
str = 'indeednow'

for i in range(N):
    S = input()
    
    if are_anagrams(str, S):
        print('YES')
    else:
        print('NO')