"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/terrenos
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ================================================================================

import pickle
import os
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA
from python_forestacion.excepciones.persistencia_exception import (
    PersistenciaException,
    TipoOperacionPersistencia
)


class RegistroForestalService:
    """
    Servicio para persistencia de registros forestales.
    
    Usa Pickle para serializacion
    """

    def persistir(self, registro: RegistroForestal) -> None:
        """
        Guarda registro forestal en disco.

        Args:
            registro: Registro a persistir

        Raises:
            PersistenciaException: Si hay error de guardado

        Archivo generado: data/{propietario}.dat
        """
        nombre_archivo = None
        
        try:
            if not os.path.exists(DIRECTORIO_DATA):
                os.makedirs(DIRECTORIO_DATA)

            propietario = registro.get_propietario()
            if not propietario or not propietario.strip():
                raise ValueError("El propietario no puede estar vacio")

            nombre_archivo = f"{DIRECTORIO_DATA}/{propietario}{EXTENSION_DATA}"

            with open(nombre_archivo, 'wb') as archivo:
                pickle.dump(registro, archivo)

            print(f"[OK] Registro de {propietario} persistido en {nombre_archivo}")

        except (IOError, OSError, pickle.PicklingError) as e:
            raise PersistenciaException(
                tipo_operacion=TipoOperacionPersistencia.GUARDADO,
                nombre_archivo=nombre_archivo if nombre_archivo else "desconocido",
                causa=e
            )
        except ValueError as e:
            raise e

    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """
        Recupera registro forestal desde disco.

        Args:
            propietario: Nombre del propietario

        Returns:
            RegistroForestal: Registro recuperado

        Raises:
            PersistenciaException: Si archivo no existe o esta corrupto 
            ValueError: Si propietario vacio

        Archivo buscado: data/{propietario}.dat
        """
        nombre_archivo = None
        
        try:
            if not propietario or not propietario.strip():
                raise ValueError("El propietario no puede estar vacio")

            nombre_archivo = f"{DIRECTORIO_DATA}/{propietario}{EXTENSION_DATA}"

            if not os.path.exists(nombre_archivo):
                raise FileNotFoundError(f"Archivo no encontrado: {nombre_archivo}")

            with open(nombre_archivo, 'rb') as archivo:
                registro = pickle.load(archivo)

            print(f"[OK] Registro de {propietario} recuperado desde {nombre_archivo}")
            return registro

        except (IOError, OSError, pickle.UnpicklingError, FileNotFoundError) as e:
            raise PersistenciaException(
                tipo_operacion=TipoOperacionPersistencia.LECTURA,
                nombre_archivo=nombre_archivo if nombre_archivo else "desconocido",
                causa=e
            )
        except ValueError as e:
            # Re-lanzar ValueError si es de validacion
            raise e

    @staticmethod
    def mostrar_datos(registro: RegistroForestal) -> None:
        """
        Muestra datos completos del registro forestal.

        Args:
            registro: Registro a mostrar
        """
        print("\n" + "=" * 70)
        print("REGISTRO FORESTAL")
        print("=" * 70)
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo()}")

        tierra = registro.get_tierra()
        plantacion = registro.get_plantacion()

        print(f"Domicilio:   {tierra.get_domicilio()}")
        print(f"Superficie:  {tierra.get_superficie()} m²")

        cultivos = plantacion.get_cultivos()
        print(f"Cantidad de cultivos plantados: {len(cultivos)}")

        if cultivos:
            print("\nListado de Cultivos plantados")
            print("_" * 70)

            from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
            registry = CultivoServiceRegistry.get_instance()

            for cultivo in cultivos:
                print()
                registry.mostrar_datos(cultivo)

        print("\n" + "=" * 70)

# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

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

