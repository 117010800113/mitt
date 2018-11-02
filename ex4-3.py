a=eval(input(""))
b=eval(input(""))
if (a<b):
    m,n =b,a
else:
    m,n=a,b
r=m%n
while(r!=0):
    m,n=n,r
    r=m%n
print("最大公因数{}".format(n))
print("最小公倍数{}".format(a*b/n))
        
       
