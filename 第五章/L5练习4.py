"""二分法查找列表中元素位置"""


list=[1,4,9,89,898,6666]
flag_start=0#定义左边
flag_end=len(list)#定义右边
mid=(flag_start+flag_end)//2#中间
key=4#需要索引的量

while list[mid]<=key:#最外层循环，这里先确定key在整个区间的前半部分还是后半部分，还是正好在中间。
    #这里是key在左半部分执行
    if list[mid] == key:#正好在中间的情况
        break
    else:
        flag_start=mid
        mid=(flag_start+flag_end)//2#把左端点缩短到一半位置，再次定义中心以判断key在做还是右
    #这里是key在mid右半部分的情况
else:
    flag_end=mid
    mid=(flag_start+flag_end)//2

print("in list[{:d}]".format(mid),"key=",list[mid])