from typing import List, Optional, TYPE_CHECKING
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:

    def __init__(
        self,
        nombre: str,
        superficie: float,
        agua: float = AGUA_INICIAL_PLANTACION
    ):
       
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")

        self._nombre = nombre
        self._superficie_maxima = superficie
        self._agua_disponible = agua
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []

    # GETTERS Y SETTERS

    def get_nombre(self) -> str:
        return self._nombre

    def get_superficie_maxima(self) -> float:
        return self._superficie_maxima

    def get_agua_disponible(self) -> float:
        return self._agua_disponible

    def get_cultivos(self) -> List['Cultivo']:
        return self._cultivos.copy()
    def get_cultivos_interno(self) -> List['Cultivo']:
        return self._cultivos

    def get_trabajadores(self) -> List['Trabajador']:
        return self._trabajadores.copy()
    def get_trabajadores_interno(self) -> List['Trabajador']:
        return self._trabajadores

    def get_superficie_ocupada(self) -> float:
        return sum(cultivo.get_superficie() for cultivo in self._cultivos)

    def get_superficie_disponible(self) -> float:
        return self._superficie_maxima - self.get_superficie_ocupada()

    def set_nombre(self, nombre: str) -> None:
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nombre

    def set_agua_disponible(self, agua: float) -> None:
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua_disponible = agua

    def set_cultivos(self, cultivos: List['Cultivo']) -> None:
        self._cultivos = cultivos.copy() if cultivos else []

    def set_trabajadores(self, trabajadores: List['Trabajador']) -> None:
        self._trabajadores = trabajadores.copy() if trabajadores else []

    # OPERACIONES 

    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        self._cultivos.append(cultivo)

    def eliminar_cultivo(self, cultivo: 'Cultivo') -> None:
        if cultivo in self._cultivos:
            self._cultivos.remove(cultivo)

    def agregar_trabajador(self, trabajador: 'Trabajador') -> None:
        self._trabajadores.append(trabajador)

    def eliminar_trabajador(self, trabajador: 'Trabajador') -> None:
        if trabajador in self._trabajadores:
            self._trabajadores.remove(trabajador)
