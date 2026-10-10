def letterCombinations(digits):
    if not digits:
        return []
    cur = []
    res =[]
    letters ={
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz" }
    def backtrack(i):
        if i == len(digits):
            res.append("".join(cur))
            return
        digit = digits[i]
        for letter in letters[digit]:
            cur.append(letter)
            backtrack(i+1)
            cur.pop()
    backtrack(0)
    return res
digits = "23"
print(letterCombinations(digits))