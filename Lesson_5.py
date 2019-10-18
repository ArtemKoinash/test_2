# # x = list9()
# # print(type(x))
#     # def __init__(self, value):
#     #     self.name = value
#
# # if __name__ == "__main__":
# #     p1 = Person ()
# #     p1.set_name("Vasya")
# #     p2 = Person()
# #     p2.set_name("Kolya")
# #     print(p1.name, p2.name)
# #     print(p1.common_propertyies)
# #     print(p2.common_propertyies)
# #     print(p1.common_propertyies is p2.common_propertyies)
# #     p1.common_propertyies["ampount"] = 9e9
class Person:
    '''  '''
    common_properties = {"species": "human"}
    def __init__(self, name = "None", surname = "None", age = 0):
        self.name = name
        self.surname = surname
        self.age = age
        # self.skills = []

    def full_name(self):
        return f"{self.name} {self.surname}"

    def get_older(self, years):
        '''this method increase age on a number of years '''
        # return int(self.age) + int(years)
        self.age = self.age + years #self.age += years

    def __str__(self):
        return f"{self.__class__} object: {self.name} {self.surname}"


#
#
# def self(args):
#     pass
#
#
# class Employee(Person):
#     ''''''
#
#     def __init__(self, skills = None,  name = "", surname = "", age = None, salary = 0, position = None):
#         super().__init__(name, surname, age)
#         # if skills is not None:
#         #     self.salary  = salary
#         self.position = position
#         self.skills.extend(skills)
#
#     def full_name(self):
#         return f"{self.name} {self.surname}"
#
#     def income(self, month):
#         return self.salary * month
#
# class ITEmployee(Employee):
#     def __init__(self, *args, **kwargs):
#         super().__init__(self, *args, **kwargs)
#         self.skills = []
#
#     def add_skills(self, skills):
#         self.skills.extend(skills)
#
#     def add_skill(self, skill):
#         self.skill.append(skill)
#
#     def __add__(self, other):
#         return self.skills + other.skills
#
#
#
#
if __name__ == "__main__":
    '''     '''
    e3 = Employee
    e3.income(5, 12)
    e4 = ITEmployee

    p1 = Person("VAsya", age = 40, surname = "vasiliev")
    # print(p1.name)
    # print(p1.skills)
    p2 = Person()
print(p2.full_name())
print(p1.full_name())
# print(p1.get_older(8))
p1.get_older(20)




#
#
#
#
