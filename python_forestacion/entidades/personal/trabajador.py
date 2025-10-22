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