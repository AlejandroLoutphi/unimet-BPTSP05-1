#Universidad Metropolitana
#Proyecto: Metrotify
#Trimestre 2324-2
#Algoritmos y Programación (BPTSP05) Sección 1
#Alejandro Loutphi Trasande y Ayah ZaherAlDeen

class Trainer:
    def __init__(self, name: str, pokemon: None|list =None):
        self.name = name
        if pokemon is not None: self.pokemon = pokemon
        else: self.pokemon = []

class Player(Trainer):
    level = 1
    badges = []
    def __init__(self, name: str, gender: str, age: int, region: str):
        super().__init__(name)
        self.gender = gender
        self.gender_opt = 'a'*(gender=='a')
        self.name = name
        self.age = age
        self.region = region