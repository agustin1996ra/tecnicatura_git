# Ejercicio 4: Etapas de la vida
# Haremos un programa que cuando el usuario ingrese su edad le
# diga, o imprima la etapa de su vida en una breve oración:
# 0 a 10 = La infancia es increíble y bella
# 10 a 19 = Tienes muchos cambios, mucho que estudiar
# 20 a 29 = Amor y comienza el trabajo
#
mensaje = None
edad = int(input("Ingrese su edad: "))
if 0 <= edad <= 9:
    mensaje = "La infancia es increíble y bella"
elif 10 <= edad <= 19:
    mensaje = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad <= 29:
    mensaje = "mucho estudio, mucha crisis, poca plata"
elif 30 <= edad <= 39:
    mensaje = "mucho trabajo, mas crisis, (plata) XOR (hijos)"
elif 40 <= edad <= 49:
    mensaje = "crisis, moto y pelada"
elif 50 <= edad <= 59:
    mensaje = "Sali de ahi maravilla"
elif 60 <= edad <= 69:
    mensaje = "Si tenés suerte te jubilas, sino cosida"
elif 70 <= edad <= 79:
    mensaje = "Mas olor a cajon que a manzana"
elif 80 <= edad <= 89:
    mensaje = "Buena, resistente el alpataco"
elif 90 <= edad:
    mensaje = "Felicitaciones te pasaste el juego"

print(f'Tue edad es: {edad}, {mensaje}')
