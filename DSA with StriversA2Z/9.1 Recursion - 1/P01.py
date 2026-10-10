def pow(x,n):
    def helper(x,n):
        if x==0:
            return 0
        if n==0:
            return 1
        res = helper(x*x,n//2)
        return res *x if n%2==1 else res
    res = helper(x,abs(n))
    return res if n>=0 else 1/res 
x = 2
n = 5
print(pow(x,n))
