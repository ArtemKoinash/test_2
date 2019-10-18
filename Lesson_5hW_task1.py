class Person:
    """basic class for persons"""

    def __init__(self, full_name = "Name Surname", year_of_birthday = "Year"):
        """show basic values for person"""
        self.full_name = full_name
        self.year_of_birthday = year_of_birthday

    def person_name(self):
        """return name of person"""
        pn = self.full_name.split(' ')
        pn1 = pn[0]
        return pn1

    def person_surname(self):
        """return surname of person"""
        ps = self.full_name.split(' ')
        ps1 = ps[1]
        return ps1

    def current_age(self, current_year):
        """show current age of person"""
        age = current_year - int(self.year_of_birthday)
        # if self.year_of_birthday <= 1900 or self.year_of_birthday >= current_year
        #     assert
        print(age)

    def __str__(self):
        return f"{self.__class__} Full name: {self.full_name}, Year of a birthday: {self.year_of_birthday}"

class Employee(Person):
    """this class add such values like: position, experience, salary"""
    def __init__(self, position, experience, salary):
        super().__init__(full_name, year_of_birthday)
        self.position = position
        self.experience = experience
        self.salary = salary

    def level(self):
        """should return level that depends from experience with potion of employee"""
        if 3 > self.experience >= 0:
            return f"Junior {self.position}"
        elif 3 <= self.experience < 6:
            return f"Middle {self.position}"
        elif self.experience >= 6:
            return f"Senior {self.position}"
        else:
            return None

    def up_salary(self, raise_size):
        """show new size of salary"""
        new_salary = self.salary + raise_size
        return f" Amount of salary after raise: {new_salary} Soviet Rubls :)"

    def __str__(self):
        return f"{self.__class__} Position: {self.position}, Experience: {self.experience}, Salary:{self.salary}"


class ITEmployee(Employee):
    def __init__(self, skils):
        super().__init__(position)
        self.skils = skils

    def add_skill(self, new_skill):
        return self.skils.append(new_skill)


    def __str__(self):
        return f"{self.__class__} Skills: {self.position}"




if __name__ == "__main__":
    '''     '''
    p1 = Person('Anna Mikaluk', 1988)
    p2 = Person('Artur Butnik', 1990)
    p3 = Person('Anna Karpets', 1991)
    e1 = Employee()









