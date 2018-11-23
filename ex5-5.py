def isPrime(n):
    for k in range(2,n):
        if n%k ==0:
            return False
    return True
while True:
    try:
        n = eval(input("请输入一个整数:"))
    except:
        print("输入错误")
        continue
    
    if type(n) is not int:
        print("请输入一个整数: ")
        continue
    if n == -1:
        break        
if isPrime(n):
    print("{} is prime.".format(n))
else:
    print("{} is not prime.".format(n))
       
        
