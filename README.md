# Análisis Estadístico de Señales - Práctica de Laboratorio
## Descripción
Este proyecto contiene el código para descargar, procesar y análisar de manera estadística las señales fisiológicas, incluyendo el cálculo de parámetros de estadistica  descriptiva, la semejanza de señales reales y generadas, y evaluación de la relación señal-ruido (SNR) bajo distintos tipos de contaminación.
## Señal fisiologica
La base de datos Norwegian Endurance Athlete ECG Database, disponible en PhysioNet, reúne electrocardiogramas (ECG) de 12 derivaciones registrados en reposo a 28 atletas noruegos de resistencia de alto nivel. Cada señal tiene una duración de 10 segundos y fue adquirida con una frecuencia de muestreo de 500 Hz. El propósito del estudio es analizar las adaptaciones cardíacas propias del entrenamiento intenso (remodelación cardíaca del atleta) y facilitar la diferenciación entre cambios fisiológicos normales y posibles alteraciones patológicas. Además, cada ECG fue interpretado tanto por un sistema automático como por un cardiólogo especializado, lo que permite comparar el análisis computacional con la evaluación clínica experta.
## Procesamiento de señales
Las señales fisiológicas fueron descargadas desde PhysioNet e importadas en Python para su análisis.

Se calcularon los siguientes parámetros estadísticos:
- Media
- Desviación estándar
- Coeficiente de variación
- Histogramas
- Asimetría (skewness)
- Curtosis
  
Los cálculos se realizaron de dos maneras:
1. Implementando las fórmulas desde cero.
   
2. Utilizando funciones predefinidas de Python (NumPy y SciPy).

Posteriormente, se generó y adquirió una señal fisiológica experimental para comparar sus características estadísticas con la señal descargada.

Finalmente, se evaluó la relación señal-ruido (SNR) contaminando la señal con:
- Ruido gaussiano
- Ruido impulso
- Ruido tipo artefacto

## Requisitos
- Python 3.x
- NumPy
- Matplotlib
- SciPy
- WFDB

## Uso
1. Descargar una señal fisiológica.
2. Importarla en Python.
3. Ejecutar los scripts de análisis estadístico.
4. Comparar resultados y evaluar el SNR.
