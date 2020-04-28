def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    list = []
    while coin > 0:
        thisCoin = coinsUsed[coin]
        list.append(thisCoin)
        coin = coin - thisCoin

    return list


if __name__ == "__main__":
    amnt = 63
    clist = [1, 5, 10, 25]
    coinsUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)
    print "Making change for", amnt, "requires"
    print dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins"
    print "They are:"
    print printCoins(coinsUsed, amnt)
