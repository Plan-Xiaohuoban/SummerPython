

class Student:
    """
    定义Student类
    内部命名空间
    """
    hobby=""

    def __init__(self, n, a, m, h):
        """
        __init__方法：构造函数，可以在创建实例的时候，绑定一些属性。
        self参数：每一个函数前__init__方法的第一个参数永远是self，表示创建的实例对象本身。
        类的属性：以下四个变量都称为“类的属性”
        """
        self.name = n
        self.age = a
        self.major = m
        self.hobby = h

    def run(self):
        print("{} 在跑阿甘！".format(self.name))

    def introduce(self):
        """
        类的方法：在Student类的内部，定义一个introduce方法（函数）。这称之为“类的方法”。
        self参数：本方法的功能是输出一段自我介绍，需要访问“类的属性”，所以必须要有self参数。
        """
        print("我叫%s，%d岁，来自%s系，喜欢%s。" % (self.name, self.age, self.major, self.hobby))


# # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数。
# # 注意self不需要传，Python解释器自己会把实例变量传进去。
# John = Student("张约翰", 19, "化学", "唱")  # 创建实例：变量John指向一个Student实例
# Ming = Student("李小明", 21, "机械", "跳")  # 创建实例：变量Ming指向另一个Student实例

# # 实例是根据类创建出来的一个个具体的“对象”
# # 每个对象都拥有相同的方法，但各自的数据可能不同
# John.introduce()
# Ming.introduce()


# # 公有变量与私有变量
# print(John.name)
# print(Ming.hobby)


class Freshman(Student):
    def __init__(self, n, a, m, h):
        super().__init__(n, a, m, h)




# # 实例化对象run
John = Freshman("张约翰", 19, "化学", "唱")
John.introduce()  # 调用父类的方法
John.run()  # 调用父类的方法

# # Ming = Freshman("李小明", 21, "机械", "跳")
# # Ming.introduce()


class Sophomore(Student):
    def __init__(self, n, a, m, h):
        super().__init__(n, a, m, h)
        self.dest = ""

    def find_destination(self, dest):
        self.dest = dest

    def introduce(self):
        if self.dest != "":
            print("我的志向是做%s。\n" % (self.dest))
        else:
            print("我暂时还没有找到方向。\n")



# # print("-" * 30)
Jim = Sophomore("李小明", 22, "电子", "RAP")
Jim.run()
Jim.introduce()
Jim.find_destination("天线")
Jim.introduce()

