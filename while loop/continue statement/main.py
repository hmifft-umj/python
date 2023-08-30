def main():
  # Deklarasi variable untuk pengkondisian  
  i = 0
  
  while i < 4:
    i += 1
    if i == 3:      
      # Pernyataan continue dapat menghentikan iterasi saat ini 
      # dan melanjutkan dengan iterasi berikutnya
      continue
    print(i)

if __name__ == "__main__":
  main()