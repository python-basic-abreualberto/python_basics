
def math_operation(lst:list):

    keys= ['minus five','minus four','minus three','minus two','minus one',
           'zero','one','two','three','four','five','six','seven','eight','nine','ten']
    values = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
    STRING_TO_INT = dict(zip(keys, values))
    INT_TO_STRING = dict(zip(values, keys))

    if lst[1] == 'plus':
        result = STRING_TO_INT[lst[0]] + STRING_TO_INT[lst[2]]
    else:
        result = STRING_TO_INT[lst[0]] - STRING_TO_INT[lst[2]]

    return f"{lst[0]} {lst[1]} {lst[2]} equals {INT_TO_STRING[result]}" \
        f"\nThanks for using this calculator, goodbye :)"
