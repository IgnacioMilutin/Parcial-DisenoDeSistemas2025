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
