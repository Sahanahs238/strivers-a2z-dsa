n = int(input("Enter array size: "))
arr = list(map(int,input().split()))
hash_array = [0]*13
for i in range(n):
    hash_array[arr[i]]+=1
q = int(input("Enter how much numbers you want to search:"))
while q>0:
    number = int(input("enter the number to be searched: "))
    print(hash_array[number])
    q-=1