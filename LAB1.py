#Librerias
import os # manejo de rutas
import wfdb #lectura de señales fisiológicas (ECG)
import matplotlib.pyplot as plt # graficas
import numpy as np # cálculo numérico
from scipy.stats import skew, kurtosis # asimetría y curtosis
# Cargar señal
directory = r"C:/Users/Usuario/Downloads/Procesamiento de señales/LAB 1/"
record = wfdb.rdsamp(os.path.join(directory, "ath_001"))
# Extrae la señal
signal, meta = record
signal = signal[:, 1]   # Derivación II
fs = meta['fs'] #frecuencia de muestreo
print(f"Frecuencia de muestreo: {fs} Hz")


# Graficar 10 segundos

tiempo_total = 10  # segundos
muestras = int(fs * tiempo_total)

t = np.arange(muestras) / fs

plt.figure(figsize=(12,4))
plt.plot(t, signal[:muestras])
plt.title('Señal ECG - Derivación II (10 s)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()

# Recorte de señal

senal_cortada = signal[:muestras]
N = len(senal_cortada)
print("\n================ PARTE A ================\n")
# ESTADÍSTICOS MANUALES 

#  Media 
suma = 0
for i in range(N):
    suma += senal_cortada[i]

media_manual = suma / N

#  Desviación estándar 
suma_var = 0
for i in range(N):
    suma_var += (senal_cortada[i] - media_manual)**2

desv_manual = (suma_var / N)**0.5

# Coeficiente de variación
cv_manual = desv_manual / media_manual if media_manual != 0 else np.nan

#  Asimetría 
suma_skew = 0
for i in range(N):
    suma_skew += ((senal_cortada[i] - media_manual)/desv_manual)**3

skew_manual = suma_skew / N if desv_manual != 0 else np.nan

# Curtosis 
suma_kurt = 0
for i in range(N):
    suma_kurt += ((senal_cortada[i] - media_manual)/desv_manual)**4

kurt_manual = (suma_kurt / N) - 3 if desv_manual != 0 else np.nan


print("\n=== Estadísticos MANUALES ===")
print(f"Media: {media_manual:.4f}")
print(f"Desviación estándar: {desv_manual:.4f}")
print(f"Coeficiente de variación: {cv_manual:.4f}")
print(f"Asimetría (skewness): {skew_manual:.4f}")
print(f"Curtosis: {kurt_manual:.4f}")


# ESTADÍSTICOS CON FUNCIONES


media_lib = np.mean(senal_cortada)
desv_lib = np.std(senal_cortada)
cv_lib = desv_lib / media_lib if media_lib != 0 else np.nan
skew_lib = skew(senal_cortada)
kurt_lib = kurtosis(senal_cortada)  # ya devuelve exceso

print("\n=== Estadísticos con funciones de Python ===")
print(f"Media: {media_lib:.4f}")
print(f"Desviación estándar: {desv_lib:.4f}")
print(f"Coeficiente de variación: {cv_lib:.4f}")
print(f"Asimetría (skewness): {skew_lib:.4f}")
print(f"Curtosis: {kurt_lib:.4f}")


#HISTOGRAMA

plt.figure(figsize=(8,4))
plt.hist(senal_cortada, bins=50, color='skyblue', edgecolor='black')
plt.axvline(media_lib, color='red', linestyle='dashed',
            linewidth=1.5, label=f'Media={media_lib:.2f}')

plt.title('Histograma ECG - Derivación II (10 s)')
plt.xlabel('Amplitud')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True)
plt.show()

#%% Parte B
print("\n================ PARTE B ================\n")

# Cargar archivo adquirido (.txt)

ruta_B = r"C:/Users/Usuario/Downloads/Procesamiento de señales/LAB 1/senal_adquirida.txt"

datos_B = np.loadtxt(ruta_B, skiprows=1)

# Separa tiempo y señal
tiempo_B = datos_B[:,0]
senal_B = datos_B[:,1]

fs_B = 100  # frecuencia usada en adquisición

print(f"Frecuencia de muestreo Parte B: {fs_B} Hz")
print(f"Número de muestras Parte B: {len(senal_B)}")


# Graficar señal Parte B
plt.figure(figsize=(12,4))
plt.plot(tiempo_B, senal_B)
plt.title("Señal Adquirida - Parte B")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid(True)
plt.show()


#  Estadísticos con funciones Parte B
media_lib_B = np.mean(senal_B)
desv_lib_B = np.std(senal_B)
cv_lib_B = desv_lib_B / media_lib_B if media_lib_B != 0 else np.nan
skew_lib_B = skew(senal_B)
kurt_lib_B = kurtosis(senal_B)

