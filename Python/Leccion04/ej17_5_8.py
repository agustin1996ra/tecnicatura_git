""" Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
Hacer un programa donde el usuario ingrese una frase, se le
devolverá la misma frase pero sin espacios en blanco, y
además un contador de cuántos caracteres tiene la frase
(sin contar los espacios en blanco)
Ejemplo:    frase = 'vivir por siempre en paz'
            frase_final = 'vivirporsiemprenepaz'
            n° de caracteres = 20
"""

frase = input('Ingrese una frase: ')
frase_final = frase.replace(' ', '')
print(f'frase = {frase}\nfrase final = {frase_final}\nn° de caracteres = {len(frase_final)}')
