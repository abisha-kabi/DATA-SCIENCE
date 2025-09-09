import numpy as np
a=np.array1=[1,2,3,4,5]
b=np.array2=[3,5,6,7,4]
are_equal = np.array_equal(a,b)
if are_equal:
    print("arrays are equal")
else:
    print("arrays are not equal")