#Create a variable grade holding an integer between 0 - 100

#Code if, elif, else statements to print the letter grade of the number grade variable

#Grades:

#A = 90 - 100

#B = 80 - 89

#C = 70-79

#D = 60 - 69

#F = 0 - 59
marks = int(input("Enter marks : "))
if marks >= 90 and marks <=100:
    print("A")
elif marks >= 80 and marks <=89:
    print("B")
elif marks >= 70 and marks <=79:
    print("C")
elif marks >= 60 and marks <=69:
    print("D")
else:
    print("F")

