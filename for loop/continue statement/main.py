def main():
  # Deklarasi variable untuk pengkondisian 
  fruits = ["apple", "banana", "cherry"]
  for x in fruits:
    if x == "banana":
      # Dengan pernyataan break, kita dapat menghentikan 
      # pengulangan sebelum melalui semua item yang ada
      continue
    print(x)

if __name__ == "__main__":
  main()