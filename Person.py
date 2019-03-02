class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def eat(self, food):
        print(self.name + "가 "+ food + "를 먹습니다.")

    def __str__(self):
        return self.name + "는 " + str(self.age) + "살이고, 키는 " + str(self.height)

    def __len__(self):
        return self.height

    def __getitem__(self, key):
        if key == "name":
            return self.name
        if key == "age":
            return self.age

        return None

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def work(self):
        print("열심히 일을 합니다.")

    def get_salary(self):
        print("급료를 받습니다.")
        return self.salary

p = Person("철수", 18, 170)
print(p)
print(len(p))
print(p["age"])
print(p["unknown"])