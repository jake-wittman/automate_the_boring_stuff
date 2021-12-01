supplies = ['food', 'water', 'flamethrower', 'candles']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

spam = ['cat', 'rat', 'dog', 'moose']
spam.sort()
spam
