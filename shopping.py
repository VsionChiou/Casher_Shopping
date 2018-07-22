Goods = ['饮料','矿泉水','面包','可乐','冰淇凌']
His=[];


salary = int(input("请输入你的工资："))

for i in range(len(Goods)):
    print(i+1,Goods[i])

Salary=0

while Salary<salary:

    BuyItem=int(input("请输入你要购买的商品编号："))
    if BuyItem==1:
        salary=salary-5;
        His.append("饮料");
    elif BuyItem==2:
        salary=salary-1;
        His.append("矿泉水");
    elif BuyItem==3:
        salary=salary-3;
        His.append("面包");
    elif BuyItem==4:
        salary=salary-4;
        His.append("可乐");
    elif BuyItem==5:
        salary=salary-5;
        His.append("冰激凌");
    elif BuyItem>5:
        print("请输入正确的编号！");
    elif BuyItem==0:
        break;
if salary>=0 :
    print("购买的商品：",",".join(His[:]),"余额：",salary);
elif salary<0:
    del His[-1]
    print("购买的商品：",",".join(His[:]));
    print("余额不足，请充值。。。")





