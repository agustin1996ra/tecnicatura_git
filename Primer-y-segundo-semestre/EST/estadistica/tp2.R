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
frecuencias <- c(6, 10, 16, 23, 33, 40, 46, 50)


crear_muestra <- function(valores,frecuencias){
  muestra <- c()
  for (n in c(1:length(valores))){
    for (x in c(1:frecuencias[n])) {
      muestra <- c(muestra , valores[n])
    }
  }
  return(muestra)
}  
  
mi_muestra <- crear_muestra(valores = nombres,frecuencias = frecuencias)


valores6 <- c(0, 1, 2, 3, 4, 5, 6, 7)
f_acu6 <- c(6, 10, 16, 23, 33, 40, 46, 50)
f_abs6 <- c()
for (n in c(1:length(f_acu6))) {
  f_abs6 <- c(f_abs6, f_acu6[n] - f_acu6[n - 1])
}
f_abs6


# Esta es un función para crear las muestras a partir de los valores y sus frecuencias.
crear_muestra <- function(valores,frecuencias){
  muestra <- c()
  for (n in c(1:length(valores))){
    for (x in c(1:frecuencias[n])) {
      muestra <- c(muestra , valores[n])
    }
  }
  return(muestra)
}
# Esta función sirve para obtener la frecuencia absuluta de la frecuencia acumulada
acu_a_abs <- function(f_acu){
  f_abs <- c()
  for (n in c(1:length(f_acu))) {
    if (n == 1){
      f_abs <- c(f_abs, f_acu[n])
    }else {
      f_abs <- c(f_abs, f_acu[n] - f_acu[n - 1])
    }
  }
  return(f_abs)
}

# Función de la moda, con una ditribucion muestral
moda_fun <- function(x) {
  return(as.numeric(names(which.max(table(x)))))
}
# Función del calculo de la covarianza
cv <- function(x, y) {return(as.numeric(x / y * 100))}
install.packages("ggplot2")
library(ggplot2)

  

# valores de la variable
nombres6 <- c(0, 1, 2, 3, 4, 5, 6, 7)
# frecuencias acumulada
fa6 <- c(6, 10, 16, 23, 33, 40, 46, 50)
# frecuencias absolutas
f6 <- acu_a_abs(fa6)
# Frecuencias relativas
fr6 <- f6 / margin.table(f6)
# Frecuencias relativas absolutas
fra6 <- cumsum(fr6)
t6 <- cbind(nombres6, f6, fa6, fr6, fra6)
rownames(t6) <- nombres6
t6

m6 <- crear_muestra(nombres6, f6)
"El valor de la media es:"
media6 <- mean(m6)
media6
"El valor de la moda es:"
moda6 <- moda_fun(m6)
moda6
"El valor de la mediana es:"
mediana6 <- median(6)
mediana6
df6 <- data.frame(hola = m6)

library(ggplot2)

ggplot(df6, aes(x = hola)) + 
  geom_bar() 
#  stat_count(aes(y=..count..,label=..count..),geom="text",vjust=-1)

datos <- data.frame(Sexo=c(rep(1,435), rep(2, 335)),  stringsAsFactors = FALSE)
ggplot(datos,aes(x=Sexo)) +
  geom_bar(fill="darkorchid4",color="black") +
  labs(title="SEXO - INGRESANTES 2015",x="Sexo",y="Frecuencia") +
  stat_count(aes(y=..count..,label=..count..),geom="text",vjust=-1) +
  coord_cartesian(ylim=c(-1,500))
datos




