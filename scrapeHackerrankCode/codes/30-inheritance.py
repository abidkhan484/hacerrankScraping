# Accepted
# Python 3

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        total=0
        n=len(scores)
        for i in range(n):
            total += self.scores[i]
        avg = total/n

        if (avg<40):
            return "T"
        elif (avg>=40) & (avg<55):
            return "D"
        elif (avg>=55) & (avg<70):
            return "P"
        elif (avg>=70) & (avg<80):
            return "A"
        elif (avg>=80) & (avg<90):
            return "E"
        else:
            return "O"
