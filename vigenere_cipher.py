
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# decode vigenere cipher with key

def decode_vigener(cipher, key):

    # check that message does not contain numbers
    if any(char.isdigit() for char in cipher):
        print("The ciphered message cannot contain numbers")
        exit()

    if any(char.isdigit() for char in key):
        print("The cipher key cannot contain numbers")
        exit()

    # change letters uppercase
    key = key.upper()
    cipher = cipher.upper()
    # remove spaces from the string
    cipher = cipher.replace(" ","")
    
    # key length
    key_length = len(key)

    # plain text string
    plaintext_message = ""

    # key letters in numbers as a list
    key_as_list = []

    # find key letters in numbers

    for letter in key:
        #print(letter)
        if letter in alphabet:
            key_as_list.append(alphabet.index(letter))
        else:
            print("The key can contain only English alphabet letters")


    # decode vigenere
            
    for i in range(0, len(cipher), key_length):

        # key length group of characters from the cipher text
        key_length_group = cipher[i:i+key_length]
        
        # index
        k = 0

        # decode cipher
        for n in key_length_group:
            
            # cipher letter index in alphabet
            cipher_letter_index = alphabet.index(n)
            
            # decode letter to plain text
            letter_in_plain_text = cipher_letter_index - key_as_list[k]
            
            # if letter index is negative, take letter from backwards from the alphabets
            if letter_in_plain_text < 0:
                letter_in_plain_text = 26+letter_in_plain_text

            # add decoded letter to the plain text message
            plaintext_message = plaintext_message + alphabet[letter_in_plain_text]

            # increase index
            k = k + 1



    return plaintext_message


def main():

    
    cipher_text = input("Give a text to decode >>>> ")
    cipher_key = input("Give a cipher key >>>> ")

    print(decode_vigener(cipher_text, cipher_key))

main()