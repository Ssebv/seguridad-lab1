# Función para cifrar un mensaje utilizando el cifrado vigenere
def vigenereEncriptar(texto, clave):
    encrypt_text = [] # Lista para almacenar caracteres cifrados
    for i in range(len(texto)):
        if 'A' <= texto[i] <= 'Z':
            # Cifrado de letras mayúsculas
            x = (ord(texto[i]) + ord(clave[i % len(clave)]) - 2 * ord('A')) % 26
            x += ord('A')
            encrypt_text.append(chr(x))
        elif 'a' <= texto[i] <= 'z':
            # Cifrado de letras minúsculas
            x = (ord(texto[i]) + ord(clave[i % len(clave)]) - 2 * ord('a')) % 26
            x += ord('a')
            encrypt_text.append(chr(x))
        else:
            encrypt_text.append(texto[i])
    return "".join(encrypt_text)

# Función para descifrar un mensaje utilizando el cifrado vigenere
def vigenereDesencriptar(texto, clave):
    decrypt_text = [] # Lista para almacenar caracteres descifrados
    for i in range(len(texto)):
        if 'A' <= texto[i] <= 'Z':
            # Descifrado de letras mayúsculas
            x = (ord(texto[i]) - ord(clave[i % len(clave)]) + 26) % 26
            x += ord('A')
            decrypt_text.append(chr(x))
        elif 'a' <= texto[i] <= 'z':
            # Descifrado de letras minúsculas
            x = (ord(texto[i]) - ord(clave[i % len(clave)]) + 26) % 26
            x += ord('a')
            decrypt_text.append(chr(x))
        else:
            decrypt_text.append(texto[i])
    return "".join(decrypt_text)