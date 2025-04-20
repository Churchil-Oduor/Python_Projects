class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initialized SchoolMember: {}".format(self.name))

    def tell(self):
        print("Name: {} Age: {}".format(self.name, self.age))

 
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Initialized Teacher: {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Salary: {}".format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        print("Initialized Student: {}".format(self.name))


    def tell(self):
        SchoolMember.tell(self)
        print("Marks: {:d}".format(self.marks))


t = Teacher("Mrs. Okech", 40, 40000)
t.tell()
