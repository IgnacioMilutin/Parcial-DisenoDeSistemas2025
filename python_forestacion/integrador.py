"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: constantes.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/constantes.py
# ================================================================================

# python_forestacion/constantes.py

# ============================================================================
# AGUA Y RIEGO
# ============================================================================

AGUA_MINIMA = 10  # Agua minima para un riego (litros)
AGUA_INICIAL_PLANTACION = 500  # Agua inicial de cada plantacion (litros)

# Absorcion estacional de arboles
ABSORCION_SEASONAL_VERANO = 5  # Litros en verano
ABSORCION_SEASONAL_INVIERNO = 2  # Litros en invierno
MES_INICIO_VERANO = 3  # Marzo
MES_FIN_VERANO = 8  # Agosto

# Absorcion constante de hortalizas
ABSORCION_LECHUGA = 1  # Litros por riego
ABSORCION_ZANAHORIA = 2  # Litros por riego

# ============================================================================
# CULTIVOS - PINO
# ============================================================================

SUPERFICIE_PINO = 2.0  # Metros cuadrados por arbol
AGUA_INICIAL_PINO = 2  # Litros iniciales
CRECIMIENTO_PINO = 0.10  # Metros por riego

# ============================================================================
# CULTIVOS - OLIVO
# ============================================================================

SUPERFICIE_OLIVO = 3.0  # Metros cuadrados por arbol
AGUA_INICIAL_OLIVO = 5  # Litros iniciales
CRECIMIENTO_OLIVO = 0.01  # Metros por riego
ALTURA_INICIAL_OLIVO = 0.5

# ============================================================================
# CULTIVOS - LECHUGA
# ============================================================================

SUPERFICIE_LECHUGA = 0.10  # Metros cuadrados por planta
AGUA_INICIAL_LECHUGA = 1  # Litros iniciales
LECHUGA_EN_INVERNADERO = True  # Siempre en invernadero

# ============================================================================
# CULTIVOS - ZANAHORIA
# ============================================================================

SUPERFICIE_ZANAHORIA = 0.15  # Metros cuadrados por planta
AGUA_INICIAL_ZANAHORIA = 0  # Sin agua inicial
ZANAHORIA_EN_INVERNADERO = False  # Cultivo a campo abierto

# ============================================================================
# ARBOLES - GENERAL
# ============================================================================

ALTURA_INICIAL_ARBOL = 1.0  # Metros (altura inicial de arboles)

# ============================================================================
# SENSORES Y RIEGO AUTOMATIZADO
# ============================================================================

# Sensor de temperatura
INTERVALO_SENSOR_TEMPERATURA = 2.0  # Segundos entre lecturas
SENSOR_TEMP_MIN = -25  # Grados Celsius
SENSOR_TEMP_MAX = 50  # Grados Celsius

# Sensor de humedad
INTERVALO_SENSOR_HUMEDAD = 3.0  # Segundos entre lecturas
SENSOR_HUMEDAD_MIN = 0  # Porcentaje
SENSOR_HUMEDAD_MAX = 100  # Porcentaje

# Control de riego
TEMP_MIN_RIEGO = 8  # Temperatura minima para regar (C)
TEMP_MAX_RIEGO = 15  # Temperatura maxima para regar (C)
HUMEDAD_MAX_RIEGO = 50  # Humedad maxima para regar (%)
INTERVALO_CONTROL_RIEGO = 2.5  # Segundos entre evaluaciones

# ============================================================================
# THREADING
# ============================================================================

THREAD_JOIN_TIMEOUT = 2.0  # Segundos de timeout para join

# ============================================================================
# PERSISTENCIA
# ============================================================================

DIRECTORIO_DATA = "data"  # Directorio de datos persistidos
EXTENSION_DATA = ".dat"  # Extension de archivos de datos

# ============================================================================
# MENSAJES DE SISTEMA
# ============================================================================

SEPARADOR_LARGO = "=" * 70
SEPARADOR_CORTO = "-" * 70
SEPARADOR_TITULO = "_" * 28

