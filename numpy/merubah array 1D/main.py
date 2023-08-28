# Import library python
import numpy as np

# Membuat array 1D
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Mengubah bentuk array menjadi 2D (5x2)
array_2d = array_1d.reshape(2, 5)

# Menampilkan pada terminal
print("Array 1D:", array_1d)
print("Array 2D:\n", array_2d)