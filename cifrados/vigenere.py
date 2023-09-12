def vigenereEncriptar(texto, clave):
    encrypt_text = []
    for i in range(len(texto)):
        if 'A' <= texto[i] <= 'Z':
            x = (ord(texto[i]) + ord(clave[i % len(clave)]) - 2 * ord('A')) % 26
            x += ord('A')
            encrypt_text.append(chr(x))
        elif 'a' <= texto[i] <= 'z':
            x = (ord(texto[i]) + ord(clave[i % len(clave)]) - 2 * ord('a')) % 26
            x += ord('a')
            encrypt_text.append(chr(x))
        else:
            encrypt_text.append(texto[i])
    return "".join(encrypt_text)

def vigenereDesencriptar(texto, clave):
    decrypt_text = []
    for i in range(len(texto)):
        if 'A' <= texto[i] <= 'Z':
            x = (ord(texto[i]) - ord(clave[i % len(clave)]) + 26) % 26
            x += ord('A')
            decrypt_text.append(chr(x))
        elif 'a' <= texto[i] <= 'z':
            x = (ord(texto[i]) - ord(clave[i % len(clave)]) + 26) % 26
            x += ord('a')
            decrypt_text.append(chr(x))
        else:
            decrypt_text.append(texto[i])
    return "".join(decrypt_text)