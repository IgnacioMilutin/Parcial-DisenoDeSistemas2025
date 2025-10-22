from python_forestacion.entidades.cultivos.cultivo import Cultivo
from typing import Optional


class Arbol(Cultivo):
    def __init__(
        self,
        agua: int,
        superficie: float,
        altura: float = 1.0,
        id_cultivo: Optional[int] = None
    ):
        
        super().__init__(agua, superficie, id_cultivo)
        if altura <= 0:
            raise ValueError("La altura debe ser positiva")
        self._altura = altura

    def get_altura(self) -> float:
        return self._altura

    def set_altura(self, altura: float) -> None:
        if altura <= 0:
            raise ValueError("La altura debe ser positiva")
        self._altura = altura

    def crecer(self, cantidad: float) -> None:
        self.set_altura(self._altura + cantidad)