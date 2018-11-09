def isNum(s):
    try:
        n=eval(s)
    except:
        return False
    return True
s=input()
print(isNum(s))
                        
