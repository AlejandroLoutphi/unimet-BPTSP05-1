class Game:
    def __init__(self, id_game, local_team, visit_team, stadium):
        self.id_game = id_game
        self.local_team = local_team
        self.visit_team = visit_team
        self.stadium = stadium
    def read(self):
        print("ID del Juego: " + str(self.id_game))
        print("Equipo Local: " + self.local_team)
        print("Equipo de Visita: " + self.visit_team)
        print("Estadio: " + self.stadium)
        print("")

class Person:
    def __init__(self, name):
        self.name = name
    def read(self):
        print("Nombre: " + self.name)

class Player(Person):
    def __init__(self, name, player_id, team_number, position):
        Person.__init__(self, name)
        self.player_id = player_id 
        self.team_number = team_number
        self.position = position
    def read(self):
        Person.read(self)
        print("Player ID: " + str(self.player_id))
        print("Team Number: " + str(self.team_number))
        print("Position: " + str(self.player_id))
        print("")

class Client(Person):
    def __init__(self, name, game, quantity, assist_confirmed):
        Person.__init__(self, name)
        self.game = game
        self.quantity = quantity
        self.assist_confirmed = assist_confirmed
    def read(self):
        Person.read(self)
        print("Game: " + self.game.read())
        print("Quantity: " + str(self.quantity))
        print("Assist Confirmed: " + str(self.assist_confirmed))
        print("")
    def confirmed(self):
        self.assist_confirmed = True

class Team:
    def __init__(self, id_team, name, players):
        self.id_team = id_team
        self.name = name
        self.players = players
    def read(self):
        print("ID de Equipo: " + str(self.id_team))
        print("Nombre: " + self.name)
        print("Jugadores: ")
        [i.read() for i in players]
        print("")
    

db = {
    'Jugadores': [['Miguel Rodriguez', 1, 'Lanzador', 82],
                  ['Gabriel Lino', 2, 'Catcher', 75],
                  ['Erick Brito', 3, 'Infielder', 52],
                  ['Oswaldo Arcia', 4, 'Outfielder', 31],
                  ['Eduard Bazardo', 5, 'Lanzador', 83],
                  ['Rene Pinto', 6, 'Catcher', 87],
                  ['Rayder Ascanio', 7, 'Infielder', 60],
                  ['Victor Arias', 8, 'Outfielder', 78],
                  ['David Davalillo', 9, 'Lanzador', 77],
                  ['Roberto Alvarez', 10, 'Catcher', 33],
                  ['Leonardo Reginatto', 11, 'Infielder', 22],
                  ['Oswaldo Cabrera', 12, 'Outfielder', 17]],
    'Equipos': [
        {'Nombre': 'Leones de Caracas',
        'Jugadores': [1, 2, 3, 4],
        'ID': 1}, 
        {'Nombre': 'Navegantes del Magallanes',
        'Jugadores': [5, 6, 7, 8],
        'ID': 2}, 
        {'Nombre': 'Tiburones de la Guaira',
        'Jugadores': [9, 10, 11, 12],
        'ID': 3 }
               ],
  
    'Partidos': [
        [1, 'Leones de Caracas', 'Navegantes del Magallanes', 'Estadio Monumental de Caracas "Simón Bolívar"'],
        [2, 'Leones de Caracas', 'Tiburones de la Guaira', 'Estadio Forum de La Guaira'],
        [3, 'Tiburones de la Guaira', 'Navegantes del Magallanes', 'Estadio Universitario de Caracas'],
              ],
  
    'Compradores': [ 
        {'Nombre': 'Maria Martinez',
        'Partido': 1,
        'CantidadEntradas': 2,
        'Asistencia': False}, 
        {'Nombre': 'Javier Teixeira',
        'Partido': 2,
        'CantidadEntradas': 4,
        'Asistencia': False}, 
        {'Nombre': 'Antonio Guerra',
        'Partido': 3,
        'CantidadEntradas': 2,
        'Asistencia': False}, 
       {'Nombre': 'Luis Bello',
        'Partido': 1,
       'CantidadEntradas': 6,
       'Asistencia': False}
               ]
}

players = [Player(i[0], i[1], i[3], i[2]) for i in db['Jugadores']]
teams = [Team(i['ID'], i['Nombre'], i['Jugadores']) for i in db['Equipos']]
games = [Game(i[0], i[1], i[2], i[3]) for i in db['Partidos']]
clients = [Client(i['Nombre'], i['Partido'], i['CantidadEntradas'], i['Asistencia']) for i in db['Compradores']]

def player_table(teams, players):
    for i in teams:
        i.read()

def game_itinerary(games):
    for i in games:
        i.read()

def confirm_assistance(player):


for i in 
    