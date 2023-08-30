def main():
  # Deklarasi variable untuk pengkondisian  
  i = 1
  
  while i < 6:
    print(i)
    if i == 3:
      # Dengan pernyataan break dapat menghentikan 
      # pengulangan bahkan jika kondisi while masih benar
      break
    i += 1

if __name__ == "__main__":
  main()