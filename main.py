from __future__ import print_function
from random import randint

#   Flipping individual coin
#   1 -> Heads
#   0 -> Tails
def flipCoin():
    return randint(0,1)

#   Flip an array of coins
def flipNCoins(coinNumber):
    coins = [flipCoin() for coin in range(coinNumber)]
    return coins

#   Flips x number of coins y times, returns array with sum of heads per coin
def flipNTimes(coinNumber, times):
    headsFrec = [0] * coinNumber
    for i in range(times):
        coins = flipNCoins(coinNumber)

        #   Adding number of heads per time flipped
        for j in range(coinNumber):
            headsFrec[j] += coins[j]

    return headsFrec

def runExperiment(coinNumber, flipNumber):
    #   Retrieving number of heads per coin
    headCount = flipNTimes(coinNumber, flipNumber)

    #   Choosing first coin, random coin, and coin with least heads
    c1 = headCount[0]
    c_rand = headCount[randint(0,999)]
    c_min = min(headCount)

    #   Getting frecuency of heads
    v1 = c1 / float(flipNumber)
    v_rand = c_rand / float(flipNumber)
    v_min = c_min / float(flipNumber)

    return [v1, v_rand, v_min]

def main():
    #   Declaring number of coins to flip and number of flips
    coinNumber = 1000
    flipNumber = 10
    experimentNumber = 100000

    v_sum = [0.0, 0.0, 0.0]

    #   Running multiple experiments
    for i in range(experimentNumber):
        v_dist = runExperiment(coinNumber, flipNumber)

        #   Adding frecuency of heads per experiment
        for j in range(len(v_dist)):
            v_sum[j] += v_dist[j]

    v1_avg = v_sum[0] / experimentNumber
    v_rand_avg = v_sum[1] / experimentNumber
    v_min_avg = v_sum[2] / experimentNumber

    print("Fraction of heads for first coin: ", v1_avg)
    print("---------")
    print("Fraction of heads for random coin: ", v_rand_avg)
    print("---------")
    print("Fraction of heads for coin with least heads: ", v_min_avg)
    print("---------")


if __name__ == '__main__':
    main();
