def main():
    # Deklarasi dictionary berisi pasangan kunci dan nilai
    my_dictionary = {
        'title': 'Python',
        'designed_by': 'Guido Van  Rossum',
        'description': 'High-level programming language'
    }
    # Mengganti pasangan kunci dan nilai
    my_dictionary['description'] = 'Too long'
    # Menampilkan dictionary
    print(my_dictionary)

if __name__ == '__main__':
    main()