def isRepetitive(nList:list):
    for e in nList:
        if nList.count(e)>1:
            return True
    return False
list1=[1,2,3,4,5,6]
if isRepetitive(list1):
    print("有重复元素")
else:
    print("没有重复元素")
