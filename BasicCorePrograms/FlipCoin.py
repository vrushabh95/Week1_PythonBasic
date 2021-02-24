import random

def flipcoin(flip_coin):
    head = 0
    tails = 0
    i = 0
    while i < flip_coin:
        if random.random() < 0.5:
            tails += 1
        else:
            head += 1
        i = i + 1
    print("percentage of head is :", round((head * 100) / flip_coin,  2))
    print("percentage of tail is :", round((tails * 100) / flip_coin, 2))

flip_coin = int(input("Enter the number of times to flip coin\n"))
flipcoin(flip_coin)

