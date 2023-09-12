# Función para cifrar un mensaje utilizando ROT
def rotEncriptar(texto, desplazamiento):
    encrypt_text = [] # Lista para almacenar caracteres cifrados
    for char in texto:
        if 'A' <= char <= 'Z':
            # Cifrado de letras mayúsculas
            x = (ord(char) - ord('A') + desplazamiento) % 26
            x += ord('A')
            encrypt_text.append(chr(x))
        elif 'a' <= char <= 'z':
            # Cifrado de las letras minúsculas
            x = (ord(char) - ord('a') + desplazamiento) % 26
            x += ord('a')
            encrypt_text.append(chr(x))
        else:
            encrypt_text.append(char)
    return "".join(encrypt_text)

# Función para descrifrar un mensaje cifrado utilizando ROT
def rotDesencriptar(texto, desplazamiento): # Lista para almancenar caracteres descifrados
    decrypt_text = []
    for char in texto:
        if 'A' <= char <= 'Z':
            # Descrifrado de letras mayúsculas
            x = (ord(char) - ord('A') - desplazamiento) % 26
            x += ord('A')
            decrypt_text.append(chr(x))
        elif 'a' <= char <= 'z':
            # Descrifrado de letras minúsculas
            x = (ord(char) - ord('a') - desplazamiento) % 26
            x += ord('a')
            decrypt_text.append(chr(x))
        else:
            decrypt_text.append(char)
    return "".join(decrypt_text)