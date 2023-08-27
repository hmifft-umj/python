def main():
    # Deklarasi dictionary berisi pasangan kunci dan nilai
    my_dictionary = {
        'title': 'Python',
        'designed_by': 'Guido Van  Rossum',
        'description': 'Too Long'
    }
    # Menghapus pasangan kunci dan nilai
    del my_dictionary['description']
    # Menampilkan dictionary
    print(my_dictionary)


if __name__ == '__main__':
    main()
