def inputs_calc():

    print('Welcome to this calculator!')
    print('It can add and subtract whole numbers from zero to five')

    numbers = ['zero','one','two','three','four','five']
    operator = ['plus', 'minus']

    a = input('Please choose your first number (zero to five): ')
    b = input('What do you want to do? plus or minus: ')
    c = input('Please choose your second number (zero to five): ')

    if (a in numbers or
        b in numbers or
          c in operator):
            return [a,b,c]

    return print('I am not able to answer this question. Check your input.')

