"""
#1、自己写一个面向对象的例子：

比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）

创建子类【猫】，继承【动物类】，

复写父类的__init__方法，继承父类的属性，

添加一个新的属性，毛发=短毛，

添加一个新的方法， 会捉老鼠，

复写父类的‘【会叫】的方法，改成【喵喵叫】

创建子类【狗】，继承【动物类】，

复写父类的__init__方法，继承父类的属性，

添加一个新的属性，毛发=长毛，

添加一个新的方法， 会看家，

复写父类的【会叫】的方法，改成【汪汪叫】

调用 name== ‘main’：

创建一个猫猫实例

调用捉老鼠的方法

打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。

创建一个狗狗实例

调用【会看家】的方法

打印【狗狗的姓名，颜色，年龄，性别，毛发】。

2、将数据配置到yaml文件里
"""

import yaml


class Animal:
    # name=None
    # color=None
    # age=1
    # sex='male'
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def jiao(self):
        print("叫一下")

    def run(self):
        print("会跑")


class cat(Animal):
    # cat_hair="short hair"
    def __init__(self, name, color, age, sex, cat_hair):
        self.cat_hair = cat_hair
        super().__init__(name, color, age, sex)

    def catch_mouse(self):
        print("捉到了老鼠")

    def jiao(self):
        print("喵喵叫")


class dog(Animal):
    # dog_hair=None
    def __init__(self, name, color, age, sex, dog_hair):
        self.dog_hair = dog_hair
        super().__init__(name, color, age, sex)

    def home(self):
        print("会看家")

    def jiao(self):
        print("汪汪叫")


if __name__ == '__main__':
    with open("data.yml", encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
        # print(datas['cat'])
    cat_name = datas['cat']['name']
    cat_color = datas['cat']['color']
    cat_age = datas['cat']['age']
    cat_sex = datas['cat']['sex']
    cat_hair = datas['cat']['hair']
    dog_name = datas['dog']['name']
    dog_color = datas['dog']['color']
    dog_age = datas['dog']['age']
    dog_sex = datas['dog']['sex']
    dog_hair = datas['dog']['hair']
    # print(name)
    # print(color)

    catsl = cat(cat_name, cat_color, cat_age, cat_sex, cat_hair)
    print(catsl.name, catsl.color, catsl.age, catsl.sex, catsl.cat_hair)
    catsl.catch_mouse()
    #
    dogs = dog(dog_name, dog_color, dog_age, dog_sex, dog_hair)
    print(dogs.name, dogs.color, dogs.age, dogs.sex, dogs.dog_hair)
    dogs.jiao()
