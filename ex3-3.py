import math
dayup=1.0
for i in range(365):
    if i%10 in [4,5,6,7]:
        dayup=dayup*(1+0.01)
    else:
        dayup=dayup
print("{:.2f}.".format(dayup))
