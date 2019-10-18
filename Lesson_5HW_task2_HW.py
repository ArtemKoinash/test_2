# class Person:
#     '''basic class for persons'''
#     # common_propeties = {'full_name': 'name surname'}
#     def __init__(self, yearofbithday):
#         """ """
#         self.yearofbithday = yearofbithday
#
#     def current_age(self, current_year):
#         """show current age of person from class Person"""
#         age = current_year - self.yearofbithday
#         # if self.yearofbithday <= 1900 or self.yearofbithday >= current_year
#         #     assert
#         print(age)

#
#
# if __name__ == "__main__":
#     '''     '''
#     p1 = Person(yearofbithday=1989)
# p1.current_age(2019)


# class Employee
# class ITEmployee

class Rectangle:
    """described rectangle"""
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        s = self.side_a * self.side_b
        return s

    def perimentr(self):
        p = self.side_a * 2 + self.side_b * 2
        return p

    def __str__(self):
        return f"{self.__class__} side length: {self.side_a} {self.side_b}"

class MapPoint:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def distance_to_begin(self):
        dtb = (self.X**2 + self.Y**2)**0.5
        return dtb

    def distance_between_points(self, X_2, Y_2):
        dbp = ((self.X - X_2)**2 + (self.Y - Y_2)**2)**0.5
        return dbp

    def __str__(self):
        return f"{self.__class__} coordinates: {self.X} {self.Y}"


if __name__ == "__main__":
    '''     '''
    r1 = Rectangle(13, 12)
    r2 = Rectangle(19, 12)
    p1 = MapPoint(10, 10)
    p2 = MapPoint(21, 14)



# print(MapPoint.__str__(MapPoint))
print(r1)
print(p1)