"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/personal
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

from datetime import date
from typing import Optional


class AptoMedico:

    def __init__(
        self,
        apto: bool,
        fecha_emision: date,
        observaciones: str = ""
    ):
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    # GETTERS Y SETTERS
 
    def esta_apto(self) -> bool:
        return self._apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_observaciones(self) -> str:
        return self._observaciones

    def set_apto(self, apto: bool) -> None:
        self._apto = apto

    def set_observaciones(self, observaciones: str) -> None:
        self._observaciones = observaciones

    def toString(self):
        return print(f"Apto: {self._apto} | Fecha: {self._fecha_emision} | Observaciones: {self._observaciones}")

# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

class Herramienta:

    def __init__(
        self,
        id_herramienta: int,
        nombre: str,
        certificado_hys: bool = True
    ):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")

        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    # GETTERS Y SETTERS

    def get_id_herramienta(self) -> int:
        return self._id_herramienta

    def get_nombre(self) -> str:
        return self._nombre

    def tiene_certificado_hys(self) -> bool:
        return self._certificado_hys
    
    def set_nombre(self,nombre: str):
        self._nombre=nombre

    def set_certificado(self,certificado_hys: bool):
        self._certificado_hys=certificado_hys

# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/personal/tarea.py
# ================================================================================

from datetime import date


class Tarea:

    def __init__(self,id_tarea: int,fecha: date,descripcion: str,completada: bool = False):
        self._id_tarea = id_tarea
        self._fecha = fecha
        self._descripcion = descripcion
        self._completada = completada

    # GETTERS Y SETTERS

    def get_id_tarea(self) -> int:
        return self._id_tarea

    def get_fecha_programada(self) -> date:
        return self._fecha

    def get_descripcion(self) -> str:
        return self._descripcion

    def esta_completada(self) -> bool:
        return self._completada

    def set_completada(self, completada: bool) -> None:
        self._completada = completada

    def toString(self):
        return print(f"ID TAREA: {self._id_tarea} \n Fecha: {self._fecha} \n Descripción: {self._descripcion} \n Esta completada?: {self._completada}")
    

# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

from typing import List, Optional, TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.apto_medico import AptoMedico
    from python_forestacion.entidades.personal.tarea import Tarea


class Trabajador:
    
    def __init__(
        self,
        dni: int,
        nombre: str,
        tareas: Optional[List['Tarea']] = None,
        apto_medico: Optional['AptoMedico'] = None
    ):
        
        if dni <= 0:
            raise ValueError("DNI debe ser numero positivo")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")

        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas.copy() if tareas else []
        self._apto_medico = apto_medico

    # GETTERS Y SETTERS

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_tareas(self) -> List['Tarea']:
        return self._tareas.copy()

    def get_apto_medico(self) -> Optional['AptoMedico']:
        return self._apto_medico
    
    def set_nombre(self, nombre: str) -> None:
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nombre

    def set_tareas(self, tareas: List['Tarea']) -> None:
        self._tareas = tareas.copy() if tareas else []

    def set_apto_medico(self, apto_medico: 'AptoMedico') -> None:
        self._apto_medico = apto_medico

        
    # OPERACIONES

    def agregar_tarea(self, tarea: 'Tarea') -> None:
        self._tareas.append(tarea)

    def eliminar_tarea(self, tarea: 'Tarea') -> None:
        if tarea in self._tareas:
            self._tareas.remove(tarea)

