### Create separate list of even and odd numbers

myList = [1,2,3,4,5,6,7,8,9]

evenList = []
oddList = []

for n in myList:
    if( n % 2 == 0 ):
        evenList.append( n )
    else:
        oddList.append( n )

print( "Even List Items: ", evenList )
print( "Odd List Items: ", oddList )