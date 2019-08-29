
def calculation(max_len):
    solutions = [[x, y, z]
                 for x in range(5, max_len)
                 for y in range(4, max_len)
                 for z in range(3, max_len)
                 if (x*x==y*y+z*z)]
    return "The longest side possible is " + str(max(max(solutions)))

