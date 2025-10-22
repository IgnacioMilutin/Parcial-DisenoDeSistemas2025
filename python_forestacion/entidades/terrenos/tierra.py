from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:

    def __init__(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        finca: Optional['Plantacion'] = None
    ):
        
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        if not isinstance(id_padron_catastral, int):
            raise ValueError("El padron debe ser numero entero")
        if not domicilio or not domicilio.strip():
            raise ValueError("El domicilio no puede estar vacio")

        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca = finca

    # GETTERS Y SETTERS

    def get_id_padron_catastral(self) -> int:
        return self._id_padron_catastral

    def get_superficie(self) -> float:
        return self._superficie

    def get_domicilio(self) -> str:
        return self._domicilio

    def get_finca(self) -> Optional['Plantacion']:
        return self._finca

    def set_superficie(self, superficie: float) -> None: 
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie

    def set_domicilio(self, domicilio: str) -> None:
        if not domicilio or not domicilio.strip():
            raise ValueError("El domicilio no puede estar vacio")
        self._domicilio = domicilio

    def set_finca(self, finca: 'Plantacion') -> None:
        self._finca = finca
