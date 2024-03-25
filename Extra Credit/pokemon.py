class PkmType:
    def __init__(self, name: str, strengths: list, weaknesses: list, inmunes: list):
        self.name = name
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.inmunes = inmunes

def get_ptype(name: str) -> PkmType:
    return {
        "normal": PkmType("normal", [], ["rock"], ["ghost"]),
        "fire": PkmType("fire", ["grass", "ice", "bug"], ["fire", "water", "rock"], []),
        "water": PkmType("water", ["fire", "ground", "rock"], ["water", "grass"], []),
        "electric": PkmType("electric", ["water", "flying"], ["electric", "grass"], ["ground"]),
        "grass": PkmType("grass", ["water", "ground", "rock"], ["fire", "grass", "poison", "flying", "bug"], []),
        "ice": PkmType("ice", ["grass", "ground", "flying"], ["water", "ice"], []),
        "fighting": PkmType("fighting", ["normal", "ice", "rock"], ["poison", "flying", "psychic", "bug"], ["ghost"]),
        "poison": PkmType("poison", ["grass", "bug"], ["poison", "ground", "rock", "ghost"], []),
        "ground": PkmType("ground", ["fire", "electric", "poison", "rock"], ["grass", "bug"], ["flying"]),
        "flying": PkmType("flying", ["grass", "fighting", "bug"], ["electric", "rock"], []),
        "psychic": PkmType("psychic", ["fighting", "poison"], ["psychic"], []),
        "bug": PkmType("bug", ["grass", "poison", "psychic"], ["fire", "fighting", "flying", "ghost"], []),
        "rock": PkmType("rock", ["fighting", "ground"], ["fire", "ice", "flying", "bug"], []),
        "ghost": PkmType("ghost", ["ghost"], [], ["normal", "psychic"]),
    }[name]

class Attack:
    def __init__(self, name: str, power: int, defense: int, accuracy: int, ptype: PkmType):
        self.name = name
        self.power = power
        self.defense = defense
        self.accuracy = accuracy
        self.ptype = ptype

def get_attack(name: str) -> Attack:
    return {
        "mega patada": Attack("mega patada", 120, 0, 75, get_ptype("normal")),
        "tormenta de nieve": Attack("tormenta de nieve", 110, 0, 70, get_ptype("ice")),
        "explosión de fuego": Attack("explosión de fuego", 110, 0, 85, get_ptype("fire")),
        "bomba de agua": Attack("bomba de agua", 110, 0, 80, get_ptype("water")),
        "trueno": Attack("trueno", 110, 0, 70, get_ptype("electric")),
        "martillo de cangrejo": Attack("martillo de cangrejo", 100, 0, 90, get_ptype("water")),
        "terremoto": Attack("terremoto", 100, 0, 100, get_ptype("ground")),
        "bomba de huevo": Attack("bomba de huevo", 100, 0, 75, get_ptype("normal")),
        "lanzallamas": Attack("lanzallamas", 90, 0, 100, get_ptype("fire")),
        "rayo de hielo": Attack("rayo de hielo", 90, 0, 100, get_ptype("ice")),
        "psíquico": Attack("psíquico", 90, 10, 100, get_ptype("psychic")),
        "surf": Attack("surf", 90, 0, 100, get_ptype("water")),
        "rayo": Attack("rayo", 90, 0, 100, get_ptype("electric")),
        "golpe al cuerpo": Attack("golpe al cuerpo", 85, 0, 100, get_ptype("normal")),
        "picoteo de taladro": Attack("picoteo de taladro", 80, 0, 100, get_ptype("flying")),
        "mega puñetazo": Attack("mega puñetazo", 80, 0, 85, get_ptype("normal")),
        "catarata": Attack("catarata", 80, 0, 100, get_ptype("water")),
        "puñetazo de fuego": Attack("puñetazo de fuego", 75, 0, 100, get_ptype("fire")),
        "puñetazo de hielo": Attack("puñetazo de hielo", 75, 0, 100, get_ptype("ice")),
        "puñetazo eléctrico": Attack("puñetazo eléctrico", 75, 0, 100, get_ptype("electric")),
        "deslizamiento de roca": Attack("deslizamiento de roca", 75, 0, 90, get_ptype("rock")),
        "acuchillar": Attack("acuchillar", 70, 0, 100, get_ptype("normal")),
        "rayo de aurora": Attack("rayo de aurora", 65, 10, 100, get_ptype("ice")),
        "rayo de burbuja": Attack("rayo de burbuja", 65, 10, 100, get_ptype("water")),
        "rayo psíquico": Attack("rayo psíquico", 65, 10, 100, get_ptype("psychic")),
        "garrote de huesos": Attack("garrote de huesos", 65, 0, 85, get_ptype("ground")),
        "lodo": Attack("lodo", 65, 0, 100, get_ptype("poison")),
        "doble patada": Attack("doble patada", 60, 0, 100, get_ptype("fighting")),
        "mordedura": Attack("mordedura", 60, 0, 100, get_ptype("normal")),
        "patada rodante": Attack("patada rodante", 60, 0, 85, get_ptype("fighting")),
        "ataque de ala": Attack("ataque de ala", 60, 0, 85, get_ptype("flying")),
        "navaja de hoja": Attack("navaja de hoja", 55, 0, 95, get_ptype("grass")),
        "agujas gemelas": Attack("agujas gemelas", 50, 0, 70, get_ptype("bug")),
        "confusión": Attack("confusión", 50, 0, 100, get_ptype("psychic")),
        "corte": Attack("corte", 50, 0, 95, get_ptype("normal")),
        "corte de karate": Attack("corte de karate", 50, 0, 100, get_ptype("fighting")),
        "tiro de roca": Attack("tiro de roca", 50, 0, 90, get_ptype("rock")),
        "látigo cepa": Attack("látigo cepa", 45, 0, 100, get_ptype("grass")),
        "ácido": Attack("ácido", 40, 20, 100, get_ptype("poison")),
        "burbuja": Attack("burbuja", 40, 10, 100, get_ptype("water")),
        "ascuas": Attack("ascuas", 40, 0, 100, get_ptype("fire")),
        "ráfaga": Attack("ráfaga", 40, 0, 100, get_ptype("flying")),
        "placaje": Attack("placaje", 40, 0, 100, get_ptype("normal")),
        "choque de trueno": Attack("choque de trueno", 40, 0, 100, get_ptype("electric")),
        "pistola de agua": Attack("pistola de agua", 40, 0, 100, get_ptype("water")),
        "picoteo": Attack("picoteo", 35, 0, 100, get_ptype("flying")),
        "lengüetazo": Attack("lengüetazo", 30, 0, 100, get_ptype("ghost")),
        "niebla tóxica": Attack("niebla tóxica", 30, 0, 70, get_ptype("poison")),
        "mirada lasciva": Attack("mirada lasciva", 0, 30, 100, get_ptype("normal")),
        "látigo": Attack("látigo", 0, 35, 100, get_ptype("normal")),
        "chillido": Attack("chillido", 0, 50, 85, get_ptype("normal")),
    }[name]

