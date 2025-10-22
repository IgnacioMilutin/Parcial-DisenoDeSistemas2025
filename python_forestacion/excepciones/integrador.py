"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================



from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import MensajesException


class AguaAgotadaException(ForestacionException):
    """
    Excepcion lanzada cuando no hay suficiente agua para riego.
    """

    def __init__(
        self,
        agua_requerida: float,
        agua_disponible: float,
        operacion: str = "riego"
    ):
        """
        Inicializa excepcion de agua agotada.

        Args:
            agua_requerida: Litros necesarios para operacion
            agua_disponible: Litros disponibles
            operacion: Tipo de operacion (riego, cosecha, etc)
        """
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible
        self._operacion = operacion

        user_msg = MensajesException.agua_agotada_user(
            operacion, agua_requerida, agua_disponible
        )
        tech_msg = MensajesException.agua_agotada_tech(
            operacion, agua_requerida, agua_disponible
        )

        super().__init__(user_msg, tech_msg)

    def get_agua_requerida(self) -> float:
        """Retorna agua requerida."""
        return self._agua_requerida

    def get_agua_disponible(self) -> float:
        """Retorna agua disponible."""
        return self._agua_disponible



# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

"""
Excepciones base del sistema forestal.

"""


class ForestacionException(Exception):
    """
    Excepcion base de todas las excepciones del sistema forestal.
    """

    def __init__(self, user_message: str, technical_message: str = ""):
        """
        Inicializa excepcion forestal.

        Args:
            user_message: Mensaje para usuario final
            technical_message: Mensaje tecnico para desarrolladores
        """
        self._user_message = user_message
        self._technical_message = technical_message or user_message
        super().__init__(self._user_message)

    def get_user_message(self) -> str:
        """Retorna mensaje para usuario final."""
        return self._user_message

    def get_technical_message(self) -> str:
        """Retorna mensaje tecnico."""
        return self._technical_message

    def get_full_message(self) -> str:
        """Retorna ambos mensajes combinados."""
        return f"[USER] {self._user_message}\n[TECH] {self._technical_message}"


# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones/mensajes_exception.py
# ================================================================================

"""
Mensajes centralizados de excepciones.
"""


class MensajesException:
    """Clase con mensajes estáticos para excepciones."""

    @staticmethod
    def superficie_insuficiente_user(
        tipoCultivo: str,
        requerida: float,
        disponible: float
    ) -> str:
        """Mensaje de usuario para superficie insuficiente."""
        return (
            f"No hay suficiente espacio para plantar {tipoCultivo}. "
            f"Se requieren {requerida:.2f} m², "
            f"pero solo hay {disponible:.2f} m² disponibles."
        )

    @staticmethod
    def superficie_insuficiente_tech(
        tipoCultivo: str,
        requerida: float,
        disponible: float
    ) -> str:
        """Mensaje técnico para superficie insuficiente."""
        return (
            f"SuperficieInsuficiente: "
            f"especie={tipoCultivo}, "
            f"requerida={requerida}, "
            f"disponible={disponible}"
        )

    @staticmethod
    def agua_agotada_user(
        operacion: str,
        requerida: float,
        disponible: float
    ) -> str:
        """Mensaje de usuario para agua agotada."""
        return (
            f"El agua se ha agotado para realizar {operacion}. "
            f"Se requieren {requerida:.2f}L, "
            f"pero solo hay {disponible:.2f}L disponibles."
        )

    @staticmethod
    def agua_agotada_tech(
        operacion: str,
        requerida: float,
        disponible: float
    ) -> str:
        """Mensaje técnico para agua agotada."""
        return (
            f"AguaAgotada: "
            f"operacion={operacion}, "
            f"requerida={requerida}, "
            f"disponible={disponible}"
        )

    @staticmethod
    def persistencia_user(tipo_operacion: str, nombre_archivo: str) -> str:
        """Mensaje de usuario para error de persistencia."""
        return (
            f"Error durante {tipo_operacion} del archivo '{nombre_archivo}'. "
            f"Verifique permisos y espacio en disco."
        )

    @staticmethod
    def persistencia_tech(
        tipo_operacion: str,
        nombre_archivo: str,
        causa: str = ""
    ) -> str:
        """Mensaje técnico para error de persistencia."""
        causa_str = f"\nCausa original: {causa}" if causa else ""
        return (
            f"PersistenciaException: "
            f"operacion={tipo_operacion}, "
            f"archivo={nombre_archivo}{causa_str}"
        )

# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================



from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import MensajesException

class SuperficieInsuficienteException(ForestacionException):
    """
    Excepcion lanzada cuando no hay suficiente superficie para plantar.
    
    Ocurre cuando:
    - Se intenta plantar cultivos que requieren mas espacio del disponible
    """

    def __init__(
        self,
        superficie_requerida: float,
        superficie_disponible: float,
        tipoCultivo: str
    ):
        """
        Inicializa excepcion de superficie insuficiente.

        Args:
            superficie_requerida: Espacio necesario para plantacion
            superficie_disponible: Espacio disponible en plantacion
            tipoCultivo: Tipo de cultivo que se quiere cultivar
        """
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible
        self._tipoCultivo = tipoCultivo

        user_msg = MensajesException.superficie_insuficiente_user(
            tipoCultivo, superficie_requerida, superficie_disponible
        )
        tech_msg = MensajesException.superficie_insuficiente_tech(
            tipoCultivo, superficie_requerida, superficie_disponible
        )

        super().__init__(user_msg, tech_msg)

    def get_superficie_requerida(self) -> float:
        """Retorna superficie requerida."""
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        """Retorna superficie disponible."""
        return self._superficie_disponible

    def get_tipoCultivo(self) -> str:
        """Retorna tipoCultivo intentada."""
        return self._tipoCultivo

