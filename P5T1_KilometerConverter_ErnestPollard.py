#Kilometer Converter
#11/11/2018
#CTI-110 P5T1-Kilometer Converter
#Ernest Pollard

CONVERSION_FACTOR = 0.6214

def main():
    #Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    #Display the distance converted to miles.
    show_miles(kilometers)

#The show_miles function converts the parameter km from
#kilometers to miles and displays the result.

def show_miles(km):
    #Calculate miles.
    miles = km * CONVERSION_FACTOR

    #Display the miles.
    print(km, 'kilometers equal', miles, 'miles.')

#Call the main function.
main()
