memo = [-1 for i in range(0, 100)]
a = [2,4,2,5,3,7,4,8]

def lis(i):
    if(memo[i]!=-1):return memo[i]
    memo[i]=1
    for j in range(0, i):
        if(a[j]<=a[i]):memo[i] = max(memo[i], lis(j)+1)
    return memo[i]
print(lis(7))