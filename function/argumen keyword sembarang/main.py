def main(**kwargs):
  return print("Umur",kwargs["name"],"adalah",kwargs["age"],"tahun")

if __name__ == "__main__":
  # Untuk mengirim argumen dapat dengan sintaks key = value.
  # Dengan cara ini, urutan argumen tidaklah penting.
  main(name = "Andi", age = 21) 