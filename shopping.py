Goods = {'饮料': 3, '矿泉水': 1, '面包': 4, '可乐': 3.5, '冰淇凌': 5}
goodsNow = [];
His = [];


class Account(object):

    # loginlog = open("cache/login.log")

    def __init__(self,id,pswd,salary):
        self.id = id
        self.pswd = pswd
        self.salary = salary

    def register(self):
        loginlog = open("cache/login.log", 'a')
        # id = int(input("请输入你的自定义ID（限6位）："))
        # pswd = int(input("请输入密码(仅数字！)："))
        loginlog.write("%s\n" % self.id)
        loginlog.write("%s\n\n" % self.pswd)

        loginlog.close()
        print("注册成功！")
        # return loginlog

    def login(self):

        loginlog = open('cache/login.log','r')
        # id = input("请输入你的自定义ID（限6位）：")
        # pswd = int(input("请输入密码："))
        for line in loginlog:
            if self.id in line:
                f_password=loginlog.readline()
                password=int(f_password)

                if self.pswd==password:
                    print("登录成功！")

                    mysystem = system()
                    mysystem.System()
                    break
                else :
                    print("密码有误，请重新输入。")
                    self.login()

            '''
            else:
                print("无此ID，请注册。。。")
                self.register()
                '''
        loginlog.close()
        # return loginlog


    def Balance(self):
        return self.salary


class system(object):

    def System(self):
        # salary = int(input("请输入你的工资："))
        # Account.salary

        i = 1
        for goods in Goods.items():
            print(i, goods)
            goodsNow.append(goods);
            i += 1;

        Salary = 0
        while Salary < myaccount.salary:
            Item = int(input("请输入你要购买的商品编号："))
            if Item > 0:
                His.append(goodsNow[Item - 1])
                myaccount.salary = myaccount.salary - goodsNow[Item - 1][1];
            if Item == 0:
                break
        if myaccount.salary >= 0:
            pass
        elif myaccount.salary < 0:
            myaccount.salary = myaccount.salary + His[-1][1]
            print('您的余额不足！')
            His.pop(-1)

        print("您购买的商品如下：", His)
        print("您的余额还剩：%d元" % myaccount.salary)


main = int(input('请输入操作：1.登录，2.注册'))

id = input("请输入你的自定义ID（限6位）：")
pswd = int(input("请输入密码："))
salary = int(input("请输入你的工资："))

myaccount = Account(id, pswd, salary)

if main == 1:
    myaccount.login()


if main == 2:
    myaccount.register()

    while(1):
        choose = input("是否要登录呢？ y/n")

        if choose == "y" and "yes":
            myaccount.login()
        elif choose == "n" and "no":
            exit()
        else:
            print("输入错误！")



