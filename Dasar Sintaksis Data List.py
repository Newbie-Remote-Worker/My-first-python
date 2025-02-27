"""
Dasar Data List
"""

books_list = ['Deadly 7 Sins','Atomic habits','Law of Power']
print('showing variable books_list')
print(books_list)

print('proces all with for in')
for book in books_list:
    print (book)

# Memulai Elemen dari urutan yang ditentukan

print('\nShow all books list on some index')
print(books_list[0])
print(books_list[1])
print(books_list[2])

print('\nShow all books list with for in range')
for i in range(1, len(books_list)):
    print(books_list[i])

# Menambahkan Section Elemen pada Data List

books_list = [2, 'Habit no 1', 212, 'section 2']
print('\nShow all books list wigh for in range')
for i in range(1, len(books_list)):
    print(books_list [i])

# Menambah Eelemen dalam Data List

print('\nBring back value of books_list')
books_list = ['Deadly 7 Sins','Atomic habits','Law of Power']
print('\nAdd 1 new book')
books_list.append('Madilog')
for i in range(0, len(books_list)):
    print(books_list [i])

# Mengganti Elemen dalam Data List

print('\nReplace second book')
books_list = ['Deadly 7 Sins','Atomic habits','Law of Power']
books_list [1] = 'Micro habits'
for i in range(len (books_list)):
    print(books_list[i])
