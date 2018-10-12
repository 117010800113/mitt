tempstr=input("")
if tempstr[-1]in ['F','f']:
    c=(eval(tempstr[0:-1])-32)/1.8
    print("{:.0f}C".format(c))
elif tempstr[-1] in ['C','c']:
    f=1.8*eval(temputr[0:-1])+32
    print("{:.0f}F".format(f))
else:
    print("wrong")
