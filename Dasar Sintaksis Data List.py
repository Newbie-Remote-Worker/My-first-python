"""
Dasar Data List
"""

books_list = ['Atomic habits','7 Deadly Sins','48 Law of Power']
print('showing variable books_list')
print(books_list)

print('proces all with for in')
for book in books_list:
    print (book)

print('\nShow all books list on some index')
print(books_list[0])
print(books_list[1])
print(books_list[2])

print('\nShow all books list with for in range')
for n in range(0, len(books_list)):
    print(books_list[n])