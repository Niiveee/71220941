print('Selamat datang di program pembuat piramida berlubang')
a = int(input('masukan angka: '))

ruang = a-1 
for i in range(a):
    print(' '*ruang, end='')
    print('*' if i == 0 else '**' if i != 0 and i != a-1 else '*'*(a*2-1))
    ruang -= 1