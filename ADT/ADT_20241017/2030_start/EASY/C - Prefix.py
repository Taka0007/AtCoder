# Problem link    : https://atcoder.jp/contests/adt_easy_20241017_3/tasks/abc268_b
# Submission link : https://atcoder.jp/contests/adt_easy_20241017_3/submissions/59021458

# input
S = input()
T = input()
# make prefix set
prefix_set = set()
prefix_str = ""
for i in range(len(T)):
    prefix_str += T[i]
    prefix_set.add(prefix_str)
# judge
if S in prefix_set:
    ans = "Yes"
else:
    ans = "No"
# output
print(ans)
