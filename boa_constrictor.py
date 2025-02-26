from animal_exotico import Animal_Exotico


class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float):
        super().__init__(nombre, edad, peso, pais_origen, impuestos)
        self._ratones_comidos = 0
        
    def hacer_sonido(self) -> str:
        print("¡Tsss!")
    
    def comer_raton(self, cantidad: int) -> int:
        self._ratones_comidos += cantidad
    
    def obtener_ratones_comidos(self):
        return self._ratones_comidos