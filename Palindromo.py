def es_palindromo(palabra):
     palabra = palabra.lower()
     return palabra == palabra[::-1]
  
palabra = input("Escriba la palabra: ")
 
if es_palindromo(palabra):
    print("Es un palíndromo")
    
else:
    print("No es un palíndromo")
    
