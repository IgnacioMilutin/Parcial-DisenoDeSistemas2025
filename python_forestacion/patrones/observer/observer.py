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