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