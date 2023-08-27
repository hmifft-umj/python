def main():
    # Deklarasi dictionary berisi pasangan kunci dan nilai
    my_dictionary = {
        'title': 'Python',
        'designed_by': 'Guido Van  Rossum',
    }
    # Metode values() untuk mendapatkan daftar semua value dalam kamus
    keys_dictionary = list(my_dictionary.values())
    # Menampilkan list value
    print(keys_dictionary)

if __name__ == '__main__':
    main()