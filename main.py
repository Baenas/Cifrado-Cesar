import string   
import argparse
import os


letras = string.ascii_lowercase

def cifrar(entrada, pos, operacion):
     salida = []
     for y in entrada.lower():
            if y in letras:
                        index = letras.index(y)
                        status = int(index) + int(pos) if operacion == 'cifrar' else int(index) - int(pos) 
                        nueva_letra = letras[( status) % len(letras)]
                        salida.append(nueva_letra)
            else:
                salida.append(y)
                
     return ''.join(salida)

def interactivo():
       operaciones = ['cifrar', 'descifrar']
       os.system('cls')
       print(
'''
=======================
Operacion cifrar [1]
Operacion descifrar [2]
=======================
'''
                )
       operacion = input("Selecciona operacion: ")
       print("\nOpcion" , operaciones[int(operacion) - 1] ,"seleccionada\n")
       indice = input("Selecciona indice: ")
       print("\nIndice" , indice ,"\n")
       texto = input("Introduce texto: ")
       print("\nEl resultado despues de", operaciones[int(operacion) - 1] , "es:" ,  cifrar(texto, indice, operaciones[int(operacion) - 1]))
       
     # Do other stuff
       
             
parser = argparse.ArgumentParser(description='Encriptación Cesar')
parser.add_argument('-i', '--indice', type=int,  required=False, help='Indice ')
parser.add_argument('-o', '--operacion', type=str, choices=['cifrar', 'descifrar'],
                     required=False,
                    help='Operación para cifrar')

parser.add_argument('-texto','-t', type=str, required=False,
                    help='Texto a cifrar')

args = parser.parse_args()

if args.operacion == 'cifrar':
        print("\nEl resultado despues de", args.operacion , "es:" ,  cifrar(args.texto, args.indice , args.operacion))
elif args.operacion == 'descifrar':
        print("\nEl resultado despues de", args.operacion , "es:" ,  cifrar(args.texto, args.indice , args.operacion))
if args.operacion == None and args.indice == None  and args.texto == None:
        print("Entrando al modo interactivo")
        interactivo()
        repetir = input("\nVolver al inicio?: ")
        if repetir.lower() in ["y","yes"]:
            interactivo()



        
        
        


