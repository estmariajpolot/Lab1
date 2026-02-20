# Análisis Estadístico de Señales

## Asignatura

Procesamiento Digital de Señales

## Programa

Ingeniería Biomédica – Universidad Militar Nueva Granada

## Práctica de laboratorio

**Análisis estadístico de señales biomédicas**

## Integrantes

Danna Jimena Medina Ríos – Código 5600923
María José Polo Tovar – Código 5600894

---

## Descripción

Este proyecto presenta el código desarrollado para descargar, procesar y analizar estadísticamente señales fisiológicas. Incluye el cálculo de parámetros de estadística descriptiva, la comparación entre señales reales y generadas, y la evaluación de la relación señal-ruido (SNR) bajo distintos tipos de contaminación.

---

## Señal fisiológica

Se utilizó la base de datos *Norwegian Endurance Athlete ECG Database*, disponible en PhysioNet. Esta base reúne electrocardiogramas (ECG) de 12 derivaciones registrados en reposo a 28 atletas noruegos de resistencia de alto rendimiento.

Cada señal tiene una duración de 10 segundos y fue adquirida con una frecuencia de muestreo de 500 Hz. El propósito del estudio es analizar las adaptaciones cardíacas asociadas al entrenamiento intenso (remodelación cardíaca del atleta) y facilitar la diferenciación entre cambios fisiológicos normales y posibles alteraciones patológicas.

Además, cada ECG fue interpretado tanto por un sistema automático como por un cardiólogo especializado, lo que permite comparar el análisis computacional con la evaluación clínica experta.

---

## Metodología

El desarrollo del laboratorio se dividió en tres partes principales. En cada etapa se emplearon herramientas de programación en Python para el procesamiento y análisis de las señales biomédicas.

En primer lugar, se realizó la importación y visualización de una señal fisiológica descargada desde una base de datos pública. Posteriormente, se calcularon parámetros estadísticos descriptivos tanto de forma manual como utilizando funciones predefinidas del lenguaje. Finalmente, se adquirió una señal real y se evaluó el efecto de diferentes tipos de ruido mediante el cálculo de la relación señal-ruido (SNR).

### Parte A

En esta parte del trabajo se realiza el análisis de una señal electrocardiográfica (ECG) obtenida desde una base de datos pública en formato WFDB. El objetivo principal es caracterizar estadísticamente la señal y comprender su comportamiento temporal y probabilístico antes de compararla con una señal adquirida experimentalmente.
<p align="center">
  <img src="DIA2.png" width="700">
</p>

<p align="center">
  <em>Diagrama de flujo completo código principal</em>
</p>

## Explicación del código

En esta sección se explica el funcionamiento del código utilizado para el análisis estadístico de una señal fisiológica descargada desde PhysioNet.

### Importación de librerías

Primero se importan las librerías necesarias para la lectura, el procesamiento y la visualización de la señal biomédica:

* `os`: permite gestionar rutas y archivos dentro del sistema operativo.
* `wfdb`: se utiliza para leer señales fisiológicas en formato WFDB, común en bases de datos como PhysioNet.
* `numpy`: facilita el manejo de arreglos y operaciones numéricas.
* `matplotlib.pyplot`: se emplea para generar gráficos.
* `scipy.stats`: permite calcular parámetros estadísticos como asimetría y curtosis.

Estas herramientas son fundamentales para el análisis de señales biomédicas en Python.

---

### Carga de la señal fisiológica

Luego se define la ruta donde se encuentran los archivos del ECG descargado y se lee el registro mediante la función `rdsamp` de `wfdb`. Esta función permite obtener tanto los valores de la señal como la información asociada al registro, por ejemplo, la frecuencia de muestreo.

Como el registro tiene 12 derivaciones, se selecciona una derivación específica: la Derivación II. Esta es una de las más utilizadas en el análisis electrocardiográfico, ya que permite visualizar con claridad el complejo QRS.

![Imagen 2](img1.png)
---

### Extracción de parámetros temporales

Una vez cargada la señal, se obtiene la frecuencia de muestreo a partir de los metadatos del registro. Con este dato se calcula cuántas muestras corresponden a un intervalo de 10 segundos, lo que permite trabajar con un segmento temporal definido para el análisis.

También se construye un vector de tiempo que relaciona cada muestra con su instante correspondiente.

---

### Visualización de la señal

El código grafica un segmento de 10 segundos del ECG seleccionado. Esta visualización permite hacer una inspección inicial de la señal, identificando aspectos como la periodicidad del ritmo cardíaco, la amplitud de los complejos QRS y la posible presencia de ruido o artefactos.

Antes de realizar cualquier análisis cuantitativo, esta revisión visual es importante para comprobar que la señal tiene una calidad adecuada.

---

### Recorte de la señal

Para el análisis estadístico, se recorta la señal al segmento previamente definido. De esta manera, los cálculos se realizan sobre un número controlado de muestras y en un intervalo temporal uniforme.

---

### Cálculo manual de los estadísticos descriptivos

En esta etapa se implementan manualmente las fórmulas matemáticas de los principales estadísticos descriptivos:

* **Media**: promedio de los valores de la señal, representa el valor central.
* **Desviación estándar**: indica qué tan dispersos están los valores respecto a la media.
* **Coeficiente de variación**: relaciona la desviación estándar con la media y permite evaluar la variabilidad relativa.
* **Asimetría (skewness)**: muestra si la distribución de los valores está sesgada hacia la derecha o hacia la izquierda.
* **Curtosis**: describe el grado de concentración o dispersión de los valores alrededor de la media.

Realizar estos cálculos de forma manual ayuda a comprender mejor el significado matemático de cada parámetro y su relación con la forma de la señal.

---

### Cálculo mediante funciones predefinidas

Posteriormente, los mismos estadísticos se calculan usando funciones de `numpy` y `scipy.stats`. Este enfoque simplifica el código y mejora la eficiencia, además de servir para verificar que los resultados obtenidos manualmente son correctos.

Al comparar ambos métodos, se observa coherencia en los resultados, lo que confirma la adecuada implementación de las fórmulas.

---

### Análisis con histogramas

Finalmente, se genera un histograma de la señal ECG analizada. Este permite observar cómo se distribuyen las amplitudes de la señal y analizar su comportamiento estadístico.

Se añade una línea vertical que representa la media, lo que facilita interpretar visualmente la distribución de los datos con respecto a su valor central.

![Imagen 3](img2.png)
---

### Interpretación general de la Parte A

El análisis estadístico realizado permite caracterizar la señal electrocardiográfica desde un punto de vista cuantitativo, describiendo su variabilidad, distribución y forma. Estos resultados sirven como referencia para compararlos posteriormente con la señal adquirida de manera experimental.
