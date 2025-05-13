# 排序(从大到小)
d={"apple":10,"wy":6,"banana":5,"cherry":20}
for i in d.keys():
    for j in d.keys():
        if d[i]>d[j]:
            t=d[i]
            d[i]=d[j]
            d[j]=t

#返回列表，每个元素是一个元组（键，值）
a=[(i,d[i]) for i in d.keys()]
print(a)