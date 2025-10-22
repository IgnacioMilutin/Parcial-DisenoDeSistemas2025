"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/negocio
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/negocio/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: fincas_service.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/negocio/fincas_service.py
# ================================================================================

from typing import Dict, List, Type, TypeVar
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

T = TypeVar('T')


class FincasService:
    """
    Servicio de alto nivel para gestion de multiples fincas.
    """

    def __init__(self):
        """Inicializa servicio de fincas."""
        self._fincas: Dict[int, RegistroForestal] = {}
        self._plantacion_service = PlantacionService()

    def add_finca(self, registro: RegistroForestal) -> None:
        """
        Agrega una finca al portafolio.

        Args:
            registro: Registro forestal a agregar
        """
        id_padron = registro.get_id_padron()
        self._fincas[id_padron] = registro
        print(f"[OK] Finca {id_padron} agregada al portafolio")

    def buscar_finca(self, id_padron: int) -> RegistroForestal:
        """
        Busca una finca por ID de padron.

        Args:
            id_padron: ID del padron a buscar

        Returns:
            RegistroForestal: Registro forestal

        Raises:
            KeyError: Si finca no existe
        """
        if id_padron not in self._fincas:
            raise KeyError(f"Finca con padron {id_padron} no encontrada")
        return self._fincas[id_padron]

    def get_cantidad_fincas(self) -> int:
        """Retorna cantidad de fincas en portafolio."""
        return len(self._fincas)

    def listar_fincas(self) -> List[RegistroForestal]:
        """
        Lista todas las fincas del portafolio.
        
        Returns:
            List[RegistroForestal]: Lista de registros forestales
        """
        return list(self._fincas.values())

    

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """
        Fumiga una finca especifica.

        Args:
            id_padron: ID de padron a fumigar
            plaguicida: Tipo de plaguicida a usar

        Raises:
            KeyError: Si finca no existe
        """
        registro = self.buscar_finca(id_padron)
        plantacion = registro.get_plantacion()
        self._plantacion_service.fumigar(plantacion, plaguicida)

    def regar_finca(self, id_padron: int) -> None:
        """
        Riega una finca especifica.

        Args:
            id_padron: ID de padron a regar

        Raises:
            KeyError: Si finca no existe
            AguaAgotadaException: Si no hay suficiente agua
        """
        registro = self.buscar_finca(id_padron)
        plantacion = registro.get_plantacion()
        self._plantacion_service.regar(plantacion)

    def regar_todas_fincas(self) -> None:
        """
        Riega todas las fincas del portafolio.
        """
        from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
        
        print(f"\n[INFO] Regando todas las fincas ({self.get_cantidad_fincas()} fincas)...")
        
        for id_padron, registro in self._fincas.items():
            try:
                plantacion = registro.get_plantacion()
                self._plantacion_service.regar(plantacion)
                print(f"  [OK] Finca {id_padron} regada exitosamente")
            except AguaAgotadaException as e:
                print(f"  [!] Finca {id_padron}: {e.get_user_message()}")

    def cosechar_y_empaquetar(self, tipo_cultivo: Type[T]) -> Paquete[T]:
        """
        Cosecha todos los cultivos de un tipo de TODAS las fincas
        y los empaqueta.

        Args:
            tipo_cultivo: Clase del cultivo a cosechar

        Returns:
            Paquete[T]: Paquete con cultivos cosechados
        """
        
        tipo_nombre = tipo_cultivo.__name__

        print(f"\nCOSECHANDO {tipo_nombre} de todas las fincas...")
        print("-" * 70)

        
        cultivos_cosechados: List[T] = []

        for id_padron, registro in self._fincas.items():
            plantacion = registro.get_plantacion()

            cultivos = plantacion.get_cultivos()
            cultivos_tipo = [
                c for c in cultivos
                if isinstance(c, tipo_cultivo)
            ]

            for cultivo in cultivos_tipo:
                plantacion.eliminar_cultivo(cultivo)
                cultivos_cosechados.append(cultivo)

            if cultivos_tipo:
                print(f"  Finca {id_padron}: {len(cultivos_tipo)} {tipo_nombre}(s) cosechado(s)")

        paquete = Paquete(cultivos_cosechados)

        print(f"\nTOTAL COSECHADO: {len(cultivos_cosechados)} unidades de {tipo_nombre}")
        paquete.mostrar_contenido_caja()

        return paquete

    def obtener_reporte_general(self) -> None:
        """
        Muestra reporte general de todas las fincas.
        """
        print("\n" + "=" * 70)
        print("REPORTE GENERAL DEL PORTAFOLIO DE FINCAS")
        print("=" * 70)
        
        total_fincas = len(self._fincas)
        total_cultivos = 0
        total_agua = 0.0
        total_superficie = 0.0
        
        # Contadores por tipo
        contadores_tipo = {}
        
        for registro in self._fincas.values():
            plantacion = registro.get_plantacion()
            tierra = registro.get_tierra()
            
            cultivos = plantacion.get_cultivos()
            total_cultivos += len(cultivos)
            total_agua += plantacion.get_agua_disponible()
            total_superficie += tierra.get_superficie()
            
            # Contar por tipo
            for cultivo in cultivos:
                tipo = cultivo.get_tipo_cultivo()
                contadores_tipo[tipo] = contadores_tipo.get(tipo, 0) + 1
        
        print(f"Total de fincas: {total_fincas}")
        print(f"Total de cultivos: {total_cultivos}")
        print(f"Agua total disponible: {total_agua:.2f}L")
        print(f"Superficie total: {total_superficie:.2f} m²")
        
        if contadores_tipo:
            print("\nCultivos por tipo:")
            for tipo, cantidad in sorted(contadores_tipo.items()):
                print(f"  {tipo}: {cantidad}")
        
        print("=" * 70)

# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/negocio/paquete.py
# ================================================================================

"""
Paquete generico tipo-seguro para empaquetar cultivos.
"""

from typing import Generic, TypeVar, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """
    Paquete generico para cultivos cosechados.
    
    Permite empaquetar cualquier tipo de cultivo de forma type-safe.
    """


    _contador_paquetes = 0

    def __init__(self, contenido: List[T]):
        """
        Inicializa paquete.

        Args:
            contenido: Lista de items a empaquetar
        """
        Paquete._contador_paquetes += 1
        self._id_paquete = Paquete._contador_paquetes
        self._contenido = contenido.copy() if contenido else []

    def get_id_paquete(self) -> int:
        """Retorna ID del paquete."""
        return self._id_paquete

    def get_contenido(self) -> List[T]:
        """Retorna copia del contenido."""
        return self._contenido.copy()

    def get_cantidad(self) -> int:
        """Retorna cantidad de items."""
        return len(self._contenido)

    def mostrar_contenido_caja(self) -> None:
        """Muestra contenido del paquete."""
        if not self._contenido:
            print("Paquete vacio")
            return
        
        primer_item = self._contenido[0]
        tipo_nombre = type(primer_item).__name__

        print("\nContenido de la caja:")
        print(f"  Tipo: {tipo_nombre}")
        print(f"  Cantidad: {self.get_cantidad()}")
        print(f"  ID Paquete: {self._id_paquete}")

