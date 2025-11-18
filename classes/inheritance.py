"""Say we have a zoo """

class Animal:

    def __init__(self, name="None"):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes sound")

#
#
# class Cat(Animal):
#
#     def __init__(self, name):
#         super().__init__()
#         # self.name = name
#         pass
#
#
# c = Cat("Hello")
# print(c.name)
#
#
# class A():
#
#
#     def __init__(self):
#         pass
#
#


import zoo_project.Cages

