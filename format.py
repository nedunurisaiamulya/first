#To print Decimal, Octal, Hexadecimal and Binary Format of numbers from 1 to 101

#integer value for the limit.Here it is 101, can be changed.
n=17
#For spacing between the each column, based on the integer limit given.
spacing = len(bin(n)[2:])

print "Decimal".rjust(spacing, ' ')+"Octal".rjust(spacing+1, ' ')+"HexaDeci".rjust(spacing+2, ' ')+"Binary".rjust(spacing, ' ')

for i in range(1,n+1):
    print str(i).rjust(spacing, ' '),str(oct(i)[1:]).rjust(spacing, ' '),str(hex(i)[2:].upper()).rjust(spacing, ' '),str(bin(i)[2:]).rjust(spacing, ' ') 
