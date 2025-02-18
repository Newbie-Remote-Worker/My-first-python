"""
Semua Sintakis bahasa pemrograman terdiri dari 3 yaitu:
1. Sekuensial: Langkah berurutan
2. Pecabangan: Langkah melompat bila kondisi terpenuhi
3. Pengulangan: Mengulang langkah bila kondisi terpenuhi
"""

#sekuensial
print('Mom said, "go to grocery store"')
print('Acong reply, "oke, what do i do?"')
print('Mom said, "buy a bottle of milk')
print('Acong going to grocery store')
print('Acong searching for the bottle of milk')
print('Acong checked the price of milk, he had enough money')
print('Acong searching for the eggs')
print('Acong checked the price of eggs, he still had enough money')
print('Acong goes shopping')

# Percabangan
bottle_of_milk_in_grocery = 20
eggs_in_grocery = 100

print(f'bottle of milk {bottle_of_milk_in_grocery} btl')
print(f'eggs in grocecy {eggs_in_grocery} btr')

if bottle_of_milk_in_grocery > 0:
    print('Acong checked the price of milk, and found that he had enough money. ')
    if eggs_in_grocery > 0:
         print('Acong bought 1 btl')
         print('Acong bought 6 btr')
    else:
        print('Acong bought 1 btl')
        print('Acong did not bought 6 btr')
else:
    print('Acong did not bought btl and btr')

print('came home and gave the groceries to his mom')
Done