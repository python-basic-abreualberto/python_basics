import random as r
import sys

import random_str as ranst
import random

def batch_str_gen(n, a=8, b=12):
    import random
    r = []
    for i in range(n):
        if a < b:
            c = random.choice(range(a, b))
        else:
            c=a
        r.append(ranst.rand_str_gen(c))
    print(r)

