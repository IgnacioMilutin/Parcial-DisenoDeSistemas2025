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