"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/strategy
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ================================================================================

"""
PATRON: STRATEGY
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """
    Interfaz para estrategias de absorcion de agua.
    """

    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula cantidad de agua a absorber.

        Args:
            fecha: Fecha de calculo (para determinar estacion)
            temperatura: Temperatura ambiental en Celsius
            humedad: Humedad relativa en porcentaje
            cultivo: Cultivo que absorbe agua

        Returns:
            int: Litros de agua a absorber
        """
        pass

