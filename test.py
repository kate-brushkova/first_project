# with open('test.txt', 'w') as d:
#     d.write('hello\n')
#     d.write('kate')
#
# with open('test.txt', 'r') as d:
#     print(d.read())
# class Table:
#     def __init__(self, kg):
#         self._kg = kg
#
#     def get_kg_table(self):
#         return self._kg
#
#     def set_kg_table(self, new_kg=None):
#         if new_kg is not None:
#             self._kg = new_kg
#         return self._kg
#
#
# my_table = Table(10)
# print(my_table.get_kg_table())
# print(my_table.set_kg_table(new_kg=15))
#
#
# class OneTable(Table):
#     def __init__(self, kg, sm):
#         super(OneTable, self).__init__(kg)
#         self._sm = sm
#
#
# a = [1, 2, 3]
# a.append(4)
# a.insert(3, 5)
# a.remove(3)
# print(a)
#
#
# c = {1: 'a', 2: 'b'}
# c.update({3: 's'})
#
# with open('test.txt', 'w') as f:
#     f.write('Kate\n')
#     f.write('Brushkova')
#
# with open('test.txt', 'r') as f:
#     print(f.read())
#
#
# def oleh(age=30):
#     return age
#
#
# def get_age_oleh(age_oleh):
#     return oleh(age=age_oleh)
#
#
# print(get_age_oleh(31))
#
#
# def kate(age=21):
#     return age
#
#
# def get_age_kate(age_kate):
#     return kate(age=age_kate)
#
#
# print(get_age_kate(20))
#
#
# def we_are_together(duration=1):
#     return duration
#
#
# def get_we_are_together(new_dur):
#     return we_are_together(duration=new_dur)
#
#
# print(get_we_are_together(11))


# class MyPerson:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name_age(self):
#         return '- '.join([self.name, self.age])
#
#
# me = MyPerson('Kate', '21')
# print(me.get_name_age())
#
#
# class Home:
#     def __init__(self, rooms, coast):
#         self._rooms = rooms
#         self._coast = coast
#
#     def get_rooms(self):
#         return self._rooms
#
#     def get_coast(self):
#         return self._coast
#
#     def set_coast(self, new_coast=None):
#         if new_coast is not None:
#             self._coast = new_coast
#         return self._coast
#
#
# my_home = Home('1', '8500')
# print(my_home.get_rooms())
# print(my_home.get_coast())
# print(my_home.set_coast(new_coast=8400))
#
#
# class OnePerson(MyPerson):
#     def __init__(self, name, age, place):
#         super(OnePerson, self).__init__(name, age)
#         self._place = place
#
#     def get_place(self):
#         return self._place
#
#     def set_age(self, new_age=None):
#         if new_age is not None:
#             self.age = new_age
#         return self.age
#
#
# your_person = OnePerson('Kate', '21', 'Odessa')
# print(your_person.get_place())
# print(your_person.set_age(new_age=14))
#
#
# class People:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
#
#
# import time
#
# print('3')
# time.sleep(1)
# print('2')
# time.sleep(1)
# print('1')
# time.sleep(1)
#
#
# import random
# list = [20, 30, 40, 50, 60, 70, 80, 90]
# sampling = random.choices(list, k=1)
# print("Случайное число из списка", sampling)
#
#
# class Cup:
#     def __init__(self, size, color):
#         self._size = size
#         self._color = color
#
#     def get_size(self):
#         return self._size
#
#     def get_color(self):
#         return self._color
#
#     def set_size(self, new_size=None):
#         if new_size is not None:
#             self._size = new_size
#         return self._size
#
#
# one_cup = Cup('100', 'black')
# print(one_cup.set_size(new_size='200ml'))
#
#
# class TeaCup(Cup):
#     def __init__(self, size, color, made_of):
#         super(TeaCup, self).__init__(size, color)
#         self.made_of = made_of
#
#     def get_tea_cup_color(self):
#         res = super().get_color()
#         return 'color: %s' % res
#
#     @property
#     def get_size_color(self):
#         return 'ml '.join([self._size, self._color])
#
#
# cup_tea = TeaCup('150', 'red', 'China')
# print(cup_tea.get_tea_cup_color())
# print(cup_tea.made_of)
# print(cup_tea.get_size_color)


class Computer:
    def __init__(self, memory, cpu):
        self._memory = memory
        self._cpu = cpu

    # @property
    def get_memory(self):
        return self._memory

    def get_cpu(self):
        return self._cpu

    def set_memory(self, new_memory):
        self._memory += new_memory
        return self._memory


my_computer = Computer(100, 2)
print(my_computer.set_memory(4))
print(my_computer.get_memory())


class SuperComputer(Computer):
    def __init__(self, memory, cpu):
        super(SuperComputer, self).__init__(memory * 10, cpu * 10)
        # self._memory = memory * 10
        # self._cpu = cpu * 10

    def get_memory(self):
        return 'Memory: %s' % super(SuperComputer, self).get_memory()


print(SuperComputer(121, 3).get_memory())


def dec(f):
    def wrap():
        print('Log finish with result: %s' % f())
    return wrap()

@dec
def test():
    return 2


@dec
def test2():
    return 'hello'


class Person:
    # def __init__(self, name, age):
    #     self._name = name
    #     self._age = age

    @classmethod
    def is_adult(cls, age):
        return age >= 18


print(Person.is_adult(1))

# FIRST TIME
# git init
# git add .
# git commit -m "first commit"
# git remote add origin https://github.com/kate-brushkova/first_project.git
# git push -u origin <branch_name>

# REGULAR WORK
# git pull
# git status
# git diff
# git add .
# git commit -m 'commit message'           |        git commit --amend
# git push origin <branch_name>
# git push origin <branch_name>

# BRANCH MANAGEMENT
# git branch
# git checkout -b <branch_name>            |       without 'b' flag the branch will be changed

# VENV
# source venv/bin/activate
# deactivate



# TODO list
#  1. review github interface
#  2. review commands and test them out
#  #. read the docs
