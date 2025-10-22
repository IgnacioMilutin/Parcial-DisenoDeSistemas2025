from typing import List
from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')

class Observable(Generic[T], ABC):

    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Suscribe un observador a los eventos.

        Args:
            observador: Observador a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Desuscribe un observador de los eventos.

        Args:
            observador: Observador a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    # NOTIFICACION DE EVENTOS

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a los observadores que hay un nuevo evento.

        Args:
            evento: Datos del evento a notificar
        """
        for observador in self._observadores:
            observador.actualizar(evento)

    def get_cantidad_observadores(self) -> int:
        """Retorna cantidad de observadores suscritos."""
        return len(self._observadores)