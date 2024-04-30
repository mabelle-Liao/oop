class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 定義一個函數，接收一個動物對象並調用它的 speak 方法
def make_sound(animal):
    return animal.speak()

# 創建一個 Dog 對象
dog = Dog()
# 創建一個 Cat 對象
cat = Cat()

# 調用函數並傳入不同的動物對象
print(make_sound(dog))  # 輸出 "Woof!"
print(make_sound(cat))  # 輸出 "Meow!"