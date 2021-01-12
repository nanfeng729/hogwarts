# 定义计算器类

class calculator:
    # 定义加法
    def add(self, a, b):
        return a + b

    # 定义减法
    def sub(self, a, b):
        return a - b

    # 定义乘法
    def mul(self, a, b):
        return a * b

    # 定义除法
    def div(selfa, a, b):
        if b == 0:
            return '除数不能为0'
        else:
            return a / b
