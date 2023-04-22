N = int(input())
S = input()

ans = S.index('*')
slash = [i for i, x in enumerate(S) if x == '|']


if ans > slash[0] and ans < slash[1]:
    print('in')
    
else:
    print('out')
