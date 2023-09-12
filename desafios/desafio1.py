# Desafío 1
import requests
import json

from cifrados.rotn import rotEncriptar, rotDesencriptar
from cifrados.vigenere import vigenereEncriptar, vigenereDesencriptar

def desafio1(texto_original):
    clave_vigenere = "cvqnoteshrwnszhhksorbqcoas"

    texto_encriptado_rot15 = rotEncriptar(texto_original, 15)
    
    texto_vigenere = vigenereEncriptar(texto_encriptado_rot15, clave_vigenere)
    
    texto_encriptado_rot7 = rotEncriptar(texto_vigenere, 7)
    
    return texto_encriptado_rot7

def main():
    headers = {
    'Content-Type': 'text/plain',
    }
    
    texto_original = "hola mundo"
    
    data = '{"msg":"' + desafio1(texto_original) + '"}'

    respuesta = requests.post('http://finis.malba.cl/SendMsg', headers=headers, data=data)

    if respuesta.status_code == 200:
        respuesta_data = json.loads(respuesta.text)
        textoDecifrado = respuesta_data["msg"]
        
        print("")
        print("Texto Original:", texto_original)
        print("Texto Cifrado:", desafio1(texto_original))
        print("Texto Decifrado:", textoDecifrado)
        print("")

    else:
        print("Error al obtener el mensaje cifrado")

def EjecutarDesafio1():
    main()

