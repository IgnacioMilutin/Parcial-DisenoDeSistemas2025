from enum import Enum
from typing import Optional

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import MensajesException


class TipoOperacionPersistencia(Enum):
    """Tipos de operaciones de persistencia."""
    GUARDADO = "GUARDADO"
    LECTURA = "LECTURA"
    DESERIALIZACION = "DESERIALIZACION"


class PersistenciaException(ForestacionException):
    """
    Excepcion para errores de persistencia/serializacion.
    """

    def __init__(
        self,
        tipo_operacion: TipoOperacionPersistencia,
        nombre_archivo: str,
        causa: Optional[Exception] = None
    ):
        """
        Inicializa excepcion de persistencia.

        Args:
            tipo_operacion: GUARDADO, LECTURA, o DESERIALIZACION
            nombre_archivo: Archivo que causo el error
            causa: Excepcion original (opcional)
        """
        self._tipo_operacion = tipo_operacion
        self._nombre_archivo = nombre_archivo
        self._causa = causa

        user_msg = MensajesException.persistencia_user(
            tipo_operacion.value, nombre_archivo
        )
        tech_msg = MensajesException.persistencia_tech(
            tipo_operacion.value, nombre_archivo, str(causa) if causa else ""
        )

        super().__init__(user_msg, tech_msg)

    def get_tipo_operacion(self) -> TipoOperacionPersistencia:
        """Retorna tipo de operacion que fallo."""
        return self._tipo_operacion

    def get_nombre_archivo(self) -> str:
        """Retorna nombre del archivo."""
        return self._nombre_archivo

    def get_causa(self) -> Optional[Exception]:
        """Retorna excepcion original."""
        return self._causa