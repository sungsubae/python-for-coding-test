# changed user email
n = 1260
coins = [500, 100, 50, 10]
count = 0
for c in coins:
    count += n // c
    n %= c
print(count)
