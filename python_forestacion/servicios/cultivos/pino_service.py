from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """
    Servicio para Pinos.
    """

    def __init__(self):
        """Inicializa con estrategia seasonal."""
        super().__init__(AbsorcionSeasonalStrategy())

    def mostrar_datos(self, cultivo: 'Pino') -> None:
        """Muestra datos del pino."""
        self._mostrar_datos_base(cultivo)
        print(f"Altura: {cultivo.get_altura()} m")
        print(f"Variedad: {cultivo.get_variedad()}")