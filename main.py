
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
    for cultivo in cultivos[:2]:  # Mostrar solo 2 para no saturar output
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