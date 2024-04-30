
import random

def random_true(probability=0.95):
    """Returns True with a probability of probability (default 0.95)."""
    return random.random() < probability

#stake amount to begin with
stake = 50

#This accumulator variable will hold the net profit
#once the profit limit is exceeded
accumulator = 0

#Once the stake compounds to this limit it is transferred
#to the accumulator
limit = 1000

# the value in the range is just the number of bets made
for i in range(30):
    if stake > limit:
        acc += limit
        stake -= limit

    #there is a 95 percent chance that the bet will be won
    if random_true() == True:

        #the bet is placed with constant odds of 1.6 and
        # a withholding tax of 5.3% is assumed.
        stake *= 1.6*0.947
    #there is a 5 percent chance that the bet will be lost
    else:
        #In this event, the stake is initialized to 50 and
        #the accumulator is reduced by 50. Essentially, the
        #new stake is obtained from the accumulator.
        stake = 50
        acc -= 50
    
print(stake+acc-50)
