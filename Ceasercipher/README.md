# Caesar Cipher Encryption and Decryption

The Caesar cipher is a simple and widely used encryption technique. It shifts each letter of the plaintext message by a certain number of positions down the alphabet.

## Encryption Process

To encrypt a message using the Caesar cipher:
1. Determine the shift amount (the number of positions each letter should be shifted).
2. Iterate through each letter in the plaintext message.
3. Shift each letter forwards in the alphabet by the shift amount.
4. Print or return the encrypted message.

### Example
```python
# Plain text and shift amount
plain_text = "hello"
shift = 5

# Encryption function
def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            cipher_text += shifted_char
        else:
            cipher_text += char
    return cipher_text

# Encrypt the message
cipher_text = encrypt(plain_text, shift)
print(f"The encrypted text is {cipher_text}")  # Output: "The encrypted text is mjqqt"
```

### Bug Alert
Be cautious when encrypting words like "civilization" with the Caesar cipher, as it may not preserve spaces or handle punctuation correctly.

## Decryption Process

Decryption of a Caesar cipher message is essentially the reverse of the encryption process. Instead of shifting letters forwards, we shift them backward by the same amount.

### Example
```python
# Cipher text and shift amount
cipher_text = "mjqqt"
shift = 5

# Decryption function
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

# Decrypt the message
decrypted_text = decrypt(cipher_text, shift)
print(f"The decrypted text is {decrypted_text}")  # Output: "The decrypted text is hello"
```

## Usage
1. Choose a shift amount for encryption and decryption.
2. Call the `encrypt()` function to encrypt a message.
3. Call the `decrypt()` function to decrypt an encrypted message.

Feel free to experiment with different shift amounts and messages. 🚀