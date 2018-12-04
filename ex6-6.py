import jieba
excludes={"什么","一个","我们","你们","告诉","咱们","如今","就是","东西","这样","进来","说道","知道","姑娘","不知","起来","这里","出来","众人","那里","自己","一面","只见","两个","没有","怎么","不是","这个","听见"}
          
txt = open('红楼梦.txt','r', encoding='GB18030').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word =="老太太":
        rword="贾母"
    elif word =="太太":
        rword="王夫人"
    else:
          rword=word
    counts[rword]=counts.get(rword,0)+1
for word in excludes:
          del(counts[word])
items =list(counts.items())
items.sort(key=lambda x:x[1], reverse =True)
for i in range(10):
    word, count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
