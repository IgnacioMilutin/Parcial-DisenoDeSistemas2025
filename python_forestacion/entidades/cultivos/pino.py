from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO, ALTURA_INICIAL_ARBOL
from typing import Optional


class Pino(Arbol):
    def __init__(
        self,
        variedad: str,
        id_cultivo: Optional[int] = None
    ):
        
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=ALTURA_INICIAL_ARBOL,
            id_cultivo=id_cultivo
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

    def get_tipo_cultivo(self) -> str:
        return "Pino"