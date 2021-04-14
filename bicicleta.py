from desplazable import Desplazable
from fuerza import Fuerza
from maquinaMecanica import MaquinaMecanica


class Bicicleta(MaquinaMecanica, Desplazable):
    DEFAULT_RADIO_RUEDA = 33.0
    MIN_RADIO_RUEDA = 17.75
    MAX_RADIO_RUEDA = 36.85
    MAX_DESPLAZAMIENTO = 200.0

    def __init__(self, marca: str, modelo: str, radioRueda=None, fuerzaMotriz=Fuerza.Animal):
        super().__init__(marca, modelo, fuerzaMotriz)
        self._radioRueda: float = Bicicleta.DEFAULT_RADIO_RUEDA if radioRueda is None else radioRueda
        self._totalKilometros: float = 0
        if self._radioRueda < Bicicleta.MIN_RADIO_RUEDA or self._radioRueda > Bicicleta.MAX_RADIO_RUEDA:
            raise Exception(f"Error en valor del radio: {self._radioRueda} cm. Debe estar comprendido entre {Bicicleta.MIN_RADIO_RUEDA}cm. y {Bicicleta.MAX_RADIO_RUEDA} cm")

    def desplazar(self, kilometros: float):
        if kilometros < 0 or kilometros > Bicicleta.MAX_DESPLAZAMIENTO:
            raise Exception(f"Cantidad de kilómetros negativa o excesiva (Máx: {Bicicleta.MAX_DESPLAZAMIENTO} km): {kilometros} km.")

    def getTotalKilometrosRecorridos(self) -> float:
        return super().getTotalKilometrosRecorridos()

    def getKilometrosSinRepostar(self) -> float:
        return super().getKilometrosSinRepostar()

    def __str__(self) -> str:
        tmp_str = super().__str__()
        tmp_str = tmp_str[:-1] + f" Radio: {self._radioRueda}; Kilómetros: {self._totalKilometros}  }}"
        return tmp_str


