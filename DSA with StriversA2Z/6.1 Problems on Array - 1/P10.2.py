def missing_number(arr):
    return (len(arr)*(len(arr)+1))//2 - sum(arr)
arr = list(map(int,input().split()))
print(missing_number(arr))