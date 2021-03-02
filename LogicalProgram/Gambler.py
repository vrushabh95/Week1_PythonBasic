import random


class Gambler:
    stake = 0
    GOAL = 0
    trials = 0

    def __init__(self, stakeAmount,goal,trials):
        self.stake = stakeAmount
        self.GOAL = goal
        self.trials = trials
    def playGame(self):
        """
        function to play gambler game
        """
        BET_AMOUNT=1
        bets = 0
        win = 0
        loss=0
        result = 0
        cash=0
        for i in range(self.trials):
            cash=self.stake
            #loop continue till stake amount goes to 0 or stake amount reaches the goal
            while cash > 0 or cash == self.GOAL:
                bets += 1  #increments bet by 1
                result = random.randint(0,1)
                if result == 1:
                    cash += BET_AMOUNT
                    win += 1
                else:
                    cash -= BET_AMOUNT
                    loss += 1

        print("No of times games won=", win)
        print("No of times games lost=", loss)
        print("Percentage of game won=", 100 * win / trials) #calculates winning percentage
        print("Percentage of game lost=", 100 * loss / trials) #calculates loss percentage


value=1
#infinte loop
while value == 1:
    try:
        print("WELCOME TO GAMBLER GAME")
        stakeAmount = (int(input("Enter the stake amount ")))
        goal = (int(input("Enter the goal amount ")))
        trials = (int(input("Enter the how many times you want to play game ")))
        if stakeAmount > 0 and goal > 0 and trials > 0:
            game = Gambler(stakeAmount,goal,trials)
            game.playGame()
            break #break the loop if all the input given by user is correct
    except:
        print("Please enter the amount in numbers ")