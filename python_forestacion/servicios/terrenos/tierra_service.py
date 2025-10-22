"""
Servicio para gestion de terrenos (Tierra).
"""

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


class TierraService:
    """Servicio para operaciones con terrenos."""

    @staticmethod
    def crear_tierra_con_plantacion(
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea un terreno con plantacion asociada.

        Args:
            id_padron_catastral: Numero de padron
            superficie: Metros cuadrados del terreno
            domicilio: Ubicacion del terreno
            nombre_plantacion: Nombre de la plantacion

        Returns:
            Tierra: Terreno con plantacion ya asociada
        """
        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie=superficie
        )

        tierra = Tierra(
            id_padron_catastral=id_padron_catastral,
            superficie=superficie,
            domicilio=domicilio,
            finca=plantacion
        )

        return tierra