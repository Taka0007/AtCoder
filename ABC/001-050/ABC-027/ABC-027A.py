num = list(map(int,input().split()))

ans = sum(set(num))*2 - sum(num)
print(abs(ans))

'''
---------------
少し雑に作りすぎたかも
特に最後のabsかぶせたとことか雑の極み

'''
