def multi(*a):
    if len(a) == 0:
        return 0
    t = 1
    for i in a:
        t = t * i
    return t
print( multi())
