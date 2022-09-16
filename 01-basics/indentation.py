'''
Odsazování v Pythonu (indentation)

Většina programovacích jazyků jako C, C++, Java nebo JavaScript používá k vymezení bloků kódu složené závorky (braces).
V Pythonu se používá odsazování. Blok kódu (např. tělo funkce, cyklu atd.) tedy začíná s odsazením a končí prvním
neodsazeným řádkem.
Počet mezer v odsazení je libovolný, ale musí být konzistentní aspoň v rámci jednoho bloku.
K odsazení musí být použita minimálně jedna mezera.
Obvykle se k odsazování používá tubulátor, který bývá nejčastěji nastaven na 4 mezery.
'''

# Odsazení bloku kódu uvnitř cyklu a podmínky
for i in range(1, 10):
    print(i)
    if i % 2 == 0:
        print('even')
    else:
        print('odd')

'''
Dokumentační řetězce v Pythonu (docstrings)

Víceřádkový řetězec následující hned po záhlaví funkce v Pythonu je nazýván docstring (documentation string neboli 
dokumentační řetězec) a obsahuje stručné vysvětlení toho, co funkce provádí.
Přestože je to nepovinný doplněk programového kódu, je považován za "good programming practice", tedy jednu z dobrých
zásad, které by měl programátor v Pythonu dodržovat.
Docstrings se zapisují mezi trojnásobné uvozovky (tedy podobně jako komentáře).
Tyto dokumentační řetězce jsou přístupné prostřednictvím "magického" __doc__ atributu funkce.    
'''


# Odsazení bloku kódu uvnitř funkce a použití docstring
def greet(name):
    """
    This function greets to the person
    passed in as a parameter
    """
    print("Ahoj, " + name + "!")


# Vypíše docstring spojený s funkcí greet
print(greet.__doc__)
# Vyvolá funkci greet s parametrem 'Hilda'
greet('Hilda')

"""
Cvičení 2:

Vytvořte libovolně pojmenovanou vlastní funkci s minimálně jedním parametrem, v níž využijete cyklus for, 
aspoň jednu podmínku if a funkci print(). Dodržte správné odsazování kódu a opatřete funkci stručnou dokumentací.
Do konzole vypište nejprve docstring vaší funkce a potom zavolejte funkci samotnou.   
"""

array = [1,1,1,1,1,1,1,1,1]


def change_array(array, arrayLength, startIndex, shouldCopy):
    """
        This function will fill array with numbers,
        expecting that you have already created indexes and won't leave array.
        array - array you want to change
        arrayLength - how many indexes you want to change
        startIndex - index you want to start on
        shouldCopy - if true, return new array without affecting the old one
    """
    assert len(array) > startIndex + arrayLength
    new_array = array[:] if shouldCopy else array
    if arrayLength <= startIndex:
        print("Incorrect combination of arrayLength and startIndex")
        return
    for k in range(startIndex, arrayLength):
        new_array[k] = k
        print(f"Created new value of {i} in the array.")
    return new_array


print(change_array.__doc__)
print(change_array(array, 5, 1, True))
print(array)
