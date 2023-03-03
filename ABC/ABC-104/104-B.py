S = input()
N = len(S)

sub   = S[2:N-1]
cond1 = bool(S[0]=='A')
cond2 = bool('C' in sub)
cond3 = bool(S.count('A')==1 and S.count('C')==1)
cond4 = bool(sum(map(str.isupper, S))==2)

if cond1 and cond2 and cond3 and cond4:
    print('AC')
    
else:
    print('WA')
