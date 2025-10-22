"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion
Fecha de generacion: 2025-10-21 23:22:13
Total de archivos integrados: 67
Total de directorios procesados: 22
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: ..
#   1. main.py
#
# DIRECTORIO: .
#   2. __init__.py
#   3. constantes.py
#
# DIRECTORIO: entidades
#   4. __init__.py
#
# DIRECTORIO: entidades/cultivos
#   5. __init__.py
#   6. arbol.py
#   7. cultivo.py
#   8. hortaliza.py
#   9. lechuga.py
#   10. olivo.py
#   11. pino.py
#   12. tipo_aceituna.py
#   13. zanahoria.py
#
# DIRECTORIO: entidades/personal
#   14. __init__.py
#   15. apto_medico.py
#   16. herramienta.py
#   17. tarea.py
#   18. trabajador.py
#
# DIRECTORIO: entidades/terrenos
#   19. __init__.py
#   20. plantacion.py
#   21. registro_forestal.py
#   22. tierra.py
#
# DIRECTORIO: excepciones
#   23. __init__.py
#   24. agua_agotada_exception.py
#   25. forestacion_exception.py
#   26. mensajes_exception.py
#   27. persistencia_exception.py
#   28. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   29. __init__.py
#
# DIRECTORIO: patrones/factory
#   30. __init__.py
#   31. cultivo_factory.py
#
# DIRECTORIO: patrones/observer
#   32. __init__.py
#   33. observable.py
#   34. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   35. __init__.py
#   36. evento_plantacion.py
#   37. evento_sensor.py
#
# DIRECTORIO: patrones/singleton
#   38. __init__.py
#
# DIRECTORIO: patrones/strategy
#   39. __init__.py
#   40. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   41. __init__.py
#   42. absorcion_constante_strategy.py
#   43. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   44. __init__.py
#
# DIRECTORIO: riego/control
#   45. __init__.py
#   46. control_riego_task.py
#
# DIRECTORIO: riego/sensores
#   47. __init__.py
#   48. humedad_reader_task.py
#   49. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   50. __init__.py
#
# DIRECTORIO: servicios/cultivos
#   51. __init__.py
#   52. arbol_service.py
#   53. cultivo_service.py
#   54. cultivo_service_registry.py
#   55. lechuga_service.py
#   56. olivo_service.py
#   57. pino_service.py
#   58. zanahoria_service.py
#
# DIRECTORIO: servicios/negocio
#   59. __init__.py
#   60. fincas_service.py
#   61. paquete.py
#
# DIRECTORIO: servicios/personal
#   62. __init__.py
#   63. trabajador_service.py
#
# DIRECTORIO: servicios/terrenos
#   64. __init__.py
#   65. plantacion_service.py
#   66. registro_forestal_service.py
#   67. tierra_service.py
#


################################################################################
# DIRECTORIO: ..
################################################################################

# ==============================================================================
# ARCHIVO 1/67: main.py
# Directorio: ..
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/main.py
# ==============================================================================


"""
Sistema de Gestion Forestal - Demostracion de Patrones de Diseño

Este archivo demuestra:
1. SINGLETON - CultivoServiceRegistry instancia unica
2. FACTORY METHOD - Creacion de cultivos
3. OBSERVER - Sistema de sensores y control de riego
4. STRATEGY - Algoritmos de absorcion de agua
5. REGISTRY - Dispatch polimorfico sin isinstance

Ejecucion: python main.py
"""

import time
from datetime import date

from python_forestacion.constantes import SEPARADOR_LARGO, SEPARADOR_CORTO, THREAD_JOIN_TIMEOUT
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.pino import Pino


