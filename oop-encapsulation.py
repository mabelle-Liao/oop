class Car:
    def __init__(self, brand, model):
        self.brand = brand  # 品牌屬性
        self.model = model  # 型號屬性
        self.__fuel_level = 100  # 油量屬性，使用雙下劃線表示私有屬性

    def drive(self):
        if self.__fuel_level > 0:
            print("Car is driving.")
            self.__fuel_level -= 10
        else:
            print("No fuel. Please refuel.")

    def refuel(self):
        self.__fuel_level = 100
        print("Car refueled.")

    def get_fuel_level(self):
        return self.__fuel_level

# 創建一個Car對象
my_car = Car("Toyota", "Camry")

# 訪問公開屬性
print("Car brand:", my_car.brand)
print("Car model:", my_car.model)

# 訪問私有屬性（將會報錯）
# print("Fuel level:", my_car.__fuel_level)

# 使用公開方法
my_car.drive()
my_car.drive()
print("Fuel level:", my_car.get_fuel_level())

# 使用公開方法
my_car.refuel()
print("Fuel level after refueling:", my_car.get_fuel_level())
