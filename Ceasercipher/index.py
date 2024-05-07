alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
ciphered_text = ''
def encrypt(shift_amount, word):
  for letter in word:
    position = alphabet.index(letter)
    new_position = (position + shift_amount)%26
    starting_point = alphabet[new_position]
    ciphered_text = starting_point
encrypt(shift_amount=shift, word = text)

def decrypt(text, shift):
  for letter in text:
    position = alphabet.index(letter)
    new_point = (position - shift) % 26
    new_word = alphabet[new_point]
    cipher_text = new_word
decrypt(text, shift)
print(f'New word is {ciphered_text}')