def main():
    """Ejecuta demostracion completa del sistema."""

    print(SEPARADOR_LARGO)
    print(" " * 15 + "SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print(SEPARADOR_LARGO)

    # PASO 1: SINGLETON - Verificar instancia unica del Registry

    print("\n" + SEPARADOR_CORTO)
    print("  PATRON SINGLETON: Inicializando servicios")
    print(SEPARADOR_CORTO)

    from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

    registry1 = CultivoServiceRegistry.get_instance()
    registry2 = CultivoServiceRegistry.get_instance()

    if registry1 is registry2:
        print("[OK] Todos los servicios comparten la misma instancia del Registry")
    else:
        print("[ERROR] SINGLETON fallido - multiples instancias")

    # PASO 2: Crear terreno con plantacion

    print("\n1. Creando tierra con plantacion...")

    tierra_service = TierraService()
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )

    plantacion = terreno.get_finca()
    print(f"   Terreno: {terreno.get_domicilio()} ({terreno.get_superficie()} m²)")
    print(f"   Plantacion: {plantacion.get_nombre()}")

    
    # PASO 3: FACTORY METHOD - Plantar cultivos

    print("\n2. FACTORY METHOD: Plantando cultivos (sin conocer tipos concretos)...")

    plantacion_service = PlantacionService()
    
    plantacion_service.plantar(plantacion, "Pino", 5)
    plantacion_service.plantar(plantacion, "Olivo", 5)
    plantacion_service.plantar(plantacion, "Lechuga", 5)
    plantacion_service.plantar(plantacion, "Zanahoria", 5)

    print(f"   Total cultivos: {len(plantacion.get_cultivos())}")
    print(f"   Superficie disponible: {plantacion.get_superficie_disponible():.2f} m²")
    
    
    print("\n   Intentando plantar más de lo que cabe...")
    try:
        plantacion_service.plantar(plantacion, "Pino", 10000)
    except Exception as e:
        print(f"   [EXCEPCION CAPTURADA] {type(e).__name__}")
        if hasattr(e, 'get_user_message'):
            print(f"   {e.get_user_message()})Olivo", 5)
    plantacion_service.plantar(plantacion, "Lechuga", 5)
    plantacion_service.plantar(plantacion, "Zanahoria", 5)

    print(f"   Total cultivos: {len(plantacion.get_cultivos())}")
    print(f"   Superficie disponible: {plantacion.get_superficie_disponible():.2f} m²")

    # PASO 4: STRATEGY - Riego con absorcion diferenciada

    print("\n3. STRATEGY: Regando plantacion (cada cultivo absorbe segun estrategia)...")
    
    print("\n   Alturas ANTES del riego:")
    cultivos = plantacion.get_cultivos()
    for cultivo in cultivos[:4]:
        if hasattr(cultivo, 'get_altura'):
            print(f"     {cultivo.get_tipo_cultivo()} ID {cultivo.get_id_cultivo()}: {cultivo.get_altura():.2f}m")

    
    plantacion_service.regar(plantacion)
    
    print("\n   Alturas DESPUES del riego (arboles crecieron):")
    for cultivo in cultivos[:4]:
        if hasattr(cultivo, 'get_altura'):
            print(f"     {cultivo.get_tipo_cultivo()} ID {cultivo.get_id_cultivo()}: {cultivo.get_altura():.2f}m")
    
    
    print("\n   Agotando el agua para demostrar excepcion...")
    plantacion.set_agua_disponible(5.0)
    try:
        plantacion_service.regar(plantacion)
    except Exception as e:
        print(f"   [EXCEPCION CAPTURADA] {type(e).__name__}")
        if hasattr(e, 'get_user_message'):
            print(f"   {e.get_user_message()}")
    
    
    plantacion.set_agua_disponible(500.0)

    # PASO 5: REGISTRY - Mostrar datos de cultivos (dispatch polimorfico)

    print("\n4. REGISTRY: Mostrando datos de cultivos (dispatch automatico por tipo)...")

    cultivos = plantacion.get_cultivos()
    print("\n   Datos de algunos cultivos:")
    for cultivo in cultivos[:2]:
        print()
        registry1.mostrar_datos(cultivo)

    # PASO 6: Crear registro forestal y persistir

    print("\n5. Persistencia: Guardando registro forestal en disco...")

    registro = RegistroForestal(
        id_padron=1,
        tierra=terreno,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )

    registro_service = RegistroForestalService()
    registro_service.persistir(registro)

    # PASO 7: Gestion de personal

    print("\n6. Gestion de Personal: Asignando trabajadores...")

    tareas = [
        Tarea(1, date.today(), "Desmalezar"),
        Tarea(2, date.today(), "Abonar"),
        Tarea(3, date.today(), "Marcar surcos")
    ]

    trabajador = Trabajador(
        dni=43888734,
        nombre="Juan Perez",
        tareas=tareas
    )

    trabajador_service = TrabajadorService()
    trabajador_service.asignar_apto_medico(
        trabajador=trabajador,
        apto=True,
        fecha_emision=date.today(),
        observaciones="Estado de salud: excelente"
    )

    herramienta = Herramienta(
        id_herramienta=1,
        nombre="Pala",
        certificado_hys=True
    )

    print("\n   Ejecutando tareas del trabajador...")
    resultado = trabajador_service.trabajar(
        trabajador=trabajador,
        fecha=date.today(),
        util=herramienta
    )

    plantacion.agregar_trabajador(trabajador)

    # PASO 8: OBSERVER + Threading - Sistema de riego automatizado

    print("\n7. OBSERVER: Iniciando sistema de riego automatizado con sensores...")
    print("   (Los sensores notificaran al controlador automaticamente)")
    print("   Eventos: EventoSensor con tipo, valor, timestamp")

    tarea_temp = TemperaturaReaderTask()
    tarea_hum = HumedadReaderTask()

    tarea_control = ControlRiegoTask(
        tarea_temp,
        tarea_hum,
        plantacion,
        plantacion_service
    )

    tarea_temp.start()
    tarea_hum.start()
    tarea_control.start()

    print("   Sistema funcionando... (esperando 15 segundos)")
    print("   El controlador recibe eventos de sensores y decide si regar")
    time.sleep(15)

    print("\n   Deteniendo sensores...")
    tarea_temp.detener()
    tarea_hum.detener()
    tarea_control.detener()

    tarea_temp.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_hum.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)

    # PASO 9: Servicios de negocio - Multiples fincas y operaciones

    print("\n8. Servicios de Negocio: Gestionando portafolio de fincas...")

    fincas_service = FincasService()
    fincas_service.add_finca(registro)

    print(f"   Total fincas en portafolio: {fincas_service.get_cantidad_fincas()}")

    print("\n   Fumigando Finca 1...")
    fincas_service.fumigar(1, "insecto organico")

    fincas_service.obtener_reporte_general()

    print("\n   Cosechando cultivos por tipo...")
    caja_lechugas = fincas_service.cosechar_y_empaquetar(Lechuga)
    caja_pinos = fincas_service.cosechar_y_empaquetar(Pino)

    print("\n   Reporte después de cosecha:")
    fincas_service.obtener_reporte_general()

    # PASO 10: Recuperar registro persistido

    print("\n9. Recuperando registro persistido desde disco...")

    registro_leido = RegistroForestalService.leer_registro("Juan Perez")
    registro_service.mostrar_datos(registro_leido)

    # RESUMEN FINAL

    print("\n" + SEPARADOR_LARGO)
    print(" " * 20 + "EJEMPLO COMPLETADO EXITOSAMENTE")
    print(SEPARADOR_LARGO)
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorcion de agua")
    print("  [OK] REGISTRY    - Dispatch polimorfico sin isinstance")
    print("  [OK] THREADING   - Sistema automatizado con graceful shutdown")
    print(SEPARADOR_LARGO)


