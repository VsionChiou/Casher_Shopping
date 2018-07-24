Goods = {'饮料': 3, '矿泉水': 1, '面包': 4, '可乐': 3.5, '冰淇凌': 5}
goodsNow = [];
His = [];


salary = int(input("请输入你的工资："))
i=1
for goods in Goods.items():
    print(i,goods)
    goodsNow.append(goods);
    i +=1;

Salary = 0
while Salary < salary:
    Item = int(input("请输入你要购买的商品编号："))
    if Item >0:
        His.append(goodsNow[Item-1])
        salary=salary-goodsNow[Item-1][1];
    if Item==0:
        break
if salary>=0:
    pass
elif salary<0:
    salary = salary + His[-1][1]
    print('您的余额不足！')
    His.pop(-1)


print("您购买的商品如下：",His)
print("您的余额还剩：%d元" % salary)

