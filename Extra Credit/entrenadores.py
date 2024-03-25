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