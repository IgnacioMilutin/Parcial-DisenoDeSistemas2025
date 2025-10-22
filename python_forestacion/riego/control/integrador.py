"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/control
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/control/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: control_riego_task.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/control/control_riego_task.py
# ================================================================================

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

