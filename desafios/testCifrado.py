from cifrados.rotn import rotEncriptar, rotDesencriptar
from cifrados.vigenere import vigenereEncriptar, vigenereDesencriptar

def cifrado(texto_original):
    clave_vigenere = "esta es mi clave vigenere"

    texto_encriptado_rot15 = rotEncriptar(texto_original, 15)
    
    texto_vigenere = vigenereEncriptar(texto_encriptado_rot15, clave_vigenere)
    
    texto_encriptado_rot7 = rotEncriptar(texto_vigenere, 7)
    
    texto_desencriptado_rot7 = rotDesencriptar(texto_encriptado_rot7, 7)
    
    texto_desencriptado_vigenere = vigenereDesencriptar(texto_desencriptado_rot7, clave_vigenere)
    
    texto_desencriptado_rot15 = rotDesencriptar(texto_desencriptado_vigenere, 15)
    
    return texto_desencriptado_rot15

def main():
    texto_original = "El mensaje esta correctoO"
    
    print("")
    print("Texto Original:", texto_original)
    print("Texto Cifrado rot15:", rotEncriptar(texto_original, 15))
    print("Texto Cifrado vigenere:", vigenereEncriptar(rotEncriptar(texto_original, 15), "esta es mi clave vigenere"))
    print("Texto Cifrado rot7:", rotEncriptar(vigenereEncriptar(rotEncriptar(texto_original, 15), "esta es mi clave vigenere"), 7))
    print("Texto Descifrado rot7:", rotDesencriptar(rotEncriptar(vigenereEncriptar(rotEncriptar(texto_original, 15), "esta es mi clave vigenere"), 7), 7))
    print("Texto Cifrado:", cifrado(texto_original))
    print("")   

def Ejecutartest():
    main()

