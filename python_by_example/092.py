from array import *

array1 = array('i',[1,4,2,3,5,6])
array2 = array('i',[53,23,4])

for x in array2:
   array1.append(x)

nums = sorted(array1)
for x in nums:
   print(x, end=" ")