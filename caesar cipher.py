def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                result += chr((ord(char) - start + shift_amount) % 26 + start)
            elif char.isupper():
                start = ord('A')
                result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                result += chr((ord(char) - start - shift_amount) % 26 + start)
            elif char.isupper():
                start = ord('A')
                result += chr((ord(char) - start - shift_amount) % 26 + start)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice!")
        return

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        encrypted_text = encrypt(text, shift)
        print("Encrypted text:", encrypted_text)
    elif choice == 'D':
        decrypted_text = decrypt(text, shift)
        print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()