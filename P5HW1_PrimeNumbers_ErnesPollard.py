#Prime Numbers
#11/11/2018
#CTI-110 P5HW1-Prime Numbers
#Ernest Pollard

# Determine whether number is Prime or not.


#taking input from user
number = int(input("Enter any number: "))

#prime number is always greater than 1

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

#if the number entered is less than or equal to 1
#then it is not prime

else:
    print(number, "is not a prime number")
