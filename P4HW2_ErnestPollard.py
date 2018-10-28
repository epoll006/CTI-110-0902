#Celsius to Fahrenheit Table
#10/11/2018
#CTI-110 P4HW2
#Ernest Pollard
#
#This program is used to make a conversion table of celsius to fahrenheit

print( "Celsius temperature\tFahrenheit Equivalent" )
for currentCelsiusTemperature in range( 21 ):
    fahrenheitTemperatureEquivalent = ( 9 / 5 ) * currentCelsiusTemperature + 32
    print( currentCelsiusTemperature,"\t\t\t\t", format( fahrenheitTemperatureEquivalent, ".1f" ) )
