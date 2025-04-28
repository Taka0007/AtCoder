Program ABC149_A
Implicit None
Character(len=200) :: S, T ,ans

Read*,S,T
ans = trim(T) // trim(S)
Print "(A)", ans

End Program ABC149_A