if __name__ == "__main__":
    main()




################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 2/67: __init__.py
# Directorio: .
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 3/67: constantes.py
# Directorio: .
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/constantes.py
# ==============================================================================

# python_forestacion/constantes.py

# ============================================================================
# AGUA Y RIEGO
# ============================================================================

AGUA_MINIMA = 10  # Agua minima para un riego (litros)
AGUA_INICIAL_PLANTACION = 500  # Agua inicial de cada plantacion (litros)

# Absorcion estacional de arboles
ABSORCION_SEASONAL_VERANO = 5  # Litros en verano
ABSORCION_SEASONAL_INVIERNO = 2  # Litros en invierno
MES_INICIO_VERANO = 3  # Marzo
MES_FIN_VERANO = 8  # Agosto

# Absorcion constante de hortalizas
ABSORCION_LECHUGA = 1  # Litros por riego
ABSORCION_ZANAHORIA = 2  # Litros por riego

# ============================================================================
# CULTIVOS - PINO
# ============================================================================

SUPERFICIE_PINO = 2.0  # Metros cuadrados por arbol
AGUA_INICIAL_PINO = 2  # Litros iniciales
CRECIMIENTO_PINO = 0.10  # Metros por riego

# ============================================================================
# CULTIVOS - OLIVO
# ============================================================================

SUPERFICIE_OLIVO = 3.0  # Metros cuadrados por arbol
AGUA_INICIAL_OLIVO = 5  # Litros iniciales
CRECIMIENTO_OLIVO = 0.01  # Metros por riego
ALTURA_INICIAL_OLIVO = 0.5

# ============================================================================
# CULTIVOS - LECHUGA
# ============================================================================

SUPERFICIE_LECHUGA = 0.10  # Metros cuadrados por planta
AGUA_INICIAL_LECHUGA = 1  # Litros iniciales
LECHUGA_EN_INVERNADERO = True  # Siempre en invernadero

# ============================================================================
# CULTIVOS - ZANAHORIA
# ============================================================================

SUPERFICIE_ZANAHORIA = 0.15  # Metros cuadrados por planta
AGUA_INICIAL_ZANAHORIA = 0  # Sin agua inicial
ZANAHORIA_EN_INVERNADERO = False  # Cultivo a campo abierto

# ============================================================================
# ARBOLES - GENERAL
# ============================================================================

ALTURA_INICIAL_ARBOL = 1.0  # Metros (altura inicial de arboles)

# ============================================================================
# SENSORES Y RIEGO AUTOMATIZADO
# ============================================================================

# Sensor de temperatura
INTERVALO_SENSOR_TEMPERATURA = 2.0  # Segundos entre lecturas
SENSOR_TEMP_MIN = -25  # Grados Celsius
SENSOR_TEMP_MAX = 50  # Grados Celsius

# Sensor de humedad
INTERVALO_SENSOR_HUMEDAD = 3.0  # Segundos entre lecturas
SENSOR_HUMEDAD_MIN = 0  # Porcentaje
SENSOR_HUMEDAD_MAX = 100  # Porcentaje

# Control de riego
TEMP_MIN_RIEGO = 8  # Temperatura minima para regar (C)
TEMP_MAX_RIEGO = 15  # Temperatura maxima para regar (C)
HUMEDAD_MAX_RIEGO = 50  # Humedad maxima para regar (%)
INTERVALO_CONTROL_RIEGO = 2.5  # Segundos entre evaluaciones

# ============================================================================
# THREADING
# ============================================================================

THREAD_JOIN_TIMEOUT = 2.0  # Segundos de timeout para join

# ============================================================================
# PERSISTENCIA
# ============================================================================

DIRECTORIO_DATA = "data"  # Directorio de datos persistidos
EXTENSION_DATA = ".dat"  # Extension de archivos de datos

# ============================================================================
# MENSAJES DE SISTEMA
# ============================================================================

SEPARADOR_LARGO = "=" * 70
SEPARADOR_CORTO = "-" * 70
SEPARADOR_TITULO = "_" * 28


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 4/67: __init__.py
# Directorio: entidades
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 5/67: __init__.py
# Directorio: entidades/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 6/67: arbol.py
# Directorio: entidades/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from typing import Optional


class Arbol(Cultivo):
    def __init__(
        self,
        agua: int,
        superficie: float,
        altura: float = 1.0,
        id_cultivo: Optional[int] = None
    ):
        
        super().__init__(agua, superficie, id_cultivo)
        if altura <= 0:
            raise ValueError("La altura debe ser positiva")
        self._altura = altura

    def get_altura(self) -> float:
        return self._altura

    def set_altura(self, altura: float) -> None:
        if altura <= 0:
            raise ValueError("La altura debe ser positiva")
        self._altura = altura

    def crecer(self, cantidad: float) -> None:
        self.set_altura(self._altura + cantidad)

