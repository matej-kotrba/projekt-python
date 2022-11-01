def char_frequency(txt):
    return sorted([(char, txt.count(char)) for char in set(txt)], reverse=True, key=lambda x: x[1])

print(char_frequency("aijdajdhbcybxbcyxc"))

def read_txt_file(filename):
    f = open(filename, "r", encoding="utf8")
    return f.read()

def write_txt_file(filename, txt):
    f = open(filename, "w", encoding="utf8")
    f.write(txt)
    f.close()
    return

print(read_txt_file('list.py'))
pokus = "adajhdahšč  ščšhdajsh da"
print(char_frequency(read_txt_file("list.py")))

write_txt_file("frekvence.txt", str(char_frequency(read_txt_file("dictionary.py"))))