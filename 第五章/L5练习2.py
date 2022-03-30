"""求N的阶乘，N由键盘输入"""
N=int(input("计算N的阶乘"))#如果不强制转换的话下面的range函数会报错
multliply=1
for i in range(1,(N+1)):    #start从0开始，记得里面用的是逗号不是分号切片
    multliply=multliply*i
    i+=1
print(multliply)
