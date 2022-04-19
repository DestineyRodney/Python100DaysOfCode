

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt (text, shift):
    encoded = ""

    for char in text:
        postion = alphabet.index(char)
        new_postion = postion + shift
        encoded += alphabet[new_postion]
    print(f"The encoded text is: {encoded}")


def decrypt(text_input, shift_number):
    decoded = ""
    for char in text_input:
        position = alphabet.index(char)
        new_position = position - shift_number
        decoded += alphabet[new_position]
    print(f"The decoded text is: {decoded}")


if direction == "encode":
    encrypt(text=text, shift=shift)
elif direction == "decode":
    decrypt(text_input=text, shift_number=shift)
else:
    print("Please enter encode or decode to recieve your message")

