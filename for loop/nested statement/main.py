def main():
  adj = ["red", "tasty"]
  fruits = ["apple", "banana"]

  # Pengulangan dalam akan dieksekusi satu kali 
  # untuk setiap iterasi dari pengulangan luar
  for x in adj:
    for y in fruits:
      print(x, y)

if __name__ == "__main__":
  main()      