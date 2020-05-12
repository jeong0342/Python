class Employee:
    def __init__ (self, name=0, dailywage=0, weekly=0):
        self.name = name
        self.salary = dailywage*weekly
    def calculateSalary()

# dailywage와weekly 곱 계산하여 출력
emp1 = Employee("Zara", 200, 5)
print(emp1.name, emp1.salary)
