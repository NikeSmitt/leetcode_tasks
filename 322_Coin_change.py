from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    spam_cashes = [float("inf")] * (amount + 1)
    spam_cashes[0] = 0
    
    for k in range(1, amount + 1):
        for i in range(len(coins)):
            if k - coins[i] >= 0 and spam_cashes[k - coins[i]] < spam_cashes[k]:
                spam_cashes[k] = spam_cashes[k - coins[i]]
        spam_cashes[k] += 1
    
    result = spam_cashes[-1]
    return result if result < float('inf') else -1


if __name__ == '__main__':
    res = coin_change([1, 2, 5], 11)
    print(res == 3)
    res = coin_change([2], 43)
    print(res == -1)
    res = coin_change([1], 0)
    print(res == 0)
