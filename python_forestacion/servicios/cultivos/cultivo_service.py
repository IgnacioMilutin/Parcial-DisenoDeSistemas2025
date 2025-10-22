"""
Servicio base para cultivos.

Operaciones sobre cultivos
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService(ABC):
    """
    Servicio base abstracto para cultivos.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inicializa servicio con estrategia inyectada.

        Args:
            estrategia_absorcion: Strategy para calcular absorcion(Seasonal o Constante)
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        """
        Absorbe agua en cultivo usando Strategy.

        Args:
            cultivo: Cultivo que absorbe agua

        Returns:
            int: Litros absorbidos
        """
        fecha_hoy = date.today()
        cantidad_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha=fecha_hoy,
            temperatura=0.0,  
            humedad=0.0,      
            cultivo=cultivo
        )

        agua_actual = cultivo.get_agua()
        cultivo.set_agua(agua_actual + cantidad_absorvida)

        return cantidad_absorvida

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos especificos del cultivo.

        Args:
            cultivo: Cultivo a mostrar
        """
        pass

    def _mostrar_datos_base(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos comunes a todos los cultivos.

        Args:
            cultivo: Cultivo a mostrar
        """
        print(f"Cultivo: {cultivo.get_tipo_cultivo()}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")
        if cultivo.get_id_cultivo() is not None:
            print(f"ID: {cultivo.get_id_cultivo()}")