#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(input_text, shift_amount, cipher_direction):
    text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in input_text:
        letter_index = alphabet.index(letter)
        position = letter_index + shift_amount
        text += alphabet[position]
    print(f"the {cipher_direction}d text is {text}")
        


caesar(input_text=text, shift_amount=shift, cipher_direction=direction)