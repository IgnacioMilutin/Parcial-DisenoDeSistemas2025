"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """
    Servicio para cultivos tipo Arbol (Pino, Olivo). 
    """

    def crecer(self, cultivo: 'Arbol', cantidad: float) -> None:
        """
        Hace crecer el arbol.

        Args:
            cultivo: Arbol a hacer crecer
            cantidad: Metros a crecer
        """
        cultivo.crecer(cantidad)

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Arbol') -> None:
        pass

# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

"""
Servicio base para cultivos.

Operaciones sobre cultivos
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService(ABC):
    """
    Servicio base abstracto para cultivos.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inicializa servicio con estrategia inyectada.

        Args:
            estrategia_absorcion: Strategy para calcular absorcion(Seasonal o Constante)
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        """
        Absorbe agua en cultivo usando Strategy.

        Args:
            cultivo: Cultivo que absorbe agua

        Returns:
            int: Litros absorbidos
        """
        fecha_hoy = date.today()
        cantidad_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha=fecha_hoy,
            temperatura=0.0,  
            humedad=0.0,      
            cultivo=cultivo
        )

        agua_actual = cultivo.get_agua()
        cultivo.set_agua(agua_actual + cantidad_absorvida)

        return cantidad_absorvida

    @abstractmethod
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos especificos del cultivo.

        Args:
            cultivo: Cultivo a mostrar
        """
        pass

    def _mostrar_datos_base(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos comunes a todos los cultivos.

        Args:
            cultivo: Cultivo a mostrar
        """
        print(f"Cultivo: {cultivo.get_tipo_cultivo()}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")
        if cultivo.get_id_cultivo() is not None:
            print(f"ID: {cultivo.get_id_cultivo()}")

# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

from threading import Lock
from typing import TYPE_CHECKING, Dict, Callable, Optional

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class CultivoServiceRegistry:
    """
    Registry Singleton para servicios de cultivos.
    """

    _instance: Optional['CultivoServiceRegistry'] = None
    _lock = Lock()

    def __new__(cls) -> 'CultivoServiceRegistry':
        """
        Controla la creacion de instancia.
        
        Retorna la instancia (nueva o existente).
        """

        if cls._instance is None: 
            with cls._lock: 
                if cls._instance is None: 
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Inicializa el registry.
        """

        if hasattr(self, '_inicializado') and self._inicializado:
            return

        from python_forestacion.servicios.cultivos.pino_service import PinoService
        from python_forestacion.servicios.cultivos.olivo_service import OlivoService
        from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
        from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        self._absorber_agua_handlers: Dict[type, Callable] = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

        self._mostrar_datos_handlers: Dict[type, Callable] = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

        self._inicializado = True

    @classmethod
    def get_instance(cls) -> 'CultivoServiceRegistry':
        """
        Retorna la instancia unica del registry.
        """
        if cls._instance is None:
            cls()  
        return cls._instance

    def absorber_agua(self, cultivo: 'Cultivo') -> int:
        """
        Absorbe agua en cultivo
        """
        tipo = type(cultivo)

        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo de cultivo desconocido: {tipo}")

        handler = self._absorber_agua_handlers[tipo]
        return handler(cultivo)

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos especificos del cultivo (dispatch polimorfico).
        """
        tipo = type(cultivo)

        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo de cultivo desconocido: {tipo}")

        handler = self._mostrar_datos_handlers[tipo]
        handler(cultivo)

    def _absorber_agua_pino(self, cultivo: 'Pino') -> int:
        return self._pino_service.absorver_agua(cultivo)

    def _absorber_agua_olivo(self, cultivo: 'Olivo') -> int:
        return self._olivo_service.absorver_agua(cultivo)

    def _absorber_agua_lechuga(self, cultivo: 'Lechuga') -> int:
        return self._lechuga_service.absorver_agua(cultivo)

    def _absorber_agua_zanahoria(self, cultivo: 'Zanahoria') -> int:
        return self._zanahoria_service.absorver_agua(cultivo)

    def _mostrar_datos_pino(self, cultivo: 'Pino') -> None:
        self._pino_service.mostrar_datos(cultivo)

    def _mostrar_datos_olivo(self, cultivo: 'Olivo') -> None:
        self._olivo_service.mostrar_datos(cultivo)

    def _mostrar_datos_lechuga(self, cultivo: 'Lechuga') -> None:
        self._lechuga_service.mostrar_datos(cultivo)

    def _mostrar_datos_zanahoria(self, cultivo: 'Zanahoria') -> None:
        self._zanahoria_service.mostrar_datos(cultivo)

# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_LECHUGA
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """
    Servicio para Lechugas.
    """

    def __init__(self):
        """Inicializa con estrategia constante."""
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_LECHUGA))

    def mostrar_datos(self, cultivo: 'Lechuga') -> None:
        """Muestra datos de la lechuga."""
        self._mostrar_datos_base(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")
        print(f"Invernadero: {'Si' if cultivo.get_invernadero() else 'No'}")

# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """
    Servicio para Olivos.
    """

    def __init__(self):
        """Inicializa con estrategia seasonal."""
        super().__init__(AbsorcionSeasonalStrategy())

    def mostrar_datos(self, cultivo: 'Olivo') -> None:
        """Muestra datos del olivo."""
        self._mostrar_datos_base(cultivo)
        print(f"Altura: {cultivo.get_altura()} m")
        print(f"Tipo de aceituna: {cultivo.get_tipo_aceituna()}")


# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================

from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """
    Servicio para Pinos.
    """

    def __init__(self):
        """Inicializa con estrategia seasonal."""
        super().__init__(AbsorcionSeasonalStrategy())

    def mostrar_datos(self, cultivo: 'Pino') -> None:
        """Muestra datos del pino."""
        self._mostrar_datos_base(cultivo)
        print(f"Altura: {cultivo.get_altura()} m")
        print(f"Variedad: {cultivo.get_variedad()}")

# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

from python_forestacion.constantes import ABSORCION_ZANAHORIA
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """
    Servicio para Zanahorias.
    """

    def __init__(self):
        """Inicializa con estrategia constante."""
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_ZANAHORIA))

    def mostrar_datos(self, cultivo: 'Zanahoria') -> None:
        """Muestra datos de la zanahoria."""
        self._mostrar_datos_base(cultivo)
        tipo = "Baby carrot" if cultivo.is_baby_carrot() else "Regular"
        print(f"Tipo: {tipo}")
        print(f"Campo abierto: {'Si' if not cultivo.get_invernadero() else 'No'}")

