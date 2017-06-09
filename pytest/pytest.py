class Calculator:       #首字母要大写，冒号不能缺
    name = 'Good Calculator'  #该行为class的属性
    price = 18
    def __init__(self, name, price, height, width, weight):  # 注意，这里的下划线是双下划线
        self.name = name
        self.price = price
        self.h = height
        self.wi = width
        self.we = weight
    def add(self, x, y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self, x, y):
        result=x-y
        print(result)
    def times(self, x, y):
        print(x*y)
    def divide(self, x, y):
        print(x/y)
c = Calculator()
c.times(12, 13)
