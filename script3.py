### For multiples of 3 print "Fizz", for 5 print "Buzz" and "FizzBuzz" for multiples of both


for n in range(1, 100):
    if( n % 3 == 0 and n % 5 == 0 ):
        print( n, "FizzBuzz" )
    elif( n % 3 == 0 ):
        print( n, "Fizz" )
    elif( n % 5 == 0 ):
        print( n, "BUzz" )
