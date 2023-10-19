import re

# 大文字が含まれるか判定
def in_upper(S):
    result = re.search('[A-Z]', S)
    return True if result else False

# 小文字が含まれるか判定
def in_lower(S):
    result = re.search('[a-z]', S)
    return True if result else False

def unique(S):
    return len(set(S)) == len(S)

S = input()

if in_upper(S) and in_lower(S) and unique(S):
    print('Yes')
else:
    print('No')