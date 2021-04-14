from maquina import Maquina


class MaquinaElectrica(Maquina):
    MIN_VOLTAJE: int = 10
    MAX_VOLTAJE: int = 400
    DEFAULT_VOLTAJE: int = MIN_VOLTAJE
    MIN_POTENCIA_ELECTRICA: float = 700.00
    MAX_POTENCIA_ELECTRICA: float = 200_000.00
    DEFAULT_POTENCIA_ELECTRICA: float = MIN_POTENCIA_ELECTRICA

    def __init__(self, marca: str, modelo: str, voltaje=None, potenciaElectrica=None):
        super().__init__(marca, modelo)
        if voltaje is None:
            self._voltaje = MaquinaElectrica.DEFAULT_VOLTAJE
        else:
            self._voltaje = voltaje

        self._potenciaElectrica: float = MaquinaElectrica.DEFAULT_POTENCIA_ELECTRICA if potenciaElectrica is None else potenciaElectrica

        if self._voltaje < MaquinaElectrica.MIN_VOLTAJE or self._voltaje > MaquinaElectrica.MAX_VOLTAJE:
            raise Exception(f"Error de voltaje: {voltaje} v.  Mínimo {MaquinaElectrica.MIN_VOLTAJE} v. y máximo {MaquinaElectrica.MAX_VOLTAJE} v")

        if self._potenciaElectrica < MaquinaElectrica.MIN_POTENCIA_ELECTRICA or self._potenciaElectrica > MaquinaElectrica.MAX_POTENCIA_ELECTRICA:
            raise Exception(f"Error de potencia eléctrica: {potenciaElectrica} kw.  Mínimo {MaquinaElectrica.MIN_POTENCIA_ELECTRICA} kw. y máximo {MaquinaElectrica.MAX_POTENCIA_ELECTRICA} v")

    def getVoltaje(self):
        return self._voltaje

    def getPotenciaElectrica(self):
        return self._potenciaElectrica

    def __str__(self) -> str:
        tmp_str = super().__str__()
        tmp_str = tmp_str[:-1] + f" Voltaje:{self._voltaje} v; Potencia Eléctrica: {self._potenciaElectrica} kw }}"
        return tmp_str
