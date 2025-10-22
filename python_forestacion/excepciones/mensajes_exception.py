"""
Mensajes centralizados de excepciones.
"""


class MensajesException:
    """Clase con mensajes estáticos para excepciones."""

    @staticmethod
    def superficie_insuficiente_user(
        tipoCultivo: str,
        requerida: float,
        disponible: float
    ) -> str:
        """Mensaje de usuario para superficie insuficiente."""
        return (
            f"No hay suficiente espacio para plantar {tipoCultivo}. "
            f"Se requieren {requerida:.2f} m², "
            f"pero solo hay {disponible:.2f} m² disponibles."
        )

    @staticmethod
    def superficie_insuficiente_tech(
        tipoCultivo: str,
        requerida: float,
        disponible: float
    ) -> str:
        """Mensaje técnico para superficie insuficiente."""
        return (
            f"SuperficieInsuficiente: "
            f"especie={tipoCultivo}, "
            f"requerida={requerida}, "
            f"disponible={disponible}"
        )

    @staticmethod
    def agua_agotada_user(
        operacion: str,
        requerida: float,
        disponible: float
    ) -> str:
        """Mensaje de usuario para agua agotada."""
        return (
            f"El agua se ha agotado para realizar {operacion}. "
            f"Se requieren {requerida:.2f}L, "
            f"pero solo hay {disponible:.2f}L disponibles."
        )

    @staticmethod
    def agua_agotada_tech(
        operacion: str,
        requerida: float,
        disponible: float
    ) -> str:
        """Mensaje técnico para agua agotada."""
        return (
            f"AguaAgotada: "
            f"operacion={operacion}, "
            f"requerida={requerida}, "
            f"disponible={disponible}"
        )

    @staticmethod
    def persistencia_user(tipo_operacion: str, nombre_archivo: str) -> str:
        """Mensaje de usuario para error de persistencia."""
        return (
            f"Error durante {tipo_operacion} del archivo '{nombre_archivo}'. "
            f"Verifique permisos y espacio en disco."
        )

    @staticmethod
    def persistencia_tech(
        tipo_operacion: str,
        nombre_archivo: str,
        causa: str = ""
    ) -> str:
        """Mensaje técnico para error de persistencia."""
        causa_str = f"\nCausa original: {causa}" if causa else ""
        return (
            f"PersistenciaException: "
            f"operacion={tipo_operacion}, "
            f"archivo={nombre_archivo}{causa_str}"
        )