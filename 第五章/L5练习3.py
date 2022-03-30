"""使用for循环打印乘法口诀表"""
h=0#行
l=0#列
mul=1#乘积
end_list=0#下面删除多余元素时，删除到列表的前几位
list=[[0 for i in range(9)]for j in range(9)]#创建一个9行9列的二维列表
for h in range(0,9):#外历遍循环行
    for l in range(0,9):#内历遍循环列
        if h>=l:#去掉重复部分
            mul=(h+1)*(l+1)#因为是从0开始，所以要加1
            list[h][l]="{0:d}X{1:d}={2:<2d}".format(l+1,h+1,mul)#能想到format传递参数,挺难的
        l=l+1
    h=h+1
for x in range(9):
    for y in range(8,end_list,-1):
        del list[x][y]#删除列表中的0
    end_list+=1
  #  print(list[x])
for x in range(9):
    for y in range(x+1):
        print(list[x][y],end=" ")
    print("")#换行