
library(readxl)
library(ggplot2)
base_de_datos <- read_excel("../base_de_datos_tp3.xlsx")
base_de_datos

g1 <- ggplot(base_de_datos, aes(marca, modelo))

g1 + geom_point()

g1 + geom_col()

g1 + geom_line()

g1 + geom_hex()

install.packages(tidyverse)

modelo <- pull(base_de_datos, modelo)
media <- mean(modelo)
media
mediana <- median(modelo)
mediana
desviacion_estandar <- var(modelo) ^ 0.5
desviacion_estandar

