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