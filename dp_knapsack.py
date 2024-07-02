def knapsack(max_weight, weights, profits, n):
    
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    
    for i in range(1, n + 1):
        for w in range(max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(profits[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][max_weight]


p = [5, 10, 15, 7, 8, 9, 4]    
w = [1, 3, 5, 4, 1, 3, 2]      
n = len(p)
max_weight = 10                


max_profit = knapsack(max_weight, w, p, n)
print("Maximum Profit:", max_profit)
