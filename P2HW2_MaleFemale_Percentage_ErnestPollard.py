#Male vs. Female Ratios
#9/21/2018
#CTI-110 P2HW2 - Percentages of Male and Female Students
#Ernest Pollard
#
#Write a program that asks user for the number of males and the number of females registered in a class.

#20 students = 100%
#then 8 students = ?

#20 students = 100%
#then 12 students = ?

males = int( input( "Please enter the number of males in the class: " ) )
females = int( input( "Please enter the number of females in the class: " ) )
allStudents = males + females

malePercentage = ( males / allStudents ) * 100
femalePercentage = (females / allStudents ) * 100

print("Male percentage: " + str( malePercentage ) )
print ("Female percentage: " + str( femalePercentage ) )
