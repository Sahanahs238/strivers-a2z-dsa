def buysellstocks(arr):
    buy = 0
    sell = 1
    profit = 0
    while sell < len(arr):
        if arr[buy]< arr[sell]:
            profit1 =arr[sell]-arr[buy]
            profit = max(profit,profit1)
        else:
            buy = sell 
        sell += 1
    return profit
arr = list(map(int,input().split()))
print(buysellstocks(arr))