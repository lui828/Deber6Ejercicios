def procesar_cadena(cadena, letra_a_reemplazar, letra_reemplazo):
    
    cadena_minuscula = cadena.lower()
    
    
    cadena_reemplazada = cadena_minuscula.replace(letra_a_reemplazar, letra_reemplazo)
    
    
    lista_palabras = cadena_reemplazada.split()
    
    
    print(f"Cadena modificada: {cadena_reemplazada}")
    print(f"Lista de palabras: {lista_palabras}")


texto = "Como ha estado tu día."
letra_original = 'e'
letra_nueva = 'x'

procesar_cadena(texto, letra_original, letra_nueva)