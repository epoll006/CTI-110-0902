#Tuition Increase
#CTI-110-0902
#Ernest Pollard
#P4HW3
#Make a program to display a semesters tuition increase amount for 5 years.
#
currentTuition = 8000

print( "Year\tTuition\n-----\t--------" )
for currentYear in range( 1, 6 ):
    currentTuition = currentTuition + ( 3 / 100 ) * currentTuition
    print( currentYear , "\t$", format( currentTuition, ".2f" ))
