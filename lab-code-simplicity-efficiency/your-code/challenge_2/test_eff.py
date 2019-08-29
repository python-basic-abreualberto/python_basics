

import random

import random_str as ranst

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

    def batch_str_gen(n, a=8, b=12):
        r = [(random.choice(range(a, b))) if (a < b) else c for i in range(n)]
        r.append(ranst.rand_str_gen(c))
        print(r)