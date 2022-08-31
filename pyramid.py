pyramid = ''
x = 1

stars = int(input('How many stars '))

for y in range(stars,-1,-1):
    for i in range(y):
        pyramid += ' '
        if i == y - 1:
            pyramid = pyramid + ' *' * x
            x += 1
    print(pyramid)
    pyramid = ''