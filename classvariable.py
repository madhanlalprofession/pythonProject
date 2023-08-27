class student:
    college = "SRIET"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("the name of student is ", self.name)
        print("the age of student is ", self.age)
        print("the gender of student is ", self.gender)
        print("the school of student is ", self.college)
        print()


student.college = "st.joseph"
madhan = student("madhan", 20, "male")
revathi = student("revathi", 20, "female")
madhan.display()
revathi.display()
