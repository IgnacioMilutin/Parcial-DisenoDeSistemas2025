"""
Excepciones base del sistema forestal.

"""


class ForestacionException(Exception):
    """
    Excepcion base de todas las excepciones del sistema forestal.
    """

    def __init__(self, user_message: str, technical_message: str = ""):
        """
        Inicializa excepcion forestal.

        Args:
            user_message: Mensaje para usuario final
            technical_message: Mensaje tecnico para desarrolladores
        """
        self._user_message = user_message
        self._technical_message = technical_message or user_message
        super().__init__(self._user_message)

    def get_user_message(self) -> str:
        """Retorna mensaje para usuario final."""
        return self._user_message

    def get_technical_message(self) -> str:
        """Retorna mensaje tecnico."""
        return self._technical_message

    def get_full_message(self) -> str:
        """Retorna ambos mensajes combinados."""
        return f"[USER] {self._user_message}\n[TECH] {self._technical_message}"
