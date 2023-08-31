# Secara default, sebuah fungsi harus dipanggil 
# dengan jumlah argumen yang benar.
def main(name, age):
  return print(f"Umur {name} adalah {age} tahun")

if __name__ == "__main__":
  # Jika fungsi mengharapkan 2 argumen, maka harus memanggil 
  # fungsi dengan 2 argumen, bukan lebih banyak atau kurang.
  main("Andi", 21) 