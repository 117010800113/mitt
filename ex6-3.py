def M (nlist):
    nset=set(nlist)
    if len(nlist)>len(nset):
        return True
    return False
list1=[1,2,3,4,5,6]
if M(list1):
    print("有重复元素")
else:
    print("没有重复元素")
