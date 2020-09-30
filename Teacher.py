from person import ClassPerson

class Teacher(ClassPerson):
	def getID(self):
		return int(input("Enter your ID"))

def main():
	s = Teacher()
	Id = s.getID()
	name = s.getName()
	age = s.getAge()
	print("Name:{}".format(name))
	print("ID:{}".format(Id))
	print("Age:{}".format(age))
	

if __name__ == '__main__':main()