# ==============================================================================
# ARCHIVO 7/67: cultivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import Optional


class Cultivo(ABC):

    #CONSTRUCTOR
    def __init__(
        self,
        agua:int,
        superficie:float,
        id_cultivo: Optional[int] = None
        ):

        if agua < 0:
            raise ValueError('El agua no puede ser negativa')
        if superficie <= 0:
            raise ValueError('La superficie debe ser mayor o igual a cero')
        
        self._agua = agua
        self._superficie = superficie
        self._id_cultivo = id_cultivo

    #GETTERS
    def get_agua(self)->int:
        return self._agua
    
    def get_superficie(self)->float:
        return self._superficie
    
    def get_id_cultivo(self) -> Optional[int]:
        return self._id_cultivo
    
    #SETTERS
    def set_agua(self, agua: float) -> None:
        
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua = agua

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie

    def set_id_cultivo(self, id_cultivo: int) -> None:
        self._id_cultivo = id_cultivo

   #METODOS

    @abstractmethod
    def get_tipo_cultivo(self) -> str:
        pass

# ==============================================================================
# ARCHIVO 8/67: hortaliza.py
# Directorio: entidades/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from typing import Optional


class Hortaliza(Cultivo):
    def __init__(
        self,
        agua: int,
        superficie: float,
        invernadero: bool,
        id_cultivo: Optional[int] = None
    ):
        super().__init__(agua, superficie, id_cultivo)
        self._invernadero = invernadero

    def get_invernadero(self) -> bool:
        return self._invernadero

    def set_invernadero(self, invernadero: bool) -> None:
        self._invernadero = invernadero

# ==============================================================================
# ARCHIVO 9/67: lechuga.py
# Directorio: entidades/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA, LECHUGA_EN_INVERNADERO
from typing import Optional


class Lechuga(Hortaliza):
    def __init__(self, variedad: str, id_cultivo: Optional[int] = None):
        
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=LECHUGA_EN_INVERNADERO,
            id_cultivo=id_cultivo
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

    def get_tipo_cultivo(self) -> str:
        return "Lechuga"

# ==============================================================================
# ARCHIVO 10/67: olivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO, ALTURA_INICIAL_OLIVO
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from typing import Optional

class Olivo(Arbol):
    def __init__(
        self,
        tipo_aceituna: str,
        id_cultivo: Optional[int] = None
    ):
        
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=ALTURA_INICIAL_OLIVO,
            id_cultivo=id_cultivo
        )
        self._fruto = tipo_aceituna

    def get_tipo_aceituna(self) -> str:
        return self._fruto

    def set_tipo_aceituna(self, tipo_aceituna: str) -> None:
        self._fruto = tipo_aceituna

    def get_tipo_cultivo(self) -> str:
        return "Olivo"

# ==============================================================================
# ARCHIVO 11/67: pino.py
# Directorio: entidades/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO, ALTURA_INICIAL_ARBOL
from typing import Optional


class Pino(Arbol):
    def __init__(
        self,
        variedad: str,
        id_cultivo: Optional[int] = None
    ):
        
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=ALTURA_INICIAL_ARBOL,
            id_cultivo=id_cultivo
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad

    def get_tipo_cultivo(self) -> str:
        return "Pino"

# ==============================================================================
# ARCHIVO 12/67: tipo_aceituna.py
# Directorio: entidades/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

class TipoAceituna:
    NEGRA = "Negra"
    VERDE = "Verde"
    ROJA = "Roja"

# ==============================================================================
# ARCHIVO 13/67: zanahoria.py
# Directorio: entidades/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA, ZANAHORIA_EN_INVERNADERO
from typing import Optional


class Zanahoria(Hortaliza):
    def __init__(self, is_baby_carrot: bool = False, id_cultivo: Optional[int] = None):
        
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=ZANAHORIA_EN_INVERNADERO,
            id_cultivo=id_cultivo
        )
        self._is_baby_carrot = is_baby_carrot

    def is_baby_carrot(self) -> bool:
        return self._is_baby_carrot

    def set_baby_carrot(self, is_baby_carrot: bool) -> None:
        self._is_baby_carrot = is_baby_carrot

    def get_tipo_cultivo(self) -> str:
        return "Zanahoria"


################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 14/67: __init__.py
# Directorio: entidades/personal
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 15/67: apto_medico.py
# Directorio: entidades/personal
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

from datetime import date
from typing import Optional


class AptoMedico:

    def __init__(
        self,
        apto: bool,
        fecha_emision: date,
        observaciones: str = ""
    ):
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    # GETTERS Y SETTERS
 
    def esta_apto(self) -> bool:
        return self._apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_observaciones(self) -> str:
        return self._observaciones

    def set_apto(self, apto: bool) -> None:
        self._apto = apto

    def set_observaciones(self, observaciones: str) -> None:
        self._observaciones = observaciones

    def toString(self):
        return print(f"Apto: {self._apto} | Fecha: {self._fecha_emision} | Observaciones: {self._observaciones}")

# ==============================================================================
# ARCHIVO 16/67: herramienta.py
# Directorio: entidades/personal
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

