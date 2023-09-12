# Desafio 2
import requests
import json

from cifrados.rotn import rotEncriptar, rotDesencriptar
from cifrados.vigenere import vigenereEncriptar, vigenereDesencriptar

def desafio2(texto_cifrado):

    clave_vigenere = "aobkqolrzsrigpknkufezioer"

    # Descifrar el texto cifrado con ROT7
    texto_descifrado_rot7 = rotDesencriptar(texto_cifrado, 7)

    # Descifrar el texto descifrado con Vigenere
    texto_descifrado_vigenere = vigenereDesencriptar(texto_descifrado_rot7, clave_vigenere)

    # Descifrar el texto descifrado con ROT15
    texto_descifrado_rot15 = rotDesencriptar(texto_descifrado_vigenere, 15)

    # Imprimir el texto original, cifrado y descifrado
    print("Texto descifrado con ROT(-7):", texto_descifrado_rot7)
    print("Texto descifrado con Vigenere:", texto_descifrado_vigenere)
    print("Texto descifrado con ROT(-15):", texto_descifrado_rot15)
    print("")

def main():
    headers = {
        'Content-Type': 'text/plain',
    }

    respuesta = requests.get('http://finis.malba.cl/GetMsg', headers=headers)

    if respuesta.status_code == 200:
        respuesta_data = json.loads(respuesta.text)
        textoCifrado = respuesta_data["msg"]
        
        print("")
        print("Texto cifrado:", textoCifrado)
        print("")

        desafio2(textoCifrado)

    else:
        print("Error al obtener el mensaje cifrado")

def EjecutarDesafio2():
    main()