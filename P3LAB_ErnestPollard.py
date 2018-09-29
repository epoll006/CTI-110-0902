#CTI-110
#P3LAB: Debugging
#Ernest Pollard
#9/29/2018
#
def main():
    # This program takes a number grade and outputs a letter grade.

    # System uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    # Get a test score from the user    
    score = int( input( "Enter your test score: " ) )

    # Determine the grade.
    if score >= A_score:
        print( "Your grade is A." )
    else:
        if score >= B_score:
            print( "Your score is B." )
        else:
            if score >= C_score:
               print( "Your score is C." )
            else:
               if score >= D_score:
                  print( "Your score is D." )
               else:
                  print( "Your score is F." )

main()

  
   
