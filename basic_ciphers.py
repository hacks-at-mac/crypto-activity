def char_to_num(c):
    return ord(c.upper()) - 64

def num_to_char(n):
    # Make sure that shift isn't greater than 26
    n = n % 26
    if n == 0:
        n = 26
    return chr(n + 64)



def caesar_encrypt(s, shift):
    ciphertext = ""
    for c in s:
        ciphertext += num_to_char(char_to_num(c) + shift)
    return ciphertext

plaintext = "THISISANIMPORTANTPLAINTEXT"
#print(caesar_encrypt(plaintext, 13))

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for c in ciphertext:
        plaintext += num_to_char(char_to_num(c) - shift)
    return plaintext

ciphertext = caesar_encrypt(plaintext, 13)
#for shift in range(1, 26):
    #print(caesar_decrypt(ciphertext, shift))











def extend_key(key, length):
    extended_key = ""
    for i in range(0, length):
        extended_key += key[i % len(key)]
    return extended_key


def vigenere_encrypt(s, key):
    ciphertext = ""
    full_key = extend_key(key, len(s))
    #print(full_key)
    for i in range(len(s)):
        ciphertext += num_to_char(char_to_num(s[i]) + char_to_num(full_key[i]))
    return ciphertext

plaintext = "THISISANIMPORTANTPLAINTEXT"
print(vigenere_encrypt(plaintext, "Z"))


def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    full_key = extend_key(key, len(ciphertext))
    #print(full_key)
    for i in range(len(ciphertext)):
        plaintext += num_to_char(char_to_num(ciphertext[i]) - char_to_num(full_key[i]))
    return plaintext


print(vigenere_decrypt(vigenere_encrypt(plaintext, "VERYSECUREPASSWORD"), "PASSWORD"))

def retrieve_key(plaintext, ciphertext):
    key = ""
    for i in range(len(plaintext)):
        key += num_to_char(char_to_num(ciphertext[i]) - char_to_num(plaintext[i]))
    return key

print(retrieve_key(plaintext, vigenere_encrypt(plaintext, "PASSWORD")))



#
