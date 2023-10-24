p,q = map(str,input().split())
st  = ['A','B','C','D','E','F','G']
dis = [3,1,4,1,5,9]
if p>q:
    p,q = q,p

ans = sum(dis[st.index(p):st.index(q)])
print(ans)