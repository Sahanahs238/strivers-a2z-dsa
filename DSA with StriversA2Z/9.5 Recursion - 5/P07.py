def addOperators(s,target):
    res=[]
    def backtrack(index,exp,value,last):
        if index == len(s):
            if value == target :
                res.append(exp)
                return 
        for i in range(index,len(s)):
            part = s[index:i+1]
            if len(part)>0 and part[0]=="0":
                break
            n = int(part)
            if index ==0:
                backtrack(i+1,part,n,n)
            else:
                backtrack(i+1,exp+"+"+part,value+n,n)
                backtrack(i+1,exp+"-"+part,value-n,-n)
                backtrack(i+1,exp+"*"+part,value-last+last*n,last*n)
    backtrack(0,"",0,0)
    return res
s= "123"
target = 6
print(addOperators(s,target))
    