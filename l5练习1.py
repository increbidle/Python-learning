"""练习将1020转化为二进制数"""
n=1020
left=[]
while n/2!=0:
    left.append(n % 2)#这里容易犯错，先把余数放进表里再对n二次赋值！！！
    n//=2

left.reverse()
if left[0]==0:
    del left[0]      #如果不进行删除第一个的话第一个数有0不好看
for i in range(len(left)):
    print(left[i],end="")
    i+=1
