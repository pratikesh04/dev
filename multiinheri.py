
class Person(object):

    def __init__(self, name):
        self.name = name

    def get_details(self):

        return self.name


class Student(Person):

    def __init__(self, name, branch, year):
        super().__init__(name)
        self.branch = branch
        self.year = year

    def get_details(self):

        return "%s studies %s and is in %s year." % (self.name, self.branch, self.year)


class Teacher(Person):

    def __init__(self, name, papers):
        super().__init__(name)
        self.papers = papers

    def get_details(self):
        return "%s teaches %s" % (self.name, ','.join(self.papers))


person1 = Person('Mitcorer')
student1 = Student('Souravsing', 'CSE', 2020)
teacher1 = Teacher('Prof.Trupti', ['Python', 'C++'])
print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())