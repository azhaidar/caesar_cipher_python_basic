alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            shifter_pos = (alphabet.index(letter) + shift) % 26
            cipher_text += alphabet[shifter_pos]
        else:
            cipher_text += letter
    print(f"hasil enkripsinya adalah {cipher_text}")

def decrypt(text, shift):
    decipher_text = ""
    for letter in text:
        if letter in alphabet:
            shifter_pos = (alphabet.index(letter) - shift) % 26
            decipher_text += alphabet[shifter_pos]
        else:
            decipher_text += letter
    print(f"hasil nya {decipher_text}")

def decrypt_unknown(text):
    for shift in range(26):
        decipher_text = ""
        for letter in text:
            if letter in alphabet:
                shifter_pos = (alphabet.index(letter) - shift) % 26
                decipher_text += alphabet[shifter_pos]
            else:
                decipher_text += letter
            print(f"hasil deskripsinya adalah decipher {decipher_text}")
    


status = input("ketik 1 untuk berhenti: ")
while status != "1":
# Input user
    text = input("masukkan teksnya\n").lower()
    print("ketik 1 untuk enkripsi \nketik 2 untuk decode \nketik 3 untuk decode unknown")
    direction = int(input("masukkan pilihan "))

    match direction:
        case 1:
            shift = int(input("masukkan shiftnya\n"))
            encrypt(text, shift)
        case 2:
            shift = int(input("masukkan shiftnya\n"))
            decrypt(text, shift)
        case 3:
            decrypt_unknown(text)
        case _:
            print("Pilihan tidak valid!")
    status = input("ketik 1 untuk berhenti: ") 