class Herramienta:

    def __init__(
        self,
        id_herramienta: int,
        nombre: str,
        certificado_hys: bool = True
    ):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")

        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    # GETTERS Y SETTERS

    def get_id_herramienta(self) -> int:
        return self._id_herramienta

    def get_nombre(self) -> str:
        return self._nombre

    def tiene_certificado_hys(self) -> bool:
        return self._certificado_hys
    
    def set_nombre(self,nombre: str):
        self._nombre=nombre

    def set_certificado(self,certificado_hys: bool):
        self._certificado_hys=certificado_hys

# ==============================================================================
# ARCHIVO 17/67: tarea.py
# Directorio: entidades/personal
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

from datetime import date


class Tarea:

    def __init__(self,id_tarea: int,fecha: date,descripcion: str,completada: bool = False):
        self._id_tarea = id_tarea
        self._fecha = fecha
        self._descripcion = descripcion
        self._completada = completada

    # GETTERS Y SETTERS

    def get_id_tarea(self) -> int:
        return self._id_tarea

    def get_fecha_programada(self) -> date:
        return self._fecha

    def get_descripcion(self) -> str:
        return self._descripcion

    def esta_completada(self) -> bool:
        return self._completada

    def set_completada(self, completada: bool) -> None:
        self._completada = completada

    def toString(self):
        return print(f"ID TAREA: {self._id_tarea} \n Fecha: {self._fecha} \n Descripción: {self._descripcion} \n Esta completada?: {self._completada}")
    

# ==============================================================================
# ARCHIVO 18/67: trabajador.py
# Directorio: entidades/personal
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

from typing import List, Optional, TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.apto_medico import AptoMedico
    from python_forestacion.entidades.personal.tarea import Tarea


class Trabajador:
    
    def __init__(
        self,
        dni: int,
        nombre: str,
        tareas: Optional[List['Tarea']] = None,
        apto_medico: Optional['AptoMedico'] = None
    ):
        
        if dni <= 0:
            raise ValueError("DNI debe ser numero positivo")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")

        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas.copy() if tareas else []
        self._apto_medico = apto_medico

    # GETTERS Y SETTERS

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_tareas(self) -> List['Tarea']:
        return self._tareas.copy()

    def get_apto_medico(self) -> Optional['AptoMedico']:
        return self._apto_medico
    
    def set_nombre(self, nombre: str) -> None:
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nombre

    def set_tareas(self, tareas: List['Tarea']) -> None:
        self._tareas = tareas.copy() if tareas else []

    def set_apto_medico(self, apto_medico: 'AptoMedico') -> None:
        self._apto_medico = apto_medico

        
    # OPERACIONES

    def agregar_tarea(self, tarea: 'Tarea') -> None:
        self._tareas.append(tarea)

    def eliminar_tarea(self, tarea: 'Tarea') -> None:
        if tarea in self._tareas:
            self._tareas.remove(tarea)


################################################################################
# DIRECTORIO: entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 19/67: __init__.py
# Directorio: entidades/terrenos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 20/67: plantacion.py
# Directorio: entidades/terrenos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

from typing import List, Optional, TYPE_CHECKING
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:

    def __init__(
        self,
        nombre: str,
        superficie: float,
        agua: float = AGUA_INICIAL_PLANTACION
    ):
       
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")

        self._nombre = nombre
        self._superficie_maxima = superficie
        self._agua_disponible = agua
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []

    # GETTERS Y SETTERS

    def get_nombre(self) -> str:
        return self._nombre

    def get_superficie_maxima(self) -> float:
        return self._superficie_maxima

    def get_agua_disponible(self) -> float:
        return self._agua_disponible

    def get_cultivos(self) -> List['Cultivo']:
        return self._cultivos.copy()
    def get_cultivos_interno(self) -> List['Cultivo']:
        return self._cultivos

    def get_trabajadores(self) -> List['Trabajador']:
        return self._trabajadores.copy()
    def get_trabajadores_interno(self) -> List['Trabajador']:
        return self._trabajadores

    def get_superficie_ocupada(self) -> float:
        return sum(cultivo.get_superficie() for cultivo in self._cultivos)

    def get_superficie_disponible(self) -> float:
        return self._superficie_maxima - self.get_superficie_ocupada()

    def set_nombre(self, nombre: str) -> None:
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nombre

    def set_agua_disponible(self, agua: float) -> None:
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua_disponible = agua

    def set_cultivos(self, cultivos: List['Cultivo']) -> None:
        self._cultivos = cultivos.copy() if cultivos else []

    def set_trabajadores(self, trabajadores: List['Trabajador']) -> None:
        self._trabajadores = trabajadores.copy() if trabajadores else []

    # OPERACIONES 

    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        self._cultivos.append(cultivo)

    def eliminar_cultivo(self, cultivo: 'Cultivo') -> None:
        if cultivo in self._cultivos:
            self._cultivos.remove(cultivo)

    def agregar_trabajador(self, trabajador: 'Trabajador') -> None:
        self._trabajadores.append(trabajador)

    def eliminar_trabajador(self, trabajador: 'Trabajador') -> None:
        if trabajador in self._trabajadores:
            self._trabajadores.remove(trabajador)


