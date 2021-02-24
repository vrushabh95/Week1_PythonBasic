import random
a = int(input("Enter the number of times to flip coin\n"))
def flipcoin(value):

    head = 0
    tails = 0
    i = 0
    while i < value:
        toss = random.random()
        if toss < 0.5:
            tails += 1
        else:
            head += 1
            return print("percentage of head is :", round((head * 100) / value,  2)), print("percentage of head is :", round((head * 100) / value , 2))

b = flipcoin(a)
print(b)
