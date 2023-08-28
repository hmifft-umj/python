# Import library python
import numpy as np

# Membuat array data
data = np.array([12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

# Operasi statistik
rata_rata = np.mean(data)
median = np.median(data)
deviasi_standar = np.std(data)
variansi = np.var(data)

# Menampilkan pada terminal
print("Rata-rata:", rata_rata)
print("Median:", median)
print("Deviasi Standar:", deviasi_standar)
print("Variansi:", variansi)