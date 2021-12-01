import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_flips = [random.randint(0, 1) for i in range(100)]
    # Code that checks if there is a streak of 6 heads or tails in a row.
    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))