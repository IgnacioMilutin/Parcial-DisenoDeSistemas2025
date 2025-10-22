"""
Paquete generico tipo-seguro para empaquetar cultivos.
"""

from typing import Generic, TypeVar, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """
    Paquete generico para cultivos cosechados.
    
    Permite empaquetar cualquier tipo de cultivo de forma type-safe.
    """


    _contador_paquetes = 0

    def __init__(self, contenido: List[T]):
        """
        Inicializa paquete.

        Args:
            contenido: Lista de items a empaquetar
        """
        Paquete._contador_paquetes += 1
        self._id_paquete = Paquete._contador_paquetes
        self._contenido = contenido.copy() if contenido else []

    def get_id_paquete(self) -> int:
        """Retorna ID del paquete."""
        return self._id_paquete

    def get_contenido(self) -> List[T]:
        """Retorna copia del contenido."""
        return self._contenido.copy()

    def get_cantidad(self) -> int:
        """Retorna cantidad de items."""
        return len(self._contenido)

    def mostrar_contenido_caja(self) -> None:
        """Muestra contenido del paquete."""
        if not self._contenido:
            print("Paquete vacio")
            return
        
        primer_item = self._contenido[0]
        tipo_nombre = type(primer_item).__name__

        print("\nContenido de la caja:")
        print(f"  Tipo: {tipo_nombre}")
        print(f"  Cantidad: {self.get_cantidad()}")
        print(f"  ID Paquete: {self._id_paquete}")