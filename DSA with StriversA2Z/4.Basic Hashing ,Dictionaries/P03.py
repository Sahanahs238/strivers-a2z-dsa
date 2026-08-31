n = int(input("Enter size of array:"))
arr = list(map(int,input().split()))
freq = {}
for num in arr:
    freq[num] = freq.get(num,0)+1
q = int(input("Enter no :"))
for _ in range(q):
    num = int(input("enter a num:"))
    print(freq.get(num,0))