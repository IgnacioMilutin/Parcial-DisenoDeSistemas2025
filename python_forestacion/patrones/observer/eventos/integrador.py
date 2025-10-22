"""
Archivo integrador generado automaticamente
Directorio: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/observer/eventos
Fecha: 2025-10-21 23:22:13
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/observer/eventos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: evento_plantacion.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: evento_sensor.py
# Ruta: /home/ignaciomilutin/Documentos/UM/DisenoDeSistemas2025/PARCIAL/parcial_Milutin/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ================================================================================

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


