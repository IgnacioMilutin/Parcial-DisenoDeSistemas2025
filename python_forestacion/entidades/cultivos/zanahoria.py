from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA, ZANAHORIA_EN_INVERNADERO
from typing import Optional


class Zanahoria(Hortaliza):
    def __init__(self, is_baby_carrot: bool = False, id_cultivo: Optional[int] = None):
        
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=ZANAHORIA_EN_INVERNADERO,
            id_cultivo=id_cultivo
        )
        self._is_baby_carrot = is_baby_carrot

    def is_baby_carrot(self) -> bool:
        return self._is_baby_carrot

    def set_baby_carrot(self, is_baby_carrot: bool) -> None:
        self._is_baby_carrot = is_baby_carrot

    def get_tipo_cultivo(self) -> str:
        return "Zanahoria"