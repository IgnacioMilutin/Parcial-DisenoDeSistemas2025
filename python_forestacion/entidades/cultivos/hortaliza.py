from python_forestacion.entidades.cultivos.cultivo import Cultivo
from typing import Optional


class Hortaliza(Cultivo):
    def __init__(
        self,
        agua: int,
        superficie: float,
        invernadero: bool,
        id_cultivo: Optional[int] = None
    ):
        super().__init__(agua, superficie, id_cultivo)
        self._invernadero = invernadero

    def get_invernadero(self) -> bool:
        return self._invernadero

    def set_invernadero(self, invernadero: bool) -> None:
        self._invernadero = invernadero