#append of matrix
import numpy as np
a=np.array(input("GIVE MATRIX:"))
b=np.array(input("GIVE ANOTHER MATRIX:"))
x=np.append(a,b)#adding of two matrix
print("new array after adding column")
print (x)
#part 2
import numpy as np
a=input("GIVE ARRAY:")
b=input("GIVE ANOTHER ARRAY:")
print "A=",a
print "B=",b
l=len(b)
for i in range(0,l):
     S1a=np.append(a,b[i])
print("after appending:",a)

