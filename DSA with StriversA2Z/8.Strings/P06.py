def beautySum(s):
    answer =0
    n = len(s)
    for i in range(n):
        freq = [0]*26
        Max = 0
        for j in range(i,n):
            index = ord(s[j])-ord('a')
            freq[index]+=1
            if freq[index]>Max:
                Max=freq[index]
            Min = Max
            for count in freq:
                if count>0 and count<Min:
                   Min=count
            answer += Max-Min
    return answer
s = "xyx"
print(beautySum(s))
    