# ==============================================================================
# ARCHIVO 21/67: registro_forestal.py
# Directorio: entidades/terrenos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:

    def __init__(
        self,
        id_padron: int,
        tierra: 'Tierra',
        plantacion: 'Plantacion',
        propietario: str,
        avaluo: float
    ):
        if not tierra or not plantacion:
            raise ValueError("Tierra y plantacion son obligatorias")
        if not propietario or not propietario.strip():
            raise ValueError("El propietario no puede estar vacio")
        if avaluo < 0:
            raise ValueError("El avaluo no puede ser negativo")

        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    # GETTERS Y SETTERS

    def get_id_padron(self) -> int:
        return self._id_padron

    def get_tierra(self) -> 'Tierra':
        return self._tierra

    def get_plantacion(self) -> 'Plantacion':
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo

    def set_propietario(self, propietario: str) -> None:  
        if not propietario or not propietario.strip():
            raise ValueError("El propietario no puede estar vacio")
        self._propietario = propietario

    def set_avaluo(self, avaluo: float) -> None:
        if avaluo < 0:
            raise ValueError("El avaluo no puede ser negativo")
        self._avaluo = avaluo

# ==============================================================================
# ARCHIVO 22/67: tierra.py
# Directorio: entidades/terrenos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:

    def __init__(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        finca: Optional['Plantacion'] = None
    ):
        
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        if not isinstance(id_padron_catastral, int):
            raise ValueError("El padron debe ser numero entero")
        if not domicilio or not domicilio.strip():
            raise ValueError("El domicilio no puede estar vacio")

        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca = finca

    # GETTERS Y SETTERS

    def get_id_padron_catastral(self) -> int:
        return self._id_padron_catastral

    def get_superficie(self) -> float:
        return self._superficie

    def get_domicilio(self) -> str:
        return self._domicilio

    def get_finca(self) -> Optional['Plantacion']:
        return self._finca

    def set_superficie(self, superficie: float) -> None: 
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie

    def set_domicilio(self, domicilio: str) -> None:
        if not domicilio or not domicilio.strip():
            raise ValueError("El domicilio no puede estar vacio")
        self._domicilio = domicilio

    def set_finca(self, finca: 'Plantacion') -> None:
        self._finca = finca



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 23/67: __init__.py
# Directorio: excepciones
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/67: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================



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



# ==============================================================================
# ARCHIVO 25/67: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 26/67: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones/mensajes_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 27/67: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 28/67: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================



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


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 29/67: __init__.py
# Directorio: patrones
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 30/67: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/67: cultivo_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 32/67: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 33/67: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/observer/observable.py
# ==============================================================================

from typing import List
from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')

class Observable(Generic[T], ABC):

    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Suscribe un observador a los eventos.

        Args:
            observador: Observador a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Desuscribe un observador de los eventos.

        Args:
            observador: Observador a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    # NOTIFICACION DE EVENTOS

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a los observadores que hay un nuevo evento.

        Args:
            evento: Datos del evento a notificar
        """
        for observador in self._observadores:
            observador.actualizar(evento)

    def get_cantidad_observadores(self) -> int:
        """Retorna cantidad de observadores suscritos."""
        return len(self._observadores)

# ==============================================================================
# ARCHIVO 34/67: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/observer/observer.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Observer(Generic[T], ABC):

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Llamado cuando hay un nuevo evento.

        Args:
            evento: Datos del evento (tipo T)
        """
        pass


################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 35/67: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/observer/eventos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/67: evento_plantacion.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ==============================================================================

from datetime import datetime
from typing import Optional
from dataclasses import dataclass


@dataclass
class EventoPlantacion:
    """
    Evento relacionado con operaciones de plantación.
    """
    
    tipo_evento: str 
    descripcion: str 
    timestamp: datetime 
    agua_disponible: Optional[float] = None  
    cantidad_cultivos: Optional[int] = None 
    
    def __str__(self) -> str:
        """Representación en string del evento."""
        msg = (
            f"[{self.timestamp.strftime('%H:%M:%S')}] "
            f"{self.tipo_evento}: {self.descripcion}"
        )
        if self.agua_disponible is not None:
            msg += f" (Agua: {self.agua_disponible:.1f}L)"
        if self.cantidad_cultivos is not None:
            msg += f" (Cultivos: {self.cantidad_cultivos})"
        return msg

# ==============================================================================
# ARCHIVO 37/67: evento_sensor.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ==============================================================================

