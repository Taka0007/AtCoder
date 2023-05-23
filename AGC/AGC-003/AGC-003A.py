S = input()

if len(set(S))%2!=0:
    ans = 'No'
elif 'W' not in set(S) and 'N' not in set(S):
    ans = 'No'
elif 'E' not in set(S) and 'S' not in set(S):
    ans = 'No'
elif 'E' not in set(S) and 'N' not in set(S):
    ans = 'No'
elif 'W' not in set(S) and 'S' not in set(S):
    ans = 'No'
else:
    ans = 'Yes'

print(ans)
