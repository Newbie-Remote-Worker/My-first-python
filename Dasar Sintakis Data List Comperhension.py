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
