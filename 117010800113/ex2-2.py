m=input("")
if m[-1] in ['Y']:
    Y=(eval(m[0:-1])/6)
    print ("{:.2f}dollar".format(Y))
elif m[-1] in ['dollar']:
    D=(eval(m[0:-1])*6)
    print("{:.2f}Y".format(D))
