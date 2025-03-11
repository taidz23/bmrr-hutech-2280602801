<<<<<<< HEAD
class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        decrypted_text = [''] * key
        row, col = 0, 0
        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1
=======
class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        decrypted_text = [''] * key
        row, col = 0, 0
        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1
>>>>>>> 31c7f4ddc75f823439ad7ca8ef6c553f792c5ec7
        return ''.join(decrypted_text)