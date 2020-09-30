from person import ClassPerson

class Student(ClassPerson):
	def getRollNo(self):
		return int(input("Enter your RollNo"))


def main():
	s = Student()
	roll = s.getRollNo()
	name = s.getName()
	age = s.getAge()
	print("Name:{}".format(name))
	print("RollNo:{}".format(roll))
	print("Age:{}".format(age))

if __name__ == '__main__':main()