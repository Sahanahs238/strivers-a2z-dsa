def longestPalindrome(s):
    best_left,best_right=0,0
    def expand_from_centre(left,right):
        while left >=0 and right <len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return left+1,right-1
    for i in range(len(s)):
        l1,r1=expand_from_centre(i,i)
        l2,r2=expand_from_centre(i,i+1)
        if (r1-l1)>(best_right-best_left):
            best_right,best_left=r1,l1
        elif (r2-l2)>(best_right-best_left):
            best_right,best_left=r2,l2
    return s[best_left:best_right+1]
s = "babad"
print(longestPalindrome(s))