"""
Semua Sintakis bahasa pemrograman terdiri dari 3 yaitu:
1. Sekuensial: Langkah berurutan
2. Pecabangan: Langkah melompat bila kondisi terpenuhi
3. Pengulangan: Mengulang langkah bila kondisi terpenuhi
"""

# 3. Pengulangan

jumlah_buku = 100
print('mom said, "read all books"')

read_books = 0
print(f'read books {read_books}')

for read_books in range(1, 101):
    print(f'books {read_books}, read books')

print(f'read books {read_books}')


