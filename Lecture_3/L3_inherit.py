class Hero:  # 定义 Hero 类

    # 构造方法
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def GANK(self):  # 定义 Hero 类的GANK方法
        print("{} 级的 {} 前来支援！".format(self.level, self.name))

    def use_skill(self, number):  # 定义 Hero 类的 use_skill 方法
        print("{} 级的 {} 使用了 {} 技能".format(self.level, self.name, number))




class Libai(Hero):
    """
    Libai是Hero的子类，Hero是Libai的父类（也称基类、超类）。
    继承的好处：子类获得了父类的全部功能。并能根据自己的需求覆盖父类的方法，或者扩展出新的方法。
    """

    def __init__(self, name, level):
        super().__init__(name, level)  # 调用父类（Hero类）的构造函数

    def use_skill(self, number):  # 覆盖父类的方法
        skill_list = {1: "将进酒", 2: "神来之笔", 3: "青莲剑歌"}
        if number in [1, 2, 3]:
            print(
                "{} 级的 {} 使用了 {} 技能：{}".format(
                    self.level, self.name, number, skill_list[number]
                )
            )





class Hanxin(Hero):  # Hanxin是Hero的子类，Hero是Hanxin的父类
    def __init__(self, name, level):
        super().__init__(name, level)  # 调用父类（Hero类）的构造函数

    def use_skill(self, number):  # 覆盖父类的方法
        skill_list = {1: "无情冲锋", 2: "背水一战", 3: "国士无双"}
        if number in [1, 2, 3]:
            print(
                "{} 级的 {} 使用了 {} 技能：{}".format(
                    self.level, self.name, number, skill_list[number]
                )
            )

    def StealTower(self):  # 扩展出新的方法
        print("{} 级的 {} 在偷塔!".format(self.level, self.name))




class BaiLongYin(Hanxin):
    """
    BaiLongYin是Hanxin的子类，Hanxin是BaiLongYin的父类
    """

    def __init__(self, name, level, price):
        super().__init__(name, level)  # 调用父类（Hanxin类）的构造函数
        self.price = price  # 另外绑定price属性

    def StealTower(self):  # 覆盖父类的方法
        print("{0} 级的价格 {2} 的 {1} 在偷塔!".format(self.level, self.name, self.price))




# # 以上是“继承”。更进一步，理解“多态”的好处
# # 对不同类型的实例进行相同的操作，得到不同的结果
def show(hero):
    hero.use_skill(2)
    hero.GANK()






if __name__ == "__main__":
    h = Hero("李白", 13)  # 变量 h 是一个实例对象，把 Hero 类实例化了
    h.GANK()  # 调用类方法
    h.use_skill(3)  # 调用类方法，传入self之外的参数

        
    h = Hanxin("韩信", 15)
    h.GANK()  # 注意到，Hanxin类中并没有定义GANK函数
    h.use_skill(3)
    h.StealTower()

    print("-" * 30)

    l = Libai("李白", 13)
    l.GANK()
    l.use_skill(3)

    print("-" * 30)

    b = BaiLongYin("白龙吟", 15, 1188)

    b.GANK()
    b.use_skill(3)
    b.StealTower()
    print("-" * 30)

    l = Libai("李白", 13)
    h = Hanxin("韩信", 4)
    b = BaiLongYin("白龙吟", 15, 1188)
    show(l)
    show(h)
    show(b)


    print("-" * 30)


# if __name__ == "__main__":
#     pass


#     b = BaiLongYin("白龙吟", 15, 1188)
#     b.GANK()
#     b.use_skill(3)
#     b.StealTower()
#     print("-" * 30)

