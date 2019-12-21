#performing operations on n*n matrix
import numpy as np
from numpy import linalg
x=np.array(input("ENTER MATRIX X\t"))
y=np.array(input("ENTER MATRIX Y\t"))
print "MATRIX X\n", x
print "\n"
print "MATRIX Y\n",y
add=np.add(x,y)
print "ADD MATRIX\n",add
print "\n"
sub=np.subtract(x,y)
print"SUBTRACTION X-Y\n",sub
print "\n"
div=np.divide(x,y)
print "DIVISION X/Y\n",div
print "\n"
mul=np.multiply(x,y)
print"MULTIPLICATION X*Y\n",mul
print "\n"
dot=np.dot(x,y)
print"DOT PRODUCT X.Y\n",dot
print "\n"
sqrt=np.sqrt(x)
print "SQRT OF MATRIX X\n",sqrt
print "\n"
trans=x.T
print" TRANSPOSE MATRIX X \n",trans
print "\n"
summ=np.sum(y)
print"ADDITON OF ELEMENTS Y \n",summ
print "\n"
sqr=np.square(y)
print" SQUARE MATRIX y \n",sqr
print "\n"
A = np.matrix([[1,2,3],[4,5,6],[7,8,9]]) 
print "NEW MATRIX \n",A
print "\n"
# Rank of a matrix
print "RANK OF A:\n", np.linalg.matrix_rank(A)
# Trace of matrix A
print "\n"
print "TRACE A:", np.trace(A)
print "\n"
# Determinant of a matrix
print "DET A :\n", np.linalg.det(A)
print "\n"
# Inverse of matrix A
print "INVERSE A:\n", np.linalg.inv(A)
print "\n"
#transpose of the matrix 
print  "TRANSPOSE MATRIX :\n ",A.T
print "\n"
#print (A.T) 
# Creating a diagonal matrix
a = np.diag((1, 2, 3)) 
print "DIAGONAL MATRIX : \n",a
print "\n"
#finding eigen values of general matrix
print "EIGEN VALUES OF A: \n",np.linalg.eigvals(a)
print "\n"
#finding eigen vectors and values of general matrix
print "EIGEN VECTORS :\n",np.linalg.eigh(a)
print "\n"
