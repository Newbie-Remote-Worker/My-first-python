"""
Dasar Data List
"""

# Menghapus semua Elemen dari Data List (Delete Comperhension)

print('\nDelete all book of using (Delete Comperhension)')
books_list = ['Deadly 7 Sins','Atomic habits','Law of Power','Raja Tempe','Madilog','Gerpolek']
del books_list[:] #START:END
print('All books have been deleted')
for i in range(0, len(books_list)):
    print(books_list[i])

print('\nDelete some book of book_list using (Delete Comperhension)')
books_list = ['Deadly 7 Sins','Atomic habits','Law of Power','Raja Tempe','Madilog','Gerpolek']
del books_list[0:2] #START:END
print('Some books have been deleted')
for i in range(0, len(books_list)):
    print(books_list[i])

print('\nDelete some book of book_list using (Delete Comperhension)')
books_list = ['Deadly 7 Sins','Atomic habits','Law of Power','Raja Tempe','Madilog','Gerpolek']
del books_list[0:-2] #START:END
print('Some books have been deleted')
for i in range(0, len(books_list)):
    print(books_list[i])

print('\nDelete all book of using (Delete Comperhension)')
books_list = ['Deadly 7 Sins','Atomic habits','Law of Power','Raja Tempe','Madilog','Gerpolek']
del books_list[:] #START:END
print('All books have been deleted')
for i in range(0, len(books_list)):
    print(books_list[i])

# Membuat Data List baru dengan Comperhension

print('\nMake a new_book_list with Comperhension Ganjil')
books_list = ['1 Deadly 7 Sins','2 Atomic habits','3 Law of Power','4 Raja Tempe','5 Madilog','6 Gerpolek']
new_book_list = books_list[0::2]
for i in range(0, len(new_book_list)):
    print(new_book_list[i])

print('\nMake a new_book_list with Comperhension Genap')
new_book_list = books_list[1::2]
for i in range(0, len(new_book_list)):
    print(new_book_list[i])
