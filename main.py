def decrypt_string(encrypted_string, decryption_dict):
    """
    Decrypts an encrypted string using the provided decryption dictionary.

    Args:
        encrypted_string (str): The string to be decrypted.
        decryption_dict (dict): A dictionary mapping encrypted characters to their plain text counterparts.

    Returns:
        str: The decrypted plain text string.
    """
    decrypted_string = ''

    for char in encrypted_string:
        lower_char = char.lower()
        if lower_char in decryption_dict:
            if char.isupper():
                decrypted_string += decryption_dict[lower_char].upper()
            else:
                decrypted_string += decryption_dict[lower_char]
        else:
            decrypted_string += char

    return decrypted_string


def main():
    decryption_dict = {'*': 'a', '&': 'e', '#': 'i', '+': 'o', '!': 'u'}

    encrypted_string = input("Enter a string to decrypt: ")

    # Validate user input
    if not encrypted_string:
        print("Error: Please provide a valid encrypted string.")
        return

    decrypted_string = decrypt_string(encrypted_string, decryption_dict)

    print("The Plain Text:", decrypted_string)


if __name__ == "__main__":
    main()
