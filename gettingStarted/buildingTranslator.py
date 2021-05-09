def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translator(input("Enter a phrase \n")))
"""
    Jadi tuh ini logikanya kita enter misalkan lala => maka pertanya akan di cek dari index 0 apakah termasuk dari AEIOUaeiou kalau tidak maka simpan l kedalam variable translation lalu selanjutnya cek index selanjutnya yaitu a apakah termasuk, kalau termasuk maka akan ditambahkan ke translation huruf g bukan huruf si letter dan begitu terus hingga selesai 
"""
