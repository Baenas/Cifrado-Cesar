import string

pos = 3
entrada = "hola adios"
letras = string.ascii_lowercase
resultado = ''
def cifrar(entrada, pos):
     salida = []
     for y in entrada.lower():
            if y in letras:
                        index = letras.index(y)
                        nueva_letra = letras[(index + pos) % len(letras)]
                        salida.append(nueva_letra)
            else:
                salida.append(y)
                
     print(''.join(salida))       
     return ''.join(salida)
                    

cifrar(entrada, pos)

