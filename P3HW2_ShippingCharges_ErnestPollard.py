#CTI-110
#P3HW2 - Shipping Charges
#Ernest Pollard
#9/29/2018
#
userWeightOfPackage = int( input( "Enter the weight of the package: " ) )

if userWeightOfPackage <= 2:
    shippingCharges = 1.50
elif userWeightOfPackage < 7:
    shippingCharges = 3.00
elif userWeightOfPackage < 11:
    shippingCharges = 4.00
else:
     shippingCharges = 4.75

print( "For a package weighing " + str( userWeightOfPackage ) + \
      ", you'll pay $" + format( shippingCharges, ",.2f" ) )
