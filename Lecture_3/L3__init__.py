class Hero:  # 定义 Hero 类

    # 构造方法
    def __init__(self, name, level):  
        self.name = name 
        self.__level = level 

    def GANK(self):  # 定义 Hero 类的GANK方法
        print("{} 级的 {} 前来支援！".format(self.__level, self.name))

    def use_skill(self, number):  # 定义 Hero 类的 use_skill 方法
        print("{} 级的 {} 使用了 {} 技能".format(self.__level, self.name, number))


a = Hero("Batman", 12)     # 对象 a 是 Hero 类的一个实例
b = Hero("Superman", 13)  # 对象 b 也是 Hero 类的一个实例
c = Hero("Spiderman", 15)  # 对象 c 也是 Hero 类的一个实例

# 调用类的方法
a.set_info("Batman", 12)
b.set_info("Superman", 13)
c.set_info("Spiderman", 15)
a.use_skill(1)
b.use_skill(2)
c.use_skill(3)


# print("Name = {}".format(a.name))  # 公有变量，可以在类外面直接访问
# print("Level = {}".format(a.__level))  # 私有变量，不可以在类外面直接访问

