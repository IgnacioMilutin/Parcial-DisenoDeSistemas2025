
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:

    def __init__(
        self,
        id_padron: int,
        tierra: 'Tierra',
        plantacion: 'Plantacion',
        propietario: str,
        avaluo: float
    ):
        if not tierra or not plantacion:
            raise ValueError("Tierra y plantacion son obligatorias")
        if not propietario or not propietario.strip():
            raise ValueError("El propietario no puede estar vacio")
        if avaluo < 0:
            raise ValueError("El avaluo no puede ser negativo")

        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    # GETTERS Y SETTERS

    def get_id_padron(self) -> int:
        return self._id_padron

    def get_tierra(self) -> 'Tierra':
        return self._tierra

    def get_plantacion(self) -> 'Plantacion':
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo

    def set_propietario(self, propietario: str) -> None:  
        if not propietario or not propietario.strip():
            raise ValueError("El propietario no puede estar vacio")
        self._propietario = propietario

    def set_avaluo(self, avaluo: float) -> None:
        if avaluo < 0:
            raise ValueError("El avaluo no puede ser negativo")
        self._avaluo = avaluo