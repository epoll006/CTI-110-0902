#Figuring out future sales
#9/21/2018
#CTI-110 P2T1 - Sales Prediction
#Ernest Pollard
#

projectedTotalSales = float( input( "Enter the projected amount" + \
                                    "of total sales: " ) )

#Calculate the profit as 23 percent of total sales
profit = 0.23 * projectedTotalSales

#Display the profit
print( "The profit is $", profit )
