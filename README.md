# Análisis Estadístico de Señales - Práctica de Laboratorio
## Descripción
Este proyecto contiene el código para descargar, procesar y análisar de manera estadística las señales fisiológicas, incluyendo el cálculo de parámetros de estadistica  descriptiva, la semejanza de señales reales y generadas, y evaluación de la relación señal-ruido (SNR) bajo distintos tipos de contaminación.
## Procesamiento de señales
Las señales fisiológicas fueron descargadas desde bases de datos públicas e importadas en Python para su análisis.

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
