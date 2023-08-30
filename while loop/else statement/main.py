def main():
  # Deklarasi variable untuk pengkondisian  
  i = 1

  while i < 3:
    print(i)
    i += 1  
  # Dengan pernyataan else, kita dapat menjalankan 
  # sebuah blok kode sekali saat kondisi tidak lagi benar
  else:
    print(f"Nilai {i} tidak kurang dari 3")    

if __name__ == "__main__":
  main()