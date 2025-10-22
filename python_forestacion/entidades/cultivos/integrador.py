"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================

from abc import ABC, abstractmethod
from typing import Optional


class Cultivo(ABC):

    #CONSTRUCTOR
    def __init__(
        self,
        agua:int,
        superficie:float,
        id_cultivo: Optional[int] = None
        ):

        if agua < 0:
            raise ValueError('El agua no puede ser negativa')
        if superficie <= 0:
            raise ValueError('La superficie debe ser mayor o igual a cero')
        
        self._agua = agua
        self._superficie = superficie
        self._id_cultivo = id_cultivo

    #GETTERS
    def get_agua(self)->int:
        return self._agua
    
    def get_superficie(self)->float:
        return self._superficie
    
    def get_id_cultivo(self) -> Optional[int]:
        return self._id_cultivo
    
    #SETTERS
    def set_agua(self, agua: float) -> None:
        
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua = agua

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie

    def set_id_cultivo(self, id_cultivo: int) -> None:
        self._id_cultivo = id_cultivo

   #METODOS

    @abstractmethod
    def get_tipo_cultivo(self) -> str:
        pass

# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/pino.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================

class TipoAceituna:
    NEGRA = "Negra"
    VERDE = "Verde"
    ROJA = "Roja"

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================

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

