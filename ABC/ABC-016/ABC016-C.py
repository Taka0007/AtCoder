N, M = map(int, input().split())
graph = {i: set() for i in range(1, N + 1)}
num = []
for i in range(M):
    a, b = map(int, input().split())
    num.append((a, b))

for a, b in num:
    graph[a].add(b)
    graph[b].add(a)

# IDがNの人の友達の友達の人数を返す関数
def friends_of_friends(N):
    friends_list = set()
    friends_of_friends_list = set()
    
    # 直接の友達をfriends_listに追加
    for i in graph[N]:
        friends_list.add(i)
    
    # 友達の友達をfriends_of_friends_listに追加
    for friend in friends_list:
        for friend_of_friend in graph[friend]:
            if friend_of_friend != N and friend_of_friend not in friends_list:
                friends_of_friends_list.add(friend_of_friend)
    
    return len(friends_of_friends_list)

for i in range(1, N + 1):
    print(friends_of_friends(i))