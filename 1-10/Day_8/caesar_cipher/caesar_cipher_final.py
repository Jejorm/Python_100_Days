from art import logo


def caesar(input_text, shift_amount, cipher_direction):
    text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for value in input_text:
        if value in alphabet:
            letter_index = alphabet.index(value)
            position = letter_index + shift_amount
            text += alphabet[position]
        else:
            text += value
    print(f"the {cipher_direction}d text is {text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26

    caesar(input_text=text, shift_amount=shift, cipher_direction=direction)
    
    result = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")
