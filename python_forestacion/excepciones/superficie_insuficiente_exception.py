

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import MensajesException

class SuperficieInsuficienteException(ForestacionException):
    """
    Excepcion lanzada cuando no hay suficiente superficie para plantar.
    
    Ocurre cuando:
    - Se intenta plantar cultivos que requieren mas espacio del disponible
    """

    def __init__(
        self,
        superficie_requerida: float,
        superficie_disponible: float,
        tipoCultivo: str
    ):
        """
        Inicializa excepcion de superficie insuficiente.

        Args:
            superficie_requerida: Espacio necesario para plantacion
            superficie_disponible: Espacio disponible en plantacion
            tipoCultivo: Tipo de cultivo que se quiere cultivar
        """
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible
        self._tipoCultivo = tipoCultivo

        user_msg = MensajesException.superficie_insuficiente_user(
            tipoCultivo, superficie_requerida, superficie_disponible
        )
        tech_msg = MensajesException.superficie_insuficiente_tech(
            tipoCultivo, superficie_requerida, superficie_disponible
        )

        super().__init__(user_msg, tech_msg)

    def get_superficie_requerida(self) -> float:
        """Retorna superficie requerida."""
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        """Retorna superficie disponible."""
        return self._superficie_disponible

    def get_tipoCultivo(self) -> str:
        """Retorna tipoCultivo intentada."""
        return self._tipoCultivo