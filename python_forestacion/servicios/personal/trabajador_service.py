from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.apto_medico import AptoMedico
    from python_forestacion.entidades.personal.herramienta import Herramienta
    from python_forestacion.entidades.personal.tarea import Tarea


class TrabajadorService:
    """Servicio para operaciones con trabajadores."""

    @staticmethod
    def asignar_apto_medico(
        trabajador: 'Trabajador',
        apto: bool,
        fecha_emision: date,
        observaciones: str = ""
    ) -> None:
        """
        Asigna apto medico a trabajador.

        Args:
            trabajador: Trabajador al que asignar apto
            apto: True si esta apto, False si no
            fecha_emision: Fecha del examen
            observaciones
        """
        from python_forestacion.entidades.personal.apto_medico import AptoMedico

        apto_medico = AptoMedico(
            apto=apto,
            fecha_emision=fecha_emision,
            observaciones=observaciones
        )

        trabajador.set_apto_medico(apto_medico)

        estado = "APTO" if apto else "NO APTO"
        print(f"[OK] {trabajador.get_nombre()} - {estado} (Emision: {fecha_emision})")

    @staticmethod
    def trabajar(
        trabajador: 'Trabajador',
        fecha: date,
        util: 'Herramienta'
    ) -> bool:
        """
        Ejecuta tareas del trabajador en una fecha.

        Args:
            trabajador: Trabajador que trabaja
            fecha: Fecha de trabajo
            util: Herramienta a usar

        Returns:
            bool: True si trabajo exitosamente, False si no tiene apto
        """
        
        apto_medico = trabajador.get_apto_medico()
        if not apto_medico or not apto_medico.esta_apto():
            print(f"[!] {trabajador.get_nombre()} NO PUEDE TRABAJAR - Sin apto medico valido")
            return False

        tareas = trabajador.get_tareas()
        tareas_fecha = [t for t in tareas if t.get_fecha_programada() == fecha]
        
        tareas_ordenadas = sorted(
            tareas_fecha,
            key=TrabajadorService._obtener_id_tarea,
            reverse=True
        )

        for tarea in tareas_ordenadas:
            descripcion = tarea.get_descripcion()
            herramienta = util.get_nombre()
            print(
                f"El trabajador {trabajador.get_nombre()} "
                f"realizo la tarea {tarea.get_id_tarea()} {descripcion} "
                f"con herramienta: {herramienta}"
            )
            tarea.set_completada(True)

        return True

    @staticmethod
    def _obtener_id_tarea(tarea: 'Tarea') -> int:
        """
        Extrae ID de tarea

        Args:
            tarea: Tarea de la que extraer ID
            
        Returns:
            int: ID de la tarea
        """
        return tarea.get_id_tarea()