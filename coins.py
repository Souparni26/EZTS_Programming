total_amount = 18
coins = [1, 5, 7]
coins.sort(reverse=True)
num_coins = 0
amount_remaining = total_amount
for coin in coins:
    while amount_remaining >= coin:
        amount_remaining -= coin
        num_coins += 1
if amount_remaining == 0:
    print("Minimum number of coins required:", num_coins)
else:
    print("It is not possible to form the total amount with the given coins")
        





