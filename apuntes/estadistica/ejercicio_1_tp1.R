color <- c("negro", "azul", "amarillo", "rojo", "azul", "azul", "rojo", "negro", "amarillo", "rojo", "rojo", "amarillo", "amarillo", "azul", "rojo", "negro", "azul", "rojo", "negro", "amarillo")
fabs <- table(color)
fabs
FabsAC <- cumsum(fabs)
frel <- (fabs)/margin.table(fabs)
frel
FabsAC/margin.table(fabs)
media <- mean(fabs)
media
moda <- max(fabs)
moda
mediana <- color[10]
mediana
barplot(fabs, ylab="Frecuencias absolutas", main="Colores")

autos <- c(0, 1, 2, 1, 2, 0, 3, 2, 4, 0, 4, 2, 1, 0, 3, 0, 0, 3, 4, 2, 0, 1, 1, 3, 0, 1, 2, 1, 2, 3)
mes <- data.frame(autos)

fabs <- table(mes)
fabs
FabsAC <- cumsum(fabs)
frel <- (fabs)/margin.table(fabs)
frel
FabsAC/margin.table(fabs)
media <- mean(fabs)
media
moda <- max(fabs)
moda
barplot(fabs, ylab="Frecuencias absolutas", main="Autos vendidos")



notas <- c(0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 10, 10)
fabs <- table(notas)
fabs
FabsAC <- cumsum(fabs)
frel <- (fabs)/margin.table(fabs)
frel
FabsAC/margin.table(fabs)
media <- mean(fabs)
media
moda <- max(fabs)
moda
barplot(fabs, ylab="Frecuencias absolutas", main="Notas")
