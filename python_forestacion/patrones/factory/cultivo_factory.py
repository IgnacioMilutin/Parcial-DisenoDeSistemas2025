from typing import Dict, Callable, Optional
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.constantes import (
    ALTURA_INICIAL_ARBOL
)


class CultivoFactory:

    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        """
        Crea un cultivo del tipo especificado.

        Args:
            especie: Tipo de cultivo ("Pino", "Olivo", "Lechuga", "Zanahoria")

        Returns:
            Cultivo: Instancia del tipo especificado, invocando al metodo correspondiente

        Raises:
            ValueError: Si especie es desconocida

        """

        factories: Dict[str, Callable[[], Cultivo]] = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(
                f"Especie desconocida: '{especie}'. "
                f"Especies validas: {', '.join(factories.keys())}"
            )

        factory_metodo: Callable[[], Cultivo] = factories[especie]
        return factory_metodo()


    @staticmethod
    def _crear_pino() -> Cultivo:
        """
        Factory para Pino.
        Crea con variedad por defecto 'piñonero'
        
        Returns:
            pino creado
        """
        from python_forestacion.entidades.cultivos.pino import Pino
        pino = Pino(variedad="Parana")

        return pino 

    @staticmethod
    def _crear_olivo() -> Cultivo:
        """
        Factory para Olivo.
        Crea con tipo de aceituna 'verde' por defecto

        Returns:
            olivo creado
        """
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

        olivo = Olivo(tipo_aceituna=TipoAceituna.VERDE)

        return olivo

    @staticmethod
    def _crear_lechuga() -> Cultivo:
        """
        Factory para Lechuga.
        Crea con variedad 'romana' por defecto

        Returns:
            lechuga creada
        """
        from python_forestacion.entidades.cultivos.lechuga import Lechuga

        lechuga = Lechuga(variedad="romana")

        return lechuga

    @staticmethod
    def _crear_zanahoria() -> Cultivo:
        """
        Factory para Zanahoria.
        La creada por defecto no es baby carrot
        
        Returns:
            Zanahoria creada
        """
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

        zanahoria = Zanahoria(is_baby_carrot=False)

        return zanahoria