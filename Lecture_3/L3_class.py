class Hero:  # 定义 Hero 类

    name = ""  # name 属性，默认为公有变量
    __level = 45  # 两个下划线作为前缀，表示私有变量

    def set_info(self, name, level):
        self.name = name  # 给对象的 name 属性赋值
        self.__level = level  # 给对象的 __level 属性赋值

    def GANK(self):  # 定义 Hero 类的GANK方法
        print("{} 级的 {} 前来支援！".format(self.__level, self.name))

    def use_skill(self, number):  # 定义 Hero 类的 use_skill 方法
        print("{} 级的 {} 使用了 {} 技能".format(self.__level, self.name, number))


        





a = Hero()  # 对象 a 是 Hero 类的一个实例
b = Hero()  # 对象 b 也是 Hero 类的一个实例
c = Hero()  # 对象 c 也是 Hero 类的一个实例


# print(type(a.GANK))



# 调用类的方法
a.set_info("Batman", 12)
b.set_info("Superman", 13)
c.set_info("Spiderman", 15)

a.GANK()



a.use_skill(1)
b.use_skill(2)
c.use_skill(3)

# print("-" * 30)
# print(type(a))  # 类型相同
# print(type(b))
# print(type(c))

# print("-" * 30)
# print(id(a))  # id不一样
# print(id(b))
# print(id(c))

# print("-" * 30)
# # print(a)  # id不一样
# # print(b)
# # print(c)



# # 访问变量
# print("Name = {}".format(a.name))  # 公有变量，可以在类外面直接访问
# a.name = "Hanxin"
# a.GANK()

# print("Level = {}".format(a.__level))  # 私有变量，不可以在类外面直接访问

