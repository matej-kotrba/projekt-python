'''
Proměnné v Pythonu
Python je typově odvozovaný jazyk, proto nemusíme explicitně definovat typ proměnné.
Typ proměnné je určen na základě přiřazené hodnoty.
Pro přiřazení hodnoty proměnné se používá znak rovnítko ("=").
'''

# Proměnné v Pythonu - primitivní datové typy
# Je zvykem používat podtržítko u víceslovných názvů proměnných.
students_count = 1000
rating = 4.99
# Hodnota může být přiřazena i více proměnným najednou:
x = y = z = 0

# Boolean hodnota musí začínat velkým písmenem
is_published = False

# Python obsahuje i speciální literál None - nulovou hodnotu
iq = None
# print('Jeho IQ = ', iq)

'''
V Pythonu se ale ve skutečnosti nepřiřazují do proměnných hodnoty, ale jen reference na objekt (hodnotu).
Každý objekt (instance třídy) má jedinečnou hodnotu (value), typ (type) a identitu (ID).
Proto i typy proměnných poukazují na určitou výchozí třídu, z níž byl objekt vytvořen. 
Identita objektu je vyjádřena jeho identifikačním číslem (ID), které je adresou paměťového místa, ve kterém je hodnota uložena. 
Některé objekty mohou mít explicitně přiřazené jméno, obecně označované jako proměnná:
'''

'''Úkol A'''
#? Najděte na Internetu, jakými funkcemi lze v Pythonu zjistit
#? a) typ objektu - type
#? b) identitu objektu (jeho adresu v paměti) - hex(id(x))
#? Ukažte to na příkladech proměnných students_count, rating, is_published a vypište výstupy do konzole

print("Typ: " + str(type(students_count)), "ID: " + str(hex(id(students_count))))
print("Typ: " + str(type(rating)), "ID: " + str(hex(id(rating))))
print("Typ: " + str(type(is_published)), "ID: " + str(hex(id(is_published))))

# Numerické operátory
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# Zbytek po celočíselném dělení
# print(10 % 3)
# Celočíselné dělení
# print(10 // 3)
# Mocnina
# print(2 ** 10)

'''
Příklady použití numerických literálů (numeric literals)
'''
binary = 0b1010 #Binary Literals
octal = 0o310 #Octal Literal
decimal = 100 #Decimal Literal
hexadecimal = 0x12c #Hexadecimal Literal

# print(binary, octal, decimal, hexadecimal)
# Převod desítkového čísla na binární, oktalové a hexadecimální
# print(bin(255), oct(255), hex(255))


# Převod binárního čísla na desítkové
# print(int('0100', base=2))
# Převod hexadecimálního čísla na desítkové
# print(int('100', base=16))


'''Úkol B'''
#? Vypište do poznámky všechny bitové operátory, které nabízí Python - AND, OR, not, XOR
#? Do proměnné myself_binary uložte binární číslo vytvořené na základě osmi prvních znaků z vašeho jména a příjmení (souhláska = 1, samohláska 0)
#? Příklad - HildaDok: 10110101
#? Vypište toto binární číslo v desítkové soustavě
#? Pro toto binární číslo proveďte nejprve bitový posun o 2 bity vpravo, poté vypište výsledek v desítkové soustavě
#? Proveďte bitový součin hexadecimálního čísla "1A" a vašeho binárního čísla a opět vypište v desítkové soustavě
#? Výsledek zobrazte jako formátovaný řetězec - např. "Binární součin čísla 0b11010 a 0b10110101 je 0b10000"

myself_binary = 0b10101101

print(int(myself_binary))

myself_binary >>= 2

print(myself_binary)

c1 = int(0x1A)
c2 = int(myself_binary)
res = c1 & c2
print(res)

print(f"Binární součin čísla 0b11010 a 0b10110101 je {int(0b11010) & 0b10110101}")

'''Python plně podporuje operace v plovoucí řádové čárce (tj. desetinná čísla). 
Operátor pracující s různými typy operandů si nejprve zkonvertuje celá čísla na čísla 
v plovoucí řádové čárce a následně provede výpočet (obdobné chování jako v jazyce C).
Výsledek je vždy desetinné číslo.
'''
#Float Literal
float_1 = 10.5
float_2 = 1.5e2 # Zápis reálného čísla pomocí exponentu = 1.5 * (10 ** 2)
#print(float_1 + float_2)


# Použití vestavěných matematických funkcí
# print(round(rating))
# Použití importovaného modulu math a jeho metod
import math
# print(math.floor(rating))
# print(math.cos(45))

# Zjištění datového typu
# x = input("x: ")
# Vrátí typ str - proto je nutná typová konverze - int(), float()
# Typová konverze
# print(int(x) + 20)

# Komplexní čísla a Python
'''Python plně podporuje komplexní čísla, přičemž imaginární číslo je zapisováno s příponou "j" nebo "J". 
Komplexní čísla zapisujeme ve tvaru "(Re + Imj)" nebo je můžeme vytvořit pomocí interní funkce "complex(Re, Im)":
'''
#Complex Literal
complex = 3.14j

'''Komplexní čísla jsou vždy reprezentována dvojicí desetinných čísel, reálnou a imaginární částí. 
Chceme-li získat velikosti těchto částí čísla z, použijeme zápisu z.real a z.imag:'''
# z = 4.5 + 0.5j
# print(z, z.imag, z.real)

'''Poněvadž v matematice neexistuje způsob, jak převést komplexní číslo na reálné, 
ani Python nedovoluje použití konverzních funkcí float(), int() a long() s komplexním argumentem. 
Raději použijte funkci abs(z) pro získání absolutní hodnoty komplexního čísla, 
nebo zápis z.real reprezentují reálnou část čísla: 
'''
# Následující řádek vyvolá chybu
# print(float(z))
#
# print(abs(z))
# Je totéž jako sqrt(z.real**2 + z.imag**2)

'''
Funguje pouze  v interaktivní konzoli!
Speciální proměnná _ reprezentuje předešlý výsledek.

>>> urok = 12.5 / 100
>>> penize = 100.50
>>> penize * urok
12.5625
>>> penize + _
113.0625
>>> round(_, 2)
113.06
>>>

Varování: Hodnota proměnné _ by nikdy neměla být modifikována uživatelem. 
Pokud byste jí přiřadili hodnotu, vytvořili byste nezávislou lokální proměnnou se stejným jménem, 
která by zakryla interní proměnnou s tímto chováním.'''


