#1)Write a program that calculates the first 10 digits of the result of the following operation: square(2^(101)/pi ^(53) 11^7)

import math
number=math.sqrt(2**101/(math.pi**53*11**7))
number_str = str(number)
digits=number_str[:10]
print(digits)