class Pokemon:
    def __init__(self, name: str, hp: int, power: int, defense: int, attacks: list, ptype: str):
        self.name = name
        self.hp = hp
        self.power = power
        self.defense = defense 
        self.attacks = attacks
        self.ptype = ptype
        self.level = 0
    def learn_attack(self):
        if not self.name in ["bulbasaur", "charmander", "squirtle"]: return
        learn_set = {
            "bulbasaur": ["navaja de hoja", "mordedura", "lodo", "chillido", "catarata", "golpe al cuerpo", "mega patada"],
            "charmander": ["tiro de roca", "doble patada", "garrote de huesos", "chillido", "acuchillar", "lanzallamas", "explosión de fuego"],
            "squirtle": ["agujas gemelas", "mordedura", "rayo de burbuja", "puñetazo de hielo", "surf", "terremoto", "bomba de agua"],
        }
        self.attacks.append(get_attack(learn_set[self.name][self.level//2-1]))
        print(self.name.upper() + " ha aprendido a usar " + learn_set[self.name][self.level//2-1].upper())

def get_pokemon(name: str) -> Pokemon:
    try: return {
        "rattata": Pokemon("rattata", 75, 56, 35, [get_attack("placaje"), get_attack("mirada lasciva")], "normal"),
        "caterpie": Pokemon("caterpie", 110, 30, 35, [get_attack("placaje"), get_attack("látigo")], "bug"),
        "pidgey": Pokemon("pidgey", 100, 45, 40, [get_attack("placaje"), get_attack("ráfaga")], "flying"),
        "bellsprout": Pokemon("bellsprout", 125, 75, 35, [get_attack("látigo cepa"), get_attack("ácido")], "grass"),
        "mankey": Pokemon("mankey", 120, 80, 35, [get_attack("corte de karate"), get_attack("mirada lasciva")], "fighting"),
        "geodude": Pokemon("geodude", 100, 60, 100, [get_attack("tiro de roca"), get_attack("placaje"), get_attack("mega puñetazo")], "rock"),
        "drowzee": Pokemon("drowzee", 150, 48, 60, [get_attack("placaje"), get_attack("mirada lasciva"), get_attack("psíquico")], "psychic"),
        "snorlax": Pokemon("snorlax", 400, 8, 50, [get_attack("placaje"), get_attack("mega puñetazo"), get_attack("rayo de burbuja")], "normal"),
        "tentacool": Pokemon("tentacool", 100, 50, 60, [get_attack("pistola de agua"), get_attack("ácido"), get_attack("chillido"), get_attack("surf")], "water"),
        "pikachu": Pokemon("pikachu", 85, 55, 50, [get_attack("choque de trueno"), get_attack("trueno"), get_attack("corte")], "electric"),
        "ekans": Pokemon("ekans", 85, 60, 55, [get_attack("mordedura"), get_attack("chillido"), get_attack("ácido"), get_attack("deslizamiento de roca")], "poison"),
        "haunter": Pokemon("haunter", 110, 115, 45, [get_attack("lengüetazo"), get_attack("lodo"), get_attack("confusión"), get_attack("chillido")], "ghost"),
        "dugtrio": Pokemon("dugtrio", 85, 100, 50, [get_attack("terremoto"), get_attack("placaje"), get_attack("corte"), get_attack("mirada lasciva")], "ground"),

        "bulbasaur": Pokemon("bulbasaur", 110, 65, 65, [get_attack("placaje"), get_attack("látigo cepa"), get_attack("látigo")], "grass"),
        "charmander": Pokemon("charmander", 98, 60, 50, [get_attack("placaje"), get_attack("ascuas"), get_attack("mirada lasciva")], "fire"),
        "squirtle": Pokemon("squirtle", 108, 50, 65, [get_attack("placaje"), get_attack("pistola de agua"), get_attack("látigo")], "water"),
    }[name]
    except: return Pokemon("missingno", 255, 255, 255, [get_attack("látigo"), get_attack("chillido")], "normal")