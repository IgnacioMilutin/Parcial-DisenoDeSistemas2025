from python_forestacion.constantes import ABSORCION_ZANAHORIA
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """
    Servicio para Zanahorias.
    """

    def __init__(self):
        """Inicializa con estrategia constante."""
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_ZANAHORIA))

    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        """Muestra datos de la zanahoria."""
        self._mostrar_datos_base(cultivo)
        tipo = "Baby carrot" if cultivo.is_baby_carrot() else "Regular"
        print(f"Tipo: {tipo}")
        print(f"Campo abierto: {'Si' if not cultivo.get_invernadero() else 'No'}")