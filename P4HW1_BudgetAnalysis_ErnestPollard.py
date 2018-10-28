#Budget Analysis
#10/10/2018
#CTI-110 P4HW1
#Ernest Pollard
#
userBudget = float( input( "Enter how much you have budgeted" + \
                           "for the month: " ) )

moreExpenses = "y"
totalExpenses = 0

while moreExpenses == "y":
    userExpense = float( input( "Enter an expense: " ) )
    userTotalExpenses = totalExpenses + userExpense
    moreExpenses = input("Are there anymore expenses to add?: Type y," + \
          "for yes, any key for no: " )
if userTotalExpenses > userBudget:
    print( "You exceeded your budget of $",format( userBudget, ",.2f" ),\
           "by $",format( userTotalExpenses - userBudget, ",.2f" ) )
elif userBudget > totalExpenses:
    print( "You were under your budget of $", format( userBudget, ",.2f"), \
           "by $",format( userBudget - userTotalExpenses, ",.2f" ) )
else:
     print( "You stayed within your budget of $", \
            format( userBudget , ",.2f"),"." )
    
