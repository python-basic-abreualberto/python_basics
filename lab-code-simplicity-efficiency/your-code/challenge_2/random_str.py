def rand_str_gen(l=12):
    import string as st
    import random as r
    alphabet = list(st.ascii_lowercase) + list(st.digits)
    s = ''
    for i in range(l):
        s += r.choice(alphabet)
    return s