print("\n=== Estadísticos con funciones Parte B ===")
print(f"Media: {media_lib_B:.4f}")
print(f"Desviación estándar: {desv_lib_B:.4f}")
print(f"Coeficiente de variación: {cv_lib_B:.4f}")
print(f"Asimetría: {skew_lib_B:.4f}")
print(f"Curtosis: {kurt_lib_B:.4f}")


# Histograma
plt.figure(figsize=(8,4))
plt.hist(senal_B, bins=50, color='lightgreen', edgecolor='black')
plt.axvline(media_lib_B, color='red', linestyle='dashed',
            linewidth=1.5, label=f'Media={media_lib_B:.2f}')
plt.title("Histograma Señal Parte B")
plt.xlabel("Voltaje")
plt.ylabel("Frecuencia")
plt.legend()
plt.grid(True)
plt.show()

# Comparación Parte A vs Parte B 

# Calcular diferencias
diff_media = abs(media_lib - media_lib_B)
diff_desv  = abs(desv_lib - desv_lib_B)
diff_skew  = abs(skew_lib - skew_lib_B)
diff_kurt  = abs(kurt_lib - kurt_lib_B)

# Imprimir tabla formateada
print("\n=========== COMPARACIÓN FINAL ===========" )
print("{:<15} {:>12} {:>12} {:>12}".format("Parámetro", "Parte A", "Parte B", "Diferencia"))
print("-"*55)

print("{:<15} {:>12.4f} {:>12.4f} {:>12.4f}".format("Media", media_lib, media_lib_B, diff_media))
print("{:<15} {:>12.4f} {:>12.4f} {:>12.4f}".format("Desv Std", desv_lib, desv_lib_B, diff_desv))
print("{:<15} {:>12.4f} {:>12.4f} {:>12.4f}".format("Skewness", skew_lib, skew_lib_B, diff_skew))
print("{:<15} {:>12.4f} {:>12.4f} {:>12.4f}".format("Kurtosis", kurt_lib, kurt_lib_B, diff_kurt))

#%% Parte C
print("\n================ PARTE C ================\n")

# Usaremos la señal de la Parte B
senal_original = senal_B
N = len(senal_original)

# SNR = 10 * log10( Potencia señal / Potencia ruido )

def calcular_snr(senal, ruido):
    potencia_senal = np.mean(senal**2)
    potencia_ruido = np.mean(ruido**2)
    snr = 10 * np.log10(potencia_senal / potencia_ruido)
    return snr


#  Ruido Gaussiano

ruido_gauss = np.random.normal(0, 0.05*np.std(senal_original), N)
senal_gauss = senal_original + ruido_gauss

snr_gauss = calcular_snr(senal_original, ruido_gauss)

print(f"SNR con Ruido Gaussiano: {snr_gauss:.4f} dB")

plt.figure(figsize=(12,4))
plt.plot(tiempo_B, senal_gauss)
plt.title("Señal con Ruido Gaussiano")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid(True)
plt.show()


#  Ruido Impulso

ruido_impulso = np.zeros(N)
prob = 0.01  # probabilidad de impulso

for i in range(N):
    if np.random.rand() < prob:
        ruido_impulso[i] = np.random.choice([-1,1]) * 3*np.std(senal_original)

senal_impulso = senal_original + ruido_impulso

snr_impulso = calcular_snr(senal_original, ruido_impulso)

print(f"SNR con Ruido Impulso: {snr_impulso:.4f} dB")

plt.figure(figsize=(12,4))
plt.plot(tiempo_B, senal_impulso)
plt.title("Señal con Ruido Impulso")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid(True)
plt.show()


#  Ruido tipo Artefacto 

# Artefacto simulado como señal senoidal de baja frecuencia
artefacto = 0.3*np.std(senal_original) * np.sin(2*np.pi*1*tiempo_B)

senal_artefacto = senal_original + artefacto

snr_artefacto = calcular_snr(senal_original, artefacto)

print(f"SNR con Ruido tipo Artefacto: {snr_artefacto:.4f} dB")

plt.figure(figsize=(12,4))
plt.plot(tiempo_B, senal_artefacto)
plt.title("Señal con Ruido tipo Artefacto")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid(True)
plt.show()


# Comparación final de SNR

print("\n=========== COMPARACIÓN SNR ===========" )
print(f"SNR Ruido Gaussiano: {snr_gauss:.4f} dB")
print(f"SNR Ruido Impulso: {snr_impulso:.4f} dB")
print(f"SNR Ruido Artefacto: {snr_artefacto:.4f} dB")

