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
    