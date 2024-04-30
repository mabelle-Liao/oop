from abc import ABC, abstractmethod

# 定義一個抽象類 Animal
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def move(self):
        print("Moving...")

# 定義一個介面 Flyable
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

# 定義一個子類 Dog，繼承自 Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# 定義一個子類 Bird，繼承自 Animal，同時實現了 Flyable 介面
class Bird(Animal, Flyable):
    def speak(self):
        return "Chirp!"

    def fly(self):
        print("Flying...")

# 創建一個 Dog 對象
dog = Dog()
print(dog.speak())  # 輸出 "Woof!"
dog.move()  # 輸出 "Moving..."

# 創建一個 Bird 對象
bird = Bird()
print(bird.speak())  # 輸出 "Chirp!"
bird.move()  # 輸出 "Moving..."
bird.fly()  # 輸出 "Flying..."
