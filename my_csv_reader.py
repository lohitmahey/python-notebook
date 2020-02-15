### Reading the file

import os
filename = 'housing.data'

if os.path.isfile(filename):
    print( "I have a file to process" )

    f = open(filename)

    for line in f.readlines():
        new_l = line.strip().replace("  ",",")
        print( "['",new_l,"']" )
    f.close()

else:
    print('Boo, no file for me')