"""
Eventos generados por sensores.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class EventoSensor:
    """
    Evento generado por un sensor.
    """
    
    tipo_sensor: str 
    valor: float
    timestamp: datetime
    unidad: str
    
    def __str__(self) -> str:
        """Representación en string del evento."""
        return (
            f"[{self.timestamp.strftime('%H:%M:%S')}] "
            f"{self.tipo_sensor}: {self.valor:.1f}{self.unidad}"
        )



################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 38/67: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/singleton/__init__.py
# ==============================================================================

"""Patron Singleton - garantiza instancia unica."""

"""Aplicado en cultivo_service_registry.py"""


################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 39/67: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 40/67: absorcion_agua_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

"""
PATRON: STRATEGY
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """
    Interfaz para estrategias de absorcion de agua.
    """

    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula cantidad de agua a absorber.

        Args:
            fecha: Fecha de calculo (para determinar estacion)
            temperatura: Temperatura ambiental en Celsius
            humedad: Humedad relativa en porcentaje
            cultivo: Cultivo que absorbe agua

        Returns:
            int: Litros de agua a absorber
        """
        pass


################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 41/67: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 42/67: absorcion_constante_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================




from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, fecha, temperatura, humedad, cultivo):
        return self._cantidad 

# ==============================================================================
# ARCHIVO 43/67: absorcion_seasonal_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================


from python_forestacion.constantes import ABSORCION_SEASONAL_INVIERNO, ABSORCION_SEASONAL_VERANO, MES_FIN_VERANO, MES_INICIO_VERANO
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    def calcular_absorcion(self, fecha, temperatura, humedad, cultivo):
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO 
        else:
            return ABSORCION_SEASONAL_INVIERNO


################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 44/67: __init__.py
# Directorio: riego
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego/control
################################################################################

# ==============================================================================
# ARCHIVO 45/67: __init__.py
# Directorio: riego/control
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/control/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 46/67: control_riego_task.py
# Directorio: riego/control
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

from typing import TYPE_CHECKING
import threading
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO,
    AGUA_MINIMA
)

if TYPE_CHECKING:
    from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
    from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService


class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Controlador de riego automatizado.
    
    Observa sensores de temperatura y humedad.
    Cuando condiciones son ideales, riega automáticamente.
    """

    def __init__(
        self,
        sensor_temperatura: 'TemperaturaReaderTask',
        sensor_humedad: 'HumedadReaderTask',
        plantacion: 'Plantacion',
        plantacion_service: 'PlantacionService'
    ):
        """
        Inicializa controlador de riego.

        Args:
            sensor_temperatura: Observable de temperatura
            sensor_humedad: Observable de humedad
            plantacion: Plantacion a regar
            plantacion_service: Servicio para operaciones
        """
        threading.Thread.__init__(self, daemon=True)
        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service

        self._detenido = threading.Event()
        self._ultima_temperatura = 0.0
        self._ultima_humedad = 0.0
        self._lock = threading.Lock()

        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """
        METODO OBSERVER - Llamado cuando sensor notifica.
        
        Args:
            evento: Valor del sensor (temperatura o humedad)
            
        Nota: No sabemos si es temperatura o humedad.
              Se actualiza el ultimo valor recibido.
              El controlador usa AMBOS valores en su logica.
        """
        with self._lock:
            if evento.tipo_sensor == "temperatura":
                self._ultima_temperatura = evento.valor
            elif evento.tipo_sensor == "humedad":
                self._ultima_humedad = evento.valor

    def run(self) -> None:
        """
        Corre el controlador (llamado cuando .start()).
        """
        print(
            f"[CONTROL RIEGO] Iniciado - "
            f"Temp ideal: {TEMP_MIN_RIEGO}-{TEMP_MAX_RIEGO}°C, "
            f"Humedad ideal: <{HUMEDAD_MAX_RIEGO}%"
        )

        while not self._detenido.is_set():
            try:
                with self._lock:
                    temperatura = self._ultima_temperatura
                    humedad = self._ultima_humedad

                agua_disponible = self._plantacion.get_agua_disponible()

                condicion_temp = TEMP_MIN_RIEGO <= temperatura <= TEMP_MAX_RIEGO
                condicion_humedad = humedad < HUMEDAD_MAX_RIEGO
                condicion_agua = agua_disponible >= AGUA_MINIMA

                if condicion_temp and condicion_humedad and condicion_agua:
                    print(
                        f"[CONTROL] Condiciones ideales: "
                        f"T={temperatura:.1f}°C, H={humedad:.1f}%, "
                        f"Agua={agua_disponible:.1f}L → RIEGO"
                    )
                    self._plantacion_service.regar(self._plantacion)
                else:
                    if not condicion_agua:
                        raise AguaAgotadaException(AGUA_MINIMA,agua_disponible,'riego')
                        
                    elif not condicion_temp:
                        print(
                            f"[CONTROL] Temp fuera de rango: {temperatura:.1f}°C "
                            f"(ideal: {TEMP_MIN_RIEGO}-{TEMP_MAX_RIEGO}°C)"
                        )
                    elif not condicion_humedad:
                        print(
                            f"[CONTROL] Humedad alta: {humedad:.1f}% "
                            f"(ideal: <{HUMEDAD_MAX_RIEGO}%)"
                        )

            except AguaAgotadaException as e:
                print(f"[CONTROL] {e.get_user_message()}")

            self._detenido.wait(INTERVALO_CONTROL_RIEGO)

        print("[CONTROL RIEGO] Detenido")

    def detener(self) -> None:
        """Detiene el controlador de forma segura."""
        self._detenido.set()


################################################################################
# DIRECTORIO: riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 47/67: __init__.py
# Directorio: riego/sensores
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/sensores/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 48/67: humedad_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

import threading
import random
from datetime import datetime
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

