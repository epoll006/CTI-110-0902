#CTI-110
#P3HW1- Roman Numerals
#Ernest Pollard
#9/29/2018
#
userNumber = int( input( "Please enter a number: " ) )

print()

if userNumber == 1:
    print( "I" )
elif userNumber == 2:
    print( "II" )
elif userNumber == 3:
    print( "III" )
elif userNumber == 4:
    print( "IV" )
elif userNumber == 5:
    print( "V" )
elif userNumber == 6:
    print( "VI" )
elif userNumber == 7:
    print( "VII" )
elif userNumber == 8:
    print( "VIII" )
elif userNumber == 9:
    print( "IX" )
elif userNumber == 10:
    print( "X" )
else:
    print( "Error: Enter a number between" + \
           "1 and 10. " )
