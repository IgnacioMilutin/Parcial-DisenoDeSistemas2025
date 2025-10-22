class Herramienta:

    def __init__(
        self,
        id_herramienta: int,
        nombre: str,
        certificado_hys: bool = True
    ):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")

        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    # GETTERS Y SETTERS

    def get_id_herramienta(self) -> int:
        return self._id_herramienta

    def get_nombre(self) -> str:
        return self._nombre

    def tiene_certificado_hys(self) -> bool:
        return self._certificado_hys
    
    def set_nombre(self,nombre: str):
        self._nombre=nombre

    def set_certificado(self,certificado_hys: bool):
        self._certificado_hys=certificado_hys