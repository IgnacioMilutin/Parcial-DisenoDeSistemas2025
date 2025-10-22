from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """
    Servicio para cultivos tipo Arbol (Pino, Olivo). 
    """

    def crecer(self, cultivo: 'Arbol', cantidad: float) -> None:
        """
        Hace crecer el arbol.

        Args:
            cultivo: Arbol a hacer crecer
            cantidad: Metros a crecer
        """
        cultivo.crecer(cantidad)

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Arbol') -> None:
        pass