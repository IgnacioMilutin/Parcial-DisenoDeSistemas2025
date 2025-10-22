from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.constantes import (
    AGUA_MINIMA,
    CRECIMIENTO_PINO,
    CRECIMIENTO_OLIVO
)
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class PlantacionService:
    """
    Servicio para operaciones con plantaciones.
    """

    def __init__(self):
        """Inicializa servicio."""
        self._registry = CultivoServiceRegistry.get_instance()
        self._siguiente_id_cultivo = 1

    def plantar(
        self,
        plantacion: 'Plantacion',
        especie: str,
        cantidad: int
    ) -> None:
        """
        Planta cultivos en plantacion.

        Args:
            plantacion: Plantacion donde plantar
            especie: Tipo de cultivo (Pino, Olivo, Lechuga, Zanahoria)
            cantidad: Cantidad de cultivos a plantar

        Raises:
            SuperficieInsuficienteException: Si no hay espacio suficiente ⭐
            ValueError: Si cantidad invalida o especie desconocida
        """
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser positiva")

        cultivos_nuevos = []
        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            cultivos_nuevos.append(cultivo)

        superficie_requerida = sum(c.get_superficie() for c in cultivos_nuevos)

        superficie_disponible = plantacion.get_superficie_disponible()
        
        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                superficie_requerida=superficie_requerida,
                superficie_disponible=superficie_disponible,
                especie=especie
            )

        for cultivo in cultivos_nuevos:
            cultivo.set_id_cultivo(self._siguiente_id_cultivo)
            self._siguiente_id_cultivo += 1
            plantacion.agregar_cultivo(cultivo)

        print(f"[OK] Se plantaron {cantidad} {especie}(s)")
        print(f"     Superficie ocupada: {superficie_requerida:.2f} m²")
        print(f"     Superficie restante: {plantacion.get_superficie_disponible():.2f} m²")


    def regar(self, plantacion: 'Plantacion') -> None:
        """
        Riega todos los cultivos de plantacion.

        Args:
            plantacion: Plantacion a regar

        Raises:
            AguaAgotadaException: Si no hay agua suficiente ⭐
        """
        agua_disponible = plantacion.get_agua_disponible()
        
        if agua_disponible < AGUA_MINIMA:
            raise AguaAgotadaException(
                agua_requerida=AGUA_MINIMA,
                agua_disponible=agua_disponible,
                operacion="riego"
            )

        plantacion.set_agua_disponible(agua_disponible - AGUA_MINIMA)

        cultivos = plantacion.get_cultivos()
        
        for cultivo in cultivos:
            agua_absorbida = self._registry.absorber_agua(cultivo)

            tipo_cultivo = cultivo.get_tipo_cultivo()
            
            if tipo_cultivo == "Pino":
                from python_forestacion.entidades.cultivos.pino import Pino
                if isinstance(cultivo, Pino):
                    altura_antes = cultivo.get_altura()
                    cultivo.crecer(CRECIMIENTO_PINO)
                    altura_despues = cultivo.get_altura()
                    print(f"     Pino ID {cultivo.get_id_cultivo()}: {altura_antes:.2f}m → {altura_despues:.2f}m")
                    
            elif tipo_cultivo == "Olivo":
                from python_forestacion.entidades.cultivos.olivo import Olivo
                if isinstance(cultivo, Olivo):
                    altura_antes = cultivo.get_altura()
                    cultivo.crecer(CRECIMIENTO_OLIVO)
                    altura_despues = cultivo.get_altura()
                    print(f"     Olivo ID {cultivo.get_id_cultivo()}: {altura_antes:.2f}m → {altura_despues:.2f}m")

        print(f"[OK] Riego completado. Agua restante: {plantacion.get_agua_disponible():.1f}L")

    def cosechar_cultivos_tipo(self, plantacion: 'Plantacion', tipo: str) -> list:
        """
        Cosecha todos los cultivos de un tipo especifico.

        Args:
            plantacion: Plantacion donde cosechar
            tipo: Tipo de cultivo a cosechar (Pino, Lechuga, etc)

        Returns:
            list: Cultivos cosechados (removidos de plantacion)
        """
        cultivos = plantacion.get_cultivos()
        cosechados = [c for c in cultivos if c.get_tipo_cultivo() == tipo]

        for cultivo in cosechados:
            plantacion.eliminar_cultivo(cultivo)

        print(f"[OK] Se cosecharon {len(cosechados)} {tipo}(s)")
        return cosechados

    def fumigar(self, plantacion: 'Plantacion', plaguicida: str) -> None:
        """
        Fumiga todos los cultivos de la plantacion.

        Args:
            plantacion: Plantacion a fumigar
            plaguicida: Tipo de plaguicida a usar
        """
        cultivos = plantacion.get_cultivos()
        print(f"[OK] Fumigando {len(cultivos)} cultivos con: {plaguicida}")