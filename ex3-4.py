import math
Tempstr=input("")
if Tempstr[0] in Tempstr[-1]:
    if Tempstr[1] in Tempstr[-2]:
        print("yes")
    else:
        print("no")
else:
    print("no")
