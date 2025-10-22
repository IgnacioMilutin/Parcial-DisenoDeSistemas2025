"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================




from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, fecha, temperatura, humedad, cultivo):
        return self._cantidad 

# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================


from python_forestacion.constantes import ABSORCION_SEASONAL_INVIERNO, ABSORCION_SEASONAL_VERANO, MES_FIN_VERANO, MES_INICIO_VERANO
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    def calcular_absorcion(self, fecha, temperatura, humedad, cultivo):
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO 
        else:
            return ABSORCION_SEASONAL_INVIERNO

