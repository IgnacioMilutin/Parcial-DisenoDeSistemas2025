from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA, LECHUGA_EN_INVERNADERO
from typing import Optional


class Lechuga(Hortaliza):
    def __init__(self, variedad: str, id_cultivo: Optional[int] = None):
        
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=LECHUGA_EN_INVERNADERO,
            id_cultivo=id_cultivo
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

    def get_tipo_cultivo(self) -> str:
        return "Lechuga"