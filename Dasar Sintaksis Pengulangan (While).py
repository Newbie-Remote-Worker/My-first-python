"""
Semua Sintakis bahasa pemrograman terdiri dari 3 yaitu:
1. Sekuensial: Langkah berurutan
2. Pecabangan: Langkah melompat bila kondisi terpenuhi
3. Pengulangan: Mengulang langkah bila kondisi terpenuhi
"""

# 3. Pengulangan

all_books = 10
print('mom said, "read all books"')

have_been_read_books = 0
print(f'have been read books {have_been_read_books}')

while have_been_read_books < all_books:
    have_been_read_books = have_been_read_books + 1
    print(f'read unread books no {have_been_read_books}')

print(f'all books {have_been_read_books} have been read')
