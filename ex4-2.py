a=0
b=0
c=0
d=0
n=input("")
for m in n:
    if 'a' <=m <='z' :
        a=a+1
    elif '1' <=m <='9' :
        b=b+1
    elif m==' ':
        c=c+1
    else:
        d=d+1
print("英文字符{}".format(a))
print("数字{}".format(b))
print("空格{}".format(c))
print("其他字符{}".format(d))
