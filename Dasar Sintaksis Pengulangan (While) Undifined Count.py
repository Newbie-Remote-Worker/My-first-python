"""
Semua Sintakis bahasa pemrograman terdiri dari 3 yaitu:
1. Sekuensial: Langkah berurutan
2. Pecabangan: Langkah melompat bila kondisi terpenuhi
3. Pengulangan: Mengulang langkah bila kondisi terpenuhi
"""

# 3. Pengulangan

total_books = 10
print('mom said, "read all books"')

have_been_read_and_understanding_books = 0
total_reread_books = have_been_read_and_understanding_books * 2
print(f'have been read books {have_been_read_and_understanding_books}')

while total_reread_books < total_books:
    total_reread_books = total_reread_books + 1
    if have_been_read_and_understanding_books == 9:
        print(f'books {have_been_read_and_understanding_books + 1} dont understand')
    else:
         have_been_read_and_understanding_books = have_been_read_and_understanding_books + 1
         print(f'have been read and understand {have_been_read_and_understanding_books} books')

if have_been_read_and_understanding_books == total_books:
    print('all books have been read and understand Mom')
else:
    print(f'not all books i can understand, i only can understand {have_been_read_and_understanding_books}')


