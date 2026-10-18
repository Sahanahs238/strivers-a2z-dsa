def countGoodNumbers(n):
    M = 10**9+7
    def pow(base,exp):
        res = 1
        base %=M
        while exp>0:
            if exp%2==1:
                res = (res*base)%M
            base = (base*base)%M
            exp //= 2
        return res 
    even = (n+1)//2
    odd = n//2
    even_count = pow(5,even)
    odd_count = pow(4,odd)
    return (even_count*odd_count)%M
n = 4
print(countGoodNumbers(n))