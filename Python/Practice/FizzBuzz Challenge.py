__author__ = 'Billy'

for num in range(1, 21):

    if num % 5 == 0 and num % 3 == 0:
        print "FizzBuzz" # Needed to catch 15 before 3 and 5 tests.
    elif num % 3 == 0: # Originally had another if statement here printing Fizz after Fizzbuzz.
        print "Fizz"
    elif num % 5 == 0:
        print "Buzz"
    else:
        print num

