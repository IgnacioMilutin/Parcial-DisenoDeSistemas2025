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