
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)

# print(type(arr))

# import numpy as np
# array=np.random.rand(3,2)
# print(array)

import numpy as np
A = np.array([[2, 0.5],
              [3, -1]])
egnvlues, egnvctrs = np.linalg.eig(A)
Q = egnvctrs
Λ = np.diag(egnvlues)
Q_inv = np.linalg.inv(Q)
A_decomposed = np.matmul(np.matmul(Q, Λ), Q_inv)
 
print("Original Matrix A:\n", A)
print("Eigenvalue Decomposition of A:\n", A_decomposed)