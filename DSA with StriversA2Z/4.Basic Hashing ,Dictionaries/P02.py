s = input("Enter a string:")
hash_s = [0]*26
for char in s:
    hash_s[ord(char)-ord('a')]+=1
q = int(input("enter :"))
while q>0:
    char = input("enter char:")
    print(hash_s[ord(char)-ord('a')])