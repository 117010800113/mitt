import time
scale=10
print("------starting-----")
for i in range (scale+1):
    a,b='**'*i,'..'*(scale-i)
    c=(i/scale)*100
    print("\rstarting{:3.0f}%[{}->{}]Done".format(c,a,b))
    time.sleep(0.1)
print("-----Done----")
