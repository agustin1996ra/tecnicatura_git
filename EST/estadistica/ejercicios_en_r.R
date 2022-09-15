# Los alumnos del último curso de bachillerato de un Instituto 
# eligen carrera según los datos de la tabla siguiente 
# Construir la distribución de frecuencias adecuada para la variable 
# carrera elegida por los alumnos y realizar los gráficos pertinentes 
# que la representen
medicina <- 250
derecho <- 176
ciencias <- 127
letras <- 314
inef <- 103
otras <- 30
carreras <- cbind(medicina, derecho, ciencias, letras, inef, otras)
barplot(carreras)
pie(carreras, labels = c("medicina", "derecho", "ciencias", "letras", "inef", "otras"))

# En una clínica se han registrado durante un mes las longitudes
# en metros que los niños andan el primer día que comienzan a 
# caminar, obteniéndose los siguientes resultados:

# Construir la distribución de frecuencias adecuada para la variable
# logitud y realizar los gráficos pertinentes que la representen
n_niños <- c(2, 10, 10, 5, 10, 3, 2, 2)
uno <- 2
dos <- 10
tres <- 10
cuatro <- 5
cinco <- 10
seis <- 3
siete <- 2
ocho <- 2

frecuencia <- cbind(uno, dos, tres, cuatro, cinco, seis, siete, ocho)
nombres <- c("uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho")

barplot(frecuencia, ylab = "Frecuencias Absolutas", main = "
        Metros caminados")
pie(frecuencia, labels = nombres, main = "Metros caminados")




# El número de automóviles que vendió cada uno de los 10 
# vendedores de una distribuidora en un mes especifico
# fueron: 
autos_vendidos <- c(2, 4, 7, 10, 12, 10, 14, 10, 15, 12)
fabs <- table(autos_vendidos)
fabs
barplot(fabs, xlab="Autos vendidos", ylab = "Frecuencia absoluta",main = "Vendedores segun sus ventas")
f_abs_acu <- cumsum(fabs)
f_abs_acu
barplot(f_abs_acu, xlab="Autos vendidos", ylab="Frecuencia acumulada", main="Vendedores segun sus ventas")
media <- mean(autos_vendidos)
# El promedio de autos vendido por los vendedores es
media
#defino la funcion moda que sobre una muestra, arma un tabla 
# y devuelve la etiqueta del valor mas representativo
moda_fun <- function(x) {return(as.numeric(names(which.max(table(x)))))}
moda <- moda_fun(autos_vendidos)
# El valor que mas veces mas se repitede autos vendidos por vendeor
moda
mediana <- median(autos_vendidos)
# EL valor central de la muesta es
mediana
# El valor tendencia central que dsescribe mejor el volumen de 
# ventas por vendedor es el promedio


# para calcular la varianza utilizamos la funcion var()
varianza <- var(autos_vendidos)
# el valor de varianza es
varianza

# 1.6
# La siguiente distribución de frecuencias corresponde al número
# de litros de cerveza consumidos por cada una de 50
# familias en una semana determinada.

# Este vector contiene los litros de cerveza de la escala
nombres <- c(0, 1, 2, 3, 4, 5, 6, 7)
faa <- c(6, 10, 16, 23, 33, 40, 46, 50)
fabs <-

