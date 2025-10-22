from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO, ALTURA_INICIAL_OLIVO
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from typing import Optional

class Olivo(Arbol):
    def __init__(
        self,
        tipo_aceituna: str,
        id_cultivo: Optional[int] = None
    ):
        
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=ALTURA_INICIAL_OLIVO,
            id_cultivo=id_cultivo
        )
        self._fruto = tipo_aceituna

    def get_tipo_aceituna(self) -> str:
        return self._fruto

    def set_tipo_aceituna(self, tipo_aceituna: str) -> None:
        self._fruto = tipo_aceituna

    def get_tipo_cultivo(self) -> str:
        return "Olivo"