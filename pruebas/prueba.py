def incrementar(x):
    x += 1  # Esto solo modifica la copia de 'x' dentro de esta función

numero = 0
incrementar(numero)  # Pasamos el valor de 'numero' a la función
print(numero)  # Aquí 'numero' sigue siendo 0, porque no se modificó fuera de la función
