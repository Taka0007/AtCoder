# import
import itertools
# input & declare variables
S = input()
substr_set = set()
# output
for i in range(1,len(S)+1):
    for j in itertools.combinations(S,i):
        substr_set.add("".join(j))
print(substr_set)