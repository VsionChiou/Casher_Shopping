Goods = {'饮料': 3, '矿泉水': 1, '面包': 4, '可乐': 3.5, '冰淇凌': 5}
goodsNow = [];
His = [];


def register():
    loginlog = open("cache/login.log", 'a')
    id = int(input("请输入你的自定义ID（限6位）："))
    pswd = int(input("请输入密码(仅数字！)："))
    loginlog.write("%s\n" % id)
    loginlog.write("%s\n\n" % pswd)
    loginlog.close()
    print("注册成功！")

def login():
    loginlog=open('cache/login.log','r')
    id = input("请输入你的自定义ID（限6位）：")
    pswd = int(input("请输入密码："))
    for line in loginlog:
        if id in line:
            f_password=loginlog.readline()
            password=int(f_password)

            if pswd==password:
                print("登录成功！")
                System()
            else :
                print("密码有误，请重新输入。")
                login()
        else:
            print("无此ID，请注册。。。")
            register()

    loginlog.close()

def System():
    salary = int(input("请输入你的工资："))
    i = 1
    for goods in Goods.items():
        print(i, goods)
        goodsNow.append(goods);
        i += 1;

    Salary = 0
    while Salary < salary:
        Item = int(input("请输入你要购买的商品编号："))
        if Item > 0:
            His.append(goodsNow[Item - 1])
            salary = salary - goodsNow[Item - 1][1];
        if Item == 0:
            break
    if salary >= 0:
        pass
    elif salary < 0:
        salary = salary + His[-1][1]
        print('您的余额不足！')
        His.pop(-1)

    print("您购买的商品如下：", His)
    print("您的余额还剩：%d元" % salary)

main=int(input('请输入操作：1.登录，2.注册'))

if main==1:
    login()



if main==2:
    register()

    while(1):
        choose=input("是否要登录呢？ y/n")
        if choose=='y' or 'yes':
            login()
        elif choose=='n' or 'no':
            exit()
        else:
            print("输入错误！")





