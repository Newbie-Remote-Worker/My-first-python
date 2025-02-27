"""
Dasar Data List
"""

books_list = ['Deadly 7 Sins','Atomic habits','Law of Power']
print('showing variable books_list')
print(books_list)

print('proces all with for in')
for book in books_list:
    print (book)

# Memulai Elemen dari angka yang ditentukan

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

# Mengganti Elemen dalam Data List

print('\nReplace second book with Micro Habits')
books_list = ['Deadly 7 Sins','Atomic habits','Law of Power']
books_list [1] = 'Micro habits'
for i in range(len (books_list)):
    print(books_list[i])

# Mengambil Elemen dan memunculkan kembali Elemen yang sudah diambil dari Data List

print('\nTake out second book')
books_list = ['Deadly 7 Sins','Atomic habits','Law of Power']
book = books_list.pop(2)
for i in range(0, len(books_list)):
    print(books_list[i])

print('\nReappear the book')
print(book)

# Menambah Elemen dalam Data List (Push)

print('\nAdd new book of books_list')
books_list = ['Deadly 7 Sins','Atomic habits','Law of Power']
print('\nPush +1 book')
books_list.append('Art of not give a fuck')
for i in range(0, len(books_list)):
    print(books_list [i])

# Menghapus Elemen dari Data List sesuai angka yang ditentukan (Pop)

print('\nDelete book of book_list')
print('\nPop -1 book')
books_list = ['Deadly 7 Sins','Atomic habits','Law of Power']
books_list.pop(-1)
for i in range(0, len(books_list)):
    print(books_list[i])

print('\nDelete book of book_list')
print('\nPop -2 book')
books_list = ['Deadly 7 Sins','Atomic habits','Law of Power']
books_list.pop(-2)
for i in range(0, len(books_list)):
    print(books_list[i])