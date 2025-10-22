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