import numpy as np

a = np.array([1, 2, 3])  
print(type(a), a.shape, a[0], a[1], a[2])
a[0] = 5                 
print(a)                  

b = np.array([[1,2,3],[4,5,6]])   
print(b)

print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])

a = np.zeros((2,2))  
print(a)

b = np.ones((1,2))   
print(b)

c = np.full((2,2), 7) 
print(c)

d = np.eye(2)        # Create a 2x2 identity matrix
print(d)

import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[:2, 1:3]
print(b)

print(a[0, 1])
b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1]) 

row_r1 = a[1, :]    # Rank 1 view of the second row of a  
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
row_r3 = a[[1], :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
print(row_r3, row_r3.shape)

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print()
print(col_r2, col_r2.shape)

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(a)

a[np.arange(4), b] += 10
print(a)

x = np.array([1, 2])  
y = np.array([1.0, 2.0])  
z = np.array([1, 2], dtype=np.int64)  

print(x.dtype, y.dtype, z.dtype)
