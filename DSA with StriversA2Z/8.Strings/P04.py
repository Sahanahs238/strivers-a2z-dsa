def myAtoi(input):
        # Your code goes here
    INT_MAX,INT_MIN=2**31-1,-2**31
    n = len(input)
    i =0 
    res= 0
    sign =1
    while i<n and input[i] == " ":
        i+=1
    if i<n:
        if input[i] == "-":
            sign = -1
            i+=1
        elif  input[i] == "+":
            i+=1
    while i<n and input[i].isdigit():
        digit = int(input[i])
        if res > (INT_MAX-digit)//10:
            return INT_MAX if sign ==1 else INT_MIN 
        res = (res*10)+digit
        i+=1
    return sign*res
input= " +004500abc"
print(myAtoi(input))


