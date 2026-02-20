# -*- coding: utf-8 -*-
"""
Script para captura de señales usando la DAQ.
Este script permite configurar la frecuencia de muestreo y duración de la señal;
realiza la captura internamente y posteriormente grafica la señal completa. 
Es una captura eficiente y exacta en el tiempo. Es útil si quiero grabar la señal
para procesarla posteriormente usando otro script, lenguaje, entorno, etc.

Se requiere instalar: 
Librería de uso de la DAQ
!python -m pip install nidaqmx     

Driver NI DAQ mx
!python -m nidaqmx installdriver   

Created on Thu Aug 21 08:36:05 2025
@author: Carolina Corredor
"""

# Librerías: 
import nidaqmx  # Librería daq. Requiere haber instalado el driver nidaqmx
from nidaqmx.constants import AcquisitionType # Para definir que adquiera datos de manera consecutiva
import matplotlib.pyplot as plt # Librería para graficar
import numpy as np  # Librería de funciones matemáticas


#%% Adquisición de la señal por tiempo definido

fs = 100          # Frecuencia de muestreo (Hz)
duracion = 10     # Duración en segundos
dispositivo = "Dev1/ai2"  # Nombre del dispositivo/canal

total_muestras = int(fs * duracion)

# Ruta donde se guardará el archivo txt
ruta_guardado = r"C:/Users/Usuario/Downloads/Procesamiento de señales/LAB 1/"
nombre_archivo = "senal_adquirida.txt"



# Adquisición de la señal

with nidaqmx.Task() as task:
    # Configuración del canal
    task.ai_channels.add_ai_voltage_chan(dispositivo)
    # Configuración del reloj de muestreo
    task.timing.cfg_samp_clk_timing(
        fs,
        sample_mode=AcquisitionType.FINITE,# Adquisición finita
        samps_per_chan=total_muestras # Total de muestras que quiero
    )
    # Lectura de todas las muestras de una vez
    senal = task.read(number_of_samples_per_channel=total_muestras)


# Procesamiento

senal = np.array(senal)
t = np.arange(len(senal)) / fs # Crea el vector de tiempo 


# Guardar archivo

datos = np.column_stack((t, senal)) #une arreglos por columnas, crea una matriz de 2 columnas: tiempo  y señal

np.savetxt(
    ruta_guardado + nombre_archivo,  # Ruta donde se guardará el archivo
    datos,          # Matriz de datos que se va a guardar
    delimiter="\t",
    header="Tiempo(s)\tVoltaje(V)",
    comments=''
)

print(f"Archivo guardado en:\n{ruta_guardado}") #muestra texto en consola


# Gráfica

plt.plot(t,senal) # grafica datos
plt.axis([0,duracion,-1,1]) #define los límites de los ejes
plt.grid()#activa la cuadrícula en la gráfica
#coloca el nombre del eje X
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
#coloca un título a la gráfica,cuenta el número total de muestras
plt.title(f"fs = {fs} Hz | Duración = {duracion} s | Muestras = {len(senal)}")
plt.show() #muestra la gráfica en pantalla