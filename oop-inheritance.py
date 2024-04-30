# 定義一個父類 Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# 定義一個子類 Dog，繼承自 Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# 定義一個子類 Cat，繼承自 Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"

# 創建一個 Dog 對象
dog = Dog("Buddy")
print(dog.name)  # 訪問父類屬性
print(dog.speak())  # 調用子類方法

# 創建一個 Cat 對象
cat = Cat("Kitty")
print(cat.name)  # 訪問父類屬性
print(cat.speak())  # 調用子類方法