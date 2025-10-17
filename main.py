import string
import argparse

letras = string.ascii_lowercase

def cifrar(entrada, pos, operacion):
     salida = []
     for y in entrada.lower():
            if y in letras:
                        index = letras.index(y)
                        status = index + pos if operacion == 'cifrar' else index - pos
                        nueva_letra = letras[( status) % len(letras)]
                        salida.append(nueva_letra)
            else:
                salida.append(y)
                
     print(''.join(salida))        
     return ''.join(salida)
             
parser = argparse.ArgumentParser(description='Encriptación Cesar')
parser.add_argument('-i', '--indice', type=int, help='Indice ')
parser.add_argument('-o', '--operacion', type=str, choices=['cifrar', 'descifrar'],
                    default='cifrar', required=True,
                    help='Operación para cifrar')

parser.add_argument('-texto','-t', type=str, required=True,
                    help='Texto a cifrar')

args = parser.parse_args()

if args.operacion == 'cifrar':
        cifrar(args.texto, args.indice, args.operacion)
elif args.operacion == 'descifrar':
        cifrar(args.texto, args.indice , args.operacion)
