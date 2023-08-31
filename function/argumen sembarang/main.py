# Jika tidak tahu berapa banyak argumen yang akan diteruskan 
# ke dalam fungsi, tambahkan tanda * sebelum nama parameter 
# dalam definisi fungsi.
def main(*args):
  # Dengan cara ini, fungsi akan menerima sebuah tuple argumen, 
  # dan dapat mengakses item-itemnya sesuai.
  return print(f"Umur {args[0]} adalah {args[1]} tahun")

if __name__ == "__main__":
  main("Andi", 21) 