def main():
  # Deklarasi variable untuk pengkondisian
  umur = 18
    
  if umur >= 17:
    # Blok kode yang dijalankan jika kondisi benar (True)
    print("Saya sudah dewasa")
  elif umur <= 17:
    # Blok kode yang dijalankan jika kondisi sebelumnya salah (False)
    print("Saya belum dewasa")
  else:
    # Blok kode yang dijalankan jika semua kondisi salah (False)
    print("Variable umur belum dimasukkan")
  
if __name__ == "__main__":
  main()