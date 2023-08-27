def main():
    # Deklarasi dictionary berisi pasangan kunci dan nilai
    my_dictionary = {
        'title': 'Python',
        'designed_by': 'Guido Van  Rossum',
    }
    # Metode keys() untuk mendapatkan daftar semua kunci dalam kamus
    keys_dictionary = set(my_dictionary.keys())
    # Menampilkan set key
    print(keys_dictionary)

if __name__ == '__main__':
    main()