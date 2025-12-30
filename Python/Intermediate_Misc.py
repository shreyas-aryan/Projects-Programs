#use of static in python
class Employee:
    sal=20
    def __init__(self,name,position):
        self.name=name
        self.position=position
        Employee.sal+=20
    def get_info(self):
        print(f"{self.name}={self.position}")
    @staticmethod
    def is_valid(pos):
        valid=["cook","manager","scientist"]
        print(pos in valid)
print(Employee.sal)
Employee.is_valid("cook")
c1=Employee("Shreyas","cook")
c2=Employee("Reyas","manager")
print(Employee.sal)
print(c2.sal)
