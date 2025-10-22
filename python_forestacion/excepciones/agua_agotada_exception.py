

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import MensajesException


class AguaAgotadaException(ForestacionException):
    """
    Excepcion lanzada cuando no hay suficiente agua para riego.
    """

    def __init__(
        self,
        agua_requerida: float,
        agua_disponible: float,
        operacion: str = "riego"
    ):
        """
        Inicializa excepcion de agua agotada.

        Args:
            agua_requerida: Litros necesarios para operacion
            agua_disponible: Litros disponibles
            operacion: Tipo de operacion (riego, cosecha, etc)
        """
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible
        self._operacion = operacion

        user_msg = MensajesException.agua_agotada_user(
            operacion, agua_requerida, agua_disponible
        )
        tech_msg = MensajesException.agua_agotada_tech(
            operacion, agua_requerida, agua_disponible
        )

        super().__init__(user_msg, tech_msg)

    def get_agua_requerida(self) -> float:
        """Retorna agua requerida."""
        return self._agua_requerida

    def get_agua_disponible(self) -> float:
        """Retorna agua disponible."""
        return self._agua_disponible

