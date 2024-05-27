#Day 12: Inheritance


class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
import math
#Solution Code Starts Here
class Student(Person):
    #Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self):
        grade = sum(self.scores)/len(self.scores)
        return ("O" if grade >= 90 else "E" if 80 <= grade < 90 else "A" if 70 <= grade < 80 else "P" if 55 <= grade < 70 else "D" if 40 <= grade < 55 else "T")
#Solution Code Ends here
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
