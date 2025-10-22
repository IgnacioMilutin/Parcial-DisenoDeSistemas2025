"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/sensores
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/sensores/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/sensores/humedad_reader_task.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/riego/sensores/temperatura_reader_task.py
# ================================================================================

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


