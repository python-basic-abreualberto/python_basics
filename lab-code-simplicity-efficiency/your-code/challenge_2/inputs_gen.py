def inputs_gen():
    import sys
    a = int(input('Enter minimum string length: '))
    b = int(input('Enter maximum string length: '))
    n = int(input('How many random strings to generate? '))

    if (a < 1 or
        a > b or
        n < 1):
        sys.exit('Incorrect min and max string lengths. Try again.')

    return int(a),int(b),int(n)

