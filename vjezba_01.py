'''
IP adresa je adresa svakog računala na mreži koja se sastoji od četiri broja između 0 i 256.
Primjer IP adrese: 192.168.0.184

IP adresu iz primjera ispišite u binarnom, oktalno i heksadekadskom obliku.
SAVJET: Za sada koristite zasebnu varijablu za svaki od četiri broja, 
        odnosno dijela (okteta) IP adrese, ali ispišite ih u istom obliku 
        kako je navedeno u primjeru (192.168.0.184).
Ispis treba napraviti za sve oblike brojevnih sustava.
'''

a = 192
b = 168
c = 0
d = 184

binary = f'{bin(a)}.{bin(b)}.{bin(c)}.{bin(d)}'
octal = f'{oct(a)}.{oct(b)}.{oct(c)}.{oct(d)}'
hexa = f'{hex(a)}.{hex(b)}.{hex(c)}.{hex(d)}'

print()
print(f'Prikaz IP adrese {a}.{b}.{c}.{d} u binarnom zapisu je {binary}')
print(f'Prikaz IP adrese {a}.{b}.{c}.{d} u oktalnom zapisu je {octal}')
print(f'Prikaz IP adrese {a}.{b}.{c}.{d} u heksadekadskom zapisu je {hexa}')
