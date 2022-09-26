library(readxl)
library(ggplot2)
base_de_datos <- read_excel("../base_de_datos_tp3.xlsx")
base_de_datos
head(diamonds)

# Ejercicio a.1: Grafico barplot variable modelo de auto
ggplot(base_de_datos, aes(x = modelo)) +
  geom_bar() +
  ylab("Frecuencias absolutas") +
  ggtitle("Grafico de barras")


# Ejercicio a.2: Barplot con colores
ggplot(base_de_datos, aes(x = modelo)) +
  geom_bar(color = "blue", fill = "red") +
  ylab("Frecuencias absolutas") +
  ggtitle("Grafico de barras")


# Ejercicio a.3: Barplot con las cordenadas invertidas
ggplot(base_de_datos, aes(x = modelo)) +
  geom_bar(color = "blue", fill = "red") +
  ylab("Frecuencias absolutas") +
  ggtitle("Grafico de barras") +
  coord_flip()


# Ejercicio a.4: por distintos colores 
ggplot(base_de_datos, aes(x = modelo, fill = as.factor(modelo))) +
  geom_bar() +
  ylab("Frecuencias absolutas") +
  ggtitle("Grafico de barras") +
  labs(fill = "modelo")

# Ejercicio b.1: Histograma con rango 0 a 2
ggplot(base_de_datos) +
  geom_histogram(binwidth = 2, aes(x = modelo), fill = "steelblue") +
  xlab("Modelo") +
  ylab("Frecuencias") +
  ggtitle("Histograma con rango 0 a 2") +
  theme_minimal()

# Ejercicio b.2: Histograma usando cortes
ggplot(base_de_datos) +
  geom_histogram(binwidth = 1, aes(x = modelo, fill = marca)) +
  xlab("Modelo") +
  ylab("Frecuencias") +
  ggtitle("Histograma con rango 0 a 2") +
  theme_minimal()

# Ejercicio b.3: Histograma usando la varible cilindrada
ggplot(base_de_datos) +
  geom_histogram(binwidth = 0.1, aes(x = cilindrada)) +
  xlab("Cilindrada") +
  ylab("Frecuencia") +
  ggtitle("Histograma usando la variable cilindrada") +
  theme_minimal()

# Ejercicio c: Grafico de dispersion de puntos
ggplot(base_de_datos, aes(marca, modelo)) +
  geom_point() +
  xlab("Marca") +
  ylab("Modelo") +
  ggtitle("Grafico de dispersion de puntos") +
  theme_minimal()  
  



