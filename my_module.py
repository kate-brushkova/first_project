class Test:
    @staticmethod
    def show():
        print('Hello')


def oleh(age=30):
    return age


def get_age_oleh(age_oleh):
    return oleh(age=age_oleh)


print(get_age_oleh(31))


class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    @property
    def full_name(self):
        # self._name + ' ' + self._surname
        return ' '.join([self._name, self._surname])


me = Person('Ol', 'Di')
print(me.full_name)


class Home:
    def __init__(self, bed_number, sofa, table):
        self._bed_number = bed_number
        self._sofa = sofa
        self._table = table

    def get_bed_number(self):
        return self._bed_number

    def set_bed_number(self, new_bed_number):
        self._bed_number = new_bed_number

    @property
    def sofa_name(self):
        return self._sofa


my_home = Home(2, "Egger", 'lie')
print(my_home.get_bed_number())

my_home.set_bed_number(3)
print(my_home.get_bed_number())

print(my_home.sofa_name)


class OneBedSmartHome(Home):
    def __init__(self, sofa, table, square):
        super(OneBedSmartHome, self).__init__(1, sofa, table)
        self._square = square

    def get_square(self):
        return self._square

    def set_bed_number(self, new_bed_number):
        self._bed_number = new_bed_number

    def get_bed_number(self):
        res = super().get_bed_number()
        return 'number: %s' % res


bed_one = OneBedSmartHome("LG", "fili", 45)

print(bed_one.sofa_name)
print(bed_one.get_bed_number())
