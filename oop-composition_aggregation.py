# 組合的例子
class Engine:
    def __init__(self,type):
        self.type = type

class Car:
    def __init__(self):
        self.engine = Engine("Gasoline")
        print("composition... "+str(self.engine.type))

# 聚合的例子
class Department:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self):
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

# 使用組合關係創建一輛汽車
my_car = Car()



# 使用聚合關係創建一家公司
company = Company()
hr_department = Department("HR")
finance_department = Department("Finance")
company.add_department(hr_department)
company.add_department(finance_department)
