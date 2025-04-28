# Problem link : https://atcoder.jp/contests/abc109/tasks/abc109_b
# Submit link  : https://atcoder.jp/contests/abc109/submissions/50727919

# input
N = int(input())
words = []
last_str = ''
for _ in range(N):
    S = input()
    words.append(S)
    
word_set = set()
word_set.add(words[0])

# output
for i in range(1,N):
    pre_words = words[i-1]
    now_words = words[i]
    
    if (pre_words[-1] != now_words[0]) or (now_words in word_set):
        print('No')
        break
    else:
        word_set.add(now_words)
        
else:
    print('Yes')