class HumedadReaderTask(threading.Thread, Observable[float]):
    """
    Sensor de humedad que corre en background.
    """

    def __init__(self):
        """Inicializa thread sensor."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)

        self._detenido = threading.Event()
        self._ultima_humedad = 0.0

    def run(self) -> None:
        """
        Corre el sensor (llamado cuando .start()).
        """
        from python_forestacion.constantes import (
            INTERVALO_SENSOR_HUMEDAD,
            SENSOR_HUMEDAD_MIN,
            SENSOR_HUMEDAD_MAX
        )

        print(f"[SENSOR HUMEDAD] Iniciado - Leyendo cada {INTERVALO_SENSOR_HUMEDAD}s")

        while not self._detenido.is_set():
            self._ultima_humedad = random.uniform(SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX)

            evento = EventoSensor(
                tipo_sensor="humedad",
                valor=self._ultima_humedad,
                timestamp=datetime.now(),
                unidad="%"
            )

            self.notificar_observadores(evento)

            self._detenido.wait(INTERVALO_SENSOR_HUMEDAD)

        print("[SENSOR HUMEDAD] Detenido")

    def detener(self) -> None:
        """Detiene el sensor de forma segura."""
        self._detenido.set()

    def get_ultima_humedad(self) -> float:
        """Retorna ultima lectura."""
        return self._ultima_humedad

# ==============================================================================
# ARCHIVO 49/67: temperatura_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

"""
Sensor de temperatura que funciona en thread.
"""

import threading
from datetime import datetime
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    SENSOR_TEMP_MIN,
    SENSOR_TEMP_MAX
)


class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Sensor de temperatura
    """

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)

        self._detenido = threading.Event()
        self._ultima_temperatura = 0.0

    def run(self) -> None:
        """
        Corre el sensor (llamado cuando .start()).
        """
        print(f"[SENSOR TEMP] Iniciado - Leyendo cada {INTERVALO_SENSOR_TEMPERATURA}s")

        while not self._detenido.is_set():
            self._ultima_temperatura = random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX)

            evento = EventoSensor(
                tipo_sensor="temperatura",
                valor=self._ultima_temperatura,
                timestamp=datetime.now(),
                unidad="C"
            )

            self.notificar_observadores(evento)

            self._detenido.wait(INTERVALO_SENSOR_TEMPERATURA)

        print("[SENSOR TEMP] Detenido")

    def detener(self) -> None:
        """Detiene el sensor de forma segura."""
        self._detenido.set()

    def get_ultima_temperatura(self) -> float:
        """Retorna ultima lectura."""
        return self._ultima_temperatura



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 50/67: __init__.py
# Directorio: servicios
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 51/67: __init__.py
# Directorio: servicios/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 52/67: arbol_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 53/67: cultivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 54/67: cultivo_service_registry.py
# Directorio: servicios/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 55/67: lechuga_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 56/67: olivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 57/67: pino_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 58/67: zanahoria_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 59/67: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/negocio/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 60/67: fincas_service.py
# Directorio: servicios/negocio
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/negocio/fincas_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 61/67: paquete.py
# Directorio: servicios/negocio
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/negocio/paquete.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 62/67: __init__.py
# Directorio: servicios/personal
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 63/67: trabajador_service.py
# Directorio: servicios/personal
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.apto_medico import AptoMedico
    from python_forestacion.entidades.personal.herramienta import Herramienta
    from python_forestacion.entidades.personal.tarea import Tarea


class TrabajadorService:
    """Servicio para operaciones con trabajadores."""

    @staticmethod
    def asignar_apto_medico(
        trabajador: 'Trabajador',
        apto: bool,
        fecha_emision: date,
        observaciones: str = ""
    ) -> None:
        """
        Asigna apto medico a trabajador.

        Args:
            trabajador: Trabajador al que asignar apto
            apto: True si esta apto, False si no
            fecha_emision: Fecha del examen
            observaciones
        """
        from python_forestacion.entidades.personal.apto_medico import AptoMedico

        apto_medico = AptoMedico(
            apto=apto,
            fecha_emision=fecha_emision,
            observaciones=observaciones
        )

        trabajador.set_apto_medico(apto_medico)

        estado = "APTO" if apto else "NO APTO"
        print(f"[OK] {trabajador.get_nombre()} - {estado} (Emision: {fecha_emision})")

    @staticmethod
    def trabajar(
        trabajador: 'Trabajador',
        fecha: date,
        util: 'Herramienta'
    ) -> bool:
        """
        Ejecuta tareas del trabajador en una fecha.

        Args:
            trabajador: Trabajador que trabaja
            fecha: Fecha de trabajo
            util: Herramienta a usar

        Returns:
            bool: True si trabajo exitosamente, False si no tiene apto
        """
        
        apto_medico = trabajador.get_apto_medico()
        if not apto_medico or not apto_medico.esta_apto():
            print(f"[!] {trabajador.get_nombre()} NO PUEDE TRABAJAR - Sin apto medico valido")
            return False

        tareas = trabajador.get_tareas()
        tareas_fecha = [t for t in tareas if t.get_fecha_programada() == fecha]
        
        tareas_ordenadas = sorted(
            tareas_fecha,
            key=TrabajadorService._obtener_id_tarea,
            reverse=True
        )

        for tarea in tareas_ordenadas:
            descripcion = tarea.get_descripcion()
            herramienta = util.get_nombre()
            print(
                f"El trabajador {trabajador.get_nombre()} "
                f"realizo la tarea {tarea.get_id_tarea()} {descripcion} "
                f"con herramienta: {herramienta}"
            )
            tarea.set_completada(True)

        return True

    @staticmethod
    def _obtener_id_tarea(tarea: 'Tarea') -> int:
        """
        Extrae ID de tarea

        Args:
            tarea: Tarea de la que extraer ID
            
        Returns:
            int: ID de la tarea
        """
        return tarea.get_id_tarea()


################################################################################
# DIRECTORIO: servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 64/67: __init__.py
# Directorio: servicios/terrenos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 65/67: plantacion_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 66/67: registro_forestal_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 67/67: tierra_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

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


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 67
# Generado: 2025-10-21 23:22:13
################################################################################
