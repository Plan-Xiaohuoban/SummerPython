class Student(object):
    # 定义构造方法
    def __init__(self, n, a, m, h):
        # 设置属性
        self.name = n
        self.age = a
        self.major = m
        self.hobby = h

    # 定义类方法
    def introduce(self):
        print("我叫%s，%d岁，来自%s系，喜欢%s。" % (self.name, self.age, self.major, self.hobby))

    def get_GPA(self):
        return "无可奉告"


class Freshman(Student):
    def __init__(self, n, a, m, h):
        super().__init__(n, a, m, h)

    @property
    def calculus(self):
        return self.__calculus

    @calculus.setter
    def calculus(self, value):
        if not isinstance(value, int):
            raise ValueError("score mush be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")
        self.__calculus = value


class Sophomore(Student):
    def __init__(self, n, a, m, h):
        super().__init__(n, a, m, h)
        self.dest = ""

    def find_destination(self, dest):
        self.dest = dest

    def introduce(self):
        super().introduce()
        if self.dest != "":
            print("我的志向是做%s。\n" % (self.dest))
        else:
            print("我暂时还没有找到方向。\n")


def play_with_grade_1():
    print("-" * 30)
    # 实例化对象
    John = Freshman("张约翰", 19, "化学", "唱")
    John.introduce()  # 调用父类的方法
    Ming = Freshman("李小明", 21, "机械", "跳")
    Ming.introduce()
    print("{0}的GPA是……{1}".format(Ming.name, Ming.get_GPA()))
    John.calculus = 80
    Ming.calculus = 70
    print(f"{John.name}的微积分成绩是：{John.calculus}")


def play_with_grade_2():
    print("-" * 30)
    Jim = Sophomore("李小明", 22, "电子", "RAP")
    Jim.introduce()
    Jim.find_destination("天线")
    Jim.introduce()


if __name__ == "__main__":
    play_with_grade_1()
    play_with_grade_2()

