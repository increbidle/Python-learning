"""低于或等于10万元时，奖金可提10%
高于10万元，低于20万元时,高于10万元的部分，可提成7.5%
高于20万元的部分，可提成5%
高于40万元的部分，可提成3%
高于60万元的部分，可提成1.5%
超过100万元的部分按1%提成
"""



output=eval(input("当月利润 单位W"))
my_money=0
while output <=10:
    my_money=0.1*output
    break
while 10<output<=20:
    my_money=1+0.075*(output-10)
    break
while 20<output<=40:
    my_money=1+0.75+0.05*(output-20)
    break
while 40<output<=60:
    my_money=1.75+1+0.03*(output-40)
    break
while 60<output<=100:
    my_money=2.75+0.6+0.015*(output-60)
    break
else:
    my_money=2.75+0.6+0.015*40+0.01*(output-100)
print(my_money)
#应该用判断结构！！！我是笨比
