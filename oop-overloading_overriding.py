class MyClass:
    # 方法重載
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    # 方法重寫
    def speak(self):
        print("Dog barks")

# 方法重載的使用
obj = MyClass()
print(obj.add(1, 2))  # 輸出 3
print(obj.add(1, 2, 3))  # 輸出 6

# 方法重寫的使用
dog = Dog()
dog.speak()  # 輸出 "Dog barks"
