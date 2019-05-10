Para analizar un a.out, ver su ELF es:

hexdump a.out -C


Igual con: 
El siguiente nos muestra el contenido del binario por secciones
# objdump -s a.out

Nos muestran los headers.
* objdump -x a.out

Para el desensamblaje se hace con la instrucción:
# objdump -d a.out