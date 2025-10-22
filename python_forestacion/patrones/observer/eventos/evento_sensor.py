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
