"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/terrenos
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================


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

# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================

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


