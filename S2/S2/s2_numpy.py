import numpy as np

a = np.array([1, 2, 3])  # Create a rank 1 array
print(type(a))            # Prints "<type 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                 # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"


b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])



a = np.zeros((2,2))  # Create an array of all zeros
print(a)              # Prints "[[ 0.  0.]


                     #          [ 0.  0.]]"    
b = np.ones((1,2))   # Create an array of all ones
print(b)              # Prints "[[ 1.  1.]]"


d = np.eye(2)        # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]


                     #          [ 0.  1.]]"    
e = np.random.random((2,2)) # Create an array filled with random values
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                            #               [ 0.68744134  0.87236687]]"

a = np.array([[1,2], [3, 4], [5, 6]])

bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
                    # this returns a numpy array of Booleans of the same
                    # shape as a, where each slot of bool_idx tells
                    # whether that element of a is > 2.
            
print(bool_idx)      # Prints "[[False False]
                    #          [ True  True]
                    #          [ True  True]]"

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print(a[bool_idx])  # Prints "[3 4 5 6]"

# We can do all of the above in a single concise statement:
print(a[a > 2])     # Prints "[3 4 5 6]"





x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))



