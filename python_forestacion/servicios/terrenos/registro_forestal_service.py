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