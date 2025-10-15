# 🔐 Cifrado César en Python

Este proyecto implementa un sencillo **cifrado César**, un método clásico de cifrado por sustitución en el que cada letra del texto se desplaza un número fijo de posiciones en el alfabeto.

---

## 📜 Descripción

El programa permite **cifrar** y **descifrar** textos en español utilizando la técnica del cifrado César.  
A través de argumentos de línea de comandos, puedes especificar el texto a procesar, el desplazamiento y la operación deseada.

---

## ⚙️ Requisitos

- Python 3.6 o superior

No requiere librerías externas, solo módulos estándar de Python (`argparse` y `string`).

---

## 🚀 Uso

Ejecuta el script desde la terminal:

```bash
python main.py -i 19 -o cifrar -texto "Ejemplo de texto a cifrar"   


python main.py -i 19 -o descifrar -texto "Ejemplo de texto a descifrar"   

