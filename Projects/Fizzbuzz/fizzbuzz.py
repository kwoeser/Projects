# Karma Woeser
# Fizzbuzz


def fb(n):
    '''
    Explaination: If i is divided by 3 and the remanider is 0 the it will be print fizz.
    If i is divided by 5 and the remanider is 0 the it will be print buzz.
    If i can be diveded by 3 and 5 and the remainder for both is 0 then it will be print fizzbuzz.
    If it can't do any of the above it will just print i (the number).

    Parameters: n (int)

    Returns: None


    >>> fb(1)
    1
    Game Over!

    >>> fb(0.5)
    Invalid Error
    '''

    x = isinstance(n, (int))
    if x:
        for i in range(1, n+1):
            if i % 3 == 0 and  i % 5 == 0:
                print('fizzbuzz')

            elif i % 3 == 0:
                print('fizz')

            elif i % 5 == 0:
                print('buzz')

            else:
                print(i)
                                    
        print('Game Over!')
        return None

    else:
        print("Invalid Error")


#fb(15)




