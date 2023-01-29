alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            shifted_index = (char_index + shift) % len(alphabet)
            encrypted_text += alphabet[shifted_index]
        else:
            encrypted_text += char
    return encrypted_text

while True:
    action = input("Choose Mod: (E)encryption/(D)decrypt/(Q)quit ==>  ")
    if action.lower() == "e":
        text = input("Enter Text: ")
        shift = int(input("Enter Shift: "))
        print(caesar_cipher(text, shift))
    elif action.lower() == "d":
        text = input("Enter Text: ")
        shift = int(input("Enter Shift: "))
        print(caesar_cipher(text, shift, decrypt=True))
    elif action.lower() == "q":
        break
    else:
        print("Invalid input")
