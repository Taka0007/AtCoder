# input
R,X = map(int,input().split())
# output
if X == 1:
    if R >= 1600 and R <= 2999:
        ans = "Yes"
    else:
        ans = "No"
elif X == 2:
    if R >= 1200 and R <= 2399:
        ans = "Yes"
    else:
        ans = "No"
print(ans)