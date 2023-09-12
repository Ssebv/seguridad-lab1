## Integrantes

- Sebastian Allende
- Gian Franco Astorga

## Profesor

- Manuel Alba Escobar

## Descripción

Se creo un programa en python que permite cifrar y descifrar mensajes utilizando el cifrado de vigenere y rot, el programa se ejecuta con el siguiente comando:

```bash
python3 main.py
```

Al ejecutar el programa se mostrara un menu principal para imprimir el desafio 1 o el desafio 2, para seleccionar una opcion se debe ingresar el numero de la opcion y presionar enter.
Los mensajes esta declarados en cada desafio, para cambiar el mensaje se debe modificar el codigo.

## Requerimientos

- Python 3.11
- Pipenv (para instalar las dependencias)

## Enunciado

### Desafio 1 

el proceso de cifrado es el siguiente:

Mensaje de entrada 

- Rot(15)
- vigenere según el excel entregado con el password cvqnoteshrwnszhhksorbqcoas
- Rot(7)

Mensaje cifrado

el proceso de descifrado es el siguiente:

Mensaje  cifrado 

- Rot(-7)
- vigenere según con el password cvqnoteshrwnszhhksorbqcoas
- Rot(-15)

![image info](https://tutorialesenlinea.es/uploads/posts/2015-04/thumbs/1430403275_cuadro_vigenere.webp)


Mensaje de entrada

Sabiendo esto se le pide que cree  un mensaje propio y aplique los  pasos mencionados anteriormente con el mensaje cifrado envielo al servidor con el comando que esta a continuación


```bash
curl --location --request POST 'http://finis.malba.cl/SendMsg' \
--header 'Content-Type: text/plain' \
--data-raw '{"msg":"cifrado(mensaje)"}'
```

Puedes utilizar el siguiente sitio para generar codigo https://curlconverter.com/

### Desafio 2

Ejecute el siguiente mensaje

```bash
curl --location --request GET 'http://finis.malba.cl/GetMsg' --header 'Content-Type: text/plain'
```

con el mensaje recibido descifre el texto original aplicando los pasos anteriores pero cambiando la constraseña de  vigenere por aobkqolrzsrigpknkufezioer

