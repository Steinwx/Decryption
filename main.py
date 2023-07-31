def decrypt_string(encrypted_string):
    decryption_dict = {'*': 'a', '&': 'e', '#': 'i', '+': 'o', '!': 'u'}
    decrypted_string = ''

    for char in encrypted_string:
        if char in decryption_dict:
            decrypted_string += decryption_dict[char]
        else:
            decrypted_string += char

    return decrypted_string


def main():
    encrypted_string = input("Enter a string to decrypt: ")
    decrypted_string = decrypt_string(encrypted_string)
    print("The Plain Text:", decrypted_string)


if __name__ == "__main__":
    main()
