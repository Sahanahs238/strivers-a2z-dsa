def countSubstrings(s):
        # Your code goes here
    answer = 0
    n = len(s)
    for i in range(n):
        freq = [0]*26
        for j in range(i,n):
            index = ord(s[j])-ord('a')
            freq[index]+=1

            odd=0
            for count in freq:
                if count%2==1:
                    odd+=1
            if odd <= 1:
                answer +=1
    return answer
s="aba"
print(countSubstrings(s))