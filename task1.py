def encrypt(text, shift):
    result = ""
    for letter in text:
        if letter >= 'A' and letter <= 'Z':
            new_pos = ord(letter) + shift
            if new_pos > ord('Z'):
                new_pos = new_pos - 26
            result = result + chr(new_pos)
        elif letter >= 'a' and letter <= 'z':
            new_pos = ord(letter) + shift
            if new_pos > ord('z'):
                new_pos = new_pos - 26
            result = result + chr(new_pos)
        else:
            result = result + letter
    return result

def decrypt(text, shift):
    result = ""
    for letter in text:
        if letter >= 'A' and letter <= 'Z':
            new_pos = ord(letter) - shift
            if new_pos < ord('A'):
                new_pos = new_pos + 26
            result = result + chr(new_pos)
        elif letter >= 'a' and letter <= 'z':
            new_pos = ord(letter) - shift
            if new_pos < ord('a'):
                new_pos = new_pos + 26
            result = result + chr(new_pos)
        else:
            result = result + letter
    return result

def main():
    while True:
        action = input("Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
        if action == 'q':
            break
        if action != 'e' and action != 'd':
            print("Please type 'e', 'd', or 'q' only!")
            continue
        message = input("Enter your message: ")
        shift_input = input("Enter shift number (1-25): ")
        if not shift_input.isdigit():
            print("Shift must be a number!")
            continue
        shift = int(shift_input)
        if shift < 1 or shift > 25:
            print("Shift must be between 1 and 25!")
            continue
        if action == 'e':
            encrypted = encrypt(message, shift)
            print("Encrypted message:", encrypted)
        else:
            decrypted = decrypt(message, shift)
            print("Decrypted message:", decrypted)

main()