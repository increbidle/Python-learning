"""在数学上，斐波那契数列以如下被以递推的方法定义：
F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N*）"""


def sum1(i):
    def finb(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    else:
        return finb(n-1)+finb(n-2) 