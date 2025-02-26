from animal import Animal
from boa_constrictor import Boa_Constrictor
from huron import Huron
from ianimal import iAnimal


class Guarderia:
    def __init__(self):
        self._nombre = "Guarderia de Perros"

# crear una instancia para un Huron
huron_1 = Huron("Timon", 5, 3, "Estados Unidos", 10.5)
print("El nombre del huron es: {}, su edad es: {}, su peso es: {}, su pais de origen es: {}, sus impuestos son: {}, por lo que se debe pagar: $ {}".format(huron_1.obtener_nombre(), huron_1.obtener_edad(), huron_1.obtener_peso(), huron_1.obtener_pais_origen(), huron_1.obtener_impuestos(), huron_1.calcular_flete()))

# crear una instancia para una Boa Constrictor y asignarle X número de ratones comidos
boa_1 = Boa_Constrictor("Black Mamba", 8, 30, "Brasil", 15.5)
boa_1.comer_raton(5)
print("El nombre de la Boa Constrictor es: {}, su edad es: {}, su peso es: {}, su pais de origen es: {}, sus impuestos son: {}, por lo que se debe pagar: $ {} en total, ratones comidos: {}".format(boa_1.obtener_nombre(), boa_1.obtener_edad(), boa_1.obtener_peso(), boa_1.obtener_pais_origen(), boa_1.obtener_impuestos(), boa_1.calcular_flete(), boa_1.obtener_ratones_comidos()))