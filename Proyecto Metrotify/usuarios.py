#Universidad Metropolitana
#Proyecto: Metrotify
#Trimestre 2324-2
#Algoritmos y Programación (BPTSP05) Sección 1
#Alejandro Loutphi Trasande

#Este archivo contiene las clases User y sus sub-clases Listener y Musician, junto con todas las funciones que interactúan con estas y users.txt

from funcs import read_dict_from_file_or_website_qae
from funcs import input_list_element
from funcs import create_id
from musica import select_artist_album_ret_song_id
from musica import musician_total_streams
from funcs import matplotlib_barchart
import json

class User:
    def __init__(self, profile_info: dict):
        self.id = profile_info["id"]
        self.name = profile_info["name"]
        self.email = profile_info["email"]
        self.username = profile_info["username"]
    def change_info(self):
        '''
        Guía al usuario a cambiar su name o email y actualiza self con ese cambio.
        '''
        x = input_list_element("¿Qué desea cambiar?\n1) Nombre\n2) Email\n3) Salir\n", ['1', '2', '3'])
        if x == '1': self.name = input("Nuevo Nombre:\n")
        elif x == '2': self.email = input("Nuevo Email:\n")
    def to_dict(self) -> dict:
        '''
        Convierte atributos a formato de diccionario
        :return: Diccionario con los atributos de user
        '''
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "username": self.name,
            "type": "None",
        }
        
class Listener(User):
    def menu_str(self) -> str:
        '''
        Retorna los parámetros en un formato de str amigable para el usuario.
        '''
        return ("\nNombre: " + self.name)
    def to_dict(self) -> dict:
        '''
        Convierte atributos a formato de diccionario
        :return: Diccionario con los atributos de user
        '''
        x = super().to_dict()
        x["type"] = "listener"
        return x

class Musician(User):
    def __init__(self, profile_info: dict):
        super().__init__(profile_info)
        try: self.likes = profile_info["likes"]
        except: self.likes = []
    def menu_str(self) -> str:
        '''
        Retorna los parámetros en un formato de str amigable para el usuario.
        '''
        return ("\nNombre: " + self.name + "\nReproducciones Totales: " + str(musician_total_streams(self.id)))
    def to_dict(self) -> dict:
        '''
        Convierte atributos a formato de diccionario
        :return: Diccionario con los atributos de user
        '''
        x = super().to_dict()
        x["type"] = "musician"
        x["likes"] = self.likes
        return x

def write_users_to_file(users: list, file_name: str):
    '''
    Convierte a una lista de objetos de una subclase de User a formato JSON y los mueve al archivo con nombre file_name
    :param users: lista de objetos de una sublase de User
    :param file_name: nombre del archivo al que se deben guardar el JSON
    '''
    users_dict_list = [i.to_dict() for i in users]
    json.dump(users_dict_list, open(file_name, "w"))
    return

def create_user_id() -> str:
    '''
    Retorna un ID único en users.txt.
    '''
    users_dict = read_dict_from_file_or_website_qae("users.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    users = [Musician(i) if i["type"] == "musician" else Listener(i) for i in users_dict]
    x = create_id()
    while x in [i.id for i in users]: x = create_id()
    return x

def register_user() -> tuple[str, int]:
    '''
    Guía al usuario a insertar sus datos de usuario y guarda los datos a users.txt
    :return: ID y tipo (0=Escucha, 1=Músico) del nuevo usuario en una tupla
    '''
    users_dict = read_dict_from_file_or_website_qae("users.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    users = [Musician(i) if i["type"] == "musician" else Listener(i) for i in users_dict]
    name = input("¿Cuál es su nombre o nombre artístico?\n")
    email = input("¿Cuál es su correo electrónico?\n")
    usertype = input_list_element("¿Es usted:\n1) Músico, o\n2) Solo escucha música?\n", ['1', '2'])
    profile_info = {
        "id": create_user_id(),
        "name": name,
        "email": email,
        "username": name,
    }
    if usertype == '1':
        new_user = Musician(profile_info)
        y = 1
    else:
        new_user = Listener(profile_info)
        y = 0
    users.append(new_user)
    write_users_to_file(users, "users.txt")
    return (new_user.id, y)

def delete_account(users: list, logged_user: int):
    '''
    Borra la cuenta de la lista users y actualiza user.txt.
    Informa al usuario después de que la operación se complete y termina el programa.
    :param users: Lista de usuarios de la cual se va a borrar el usuario
    :param logged_user_id: Index del usuario que va a ser borrado en la lista users
    '''
    users.pop(logged_user)
    write_users_to_file(users, "users.txt")
    print("Su cuenta ha sido borrada")
    quit()

def manage_profile(logged_user_id: str):
    '''
    Le pregunta al usuario si quiere cambiar la información o borrar su cuenta.
    Luego ejecuta la acción seleccionada por el usuario.
    :param logged_user_id: ID del usuario loggeado, objeto del cual sería modificado o borrado.
    '''
    users_dict = read_dict_from_file_or_website_qae("users.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    users = [Musician(i) if i["type"] == "musician" else Listener(i) for i in users_dict]
    logged_user = [i.id for i in users].index(logged_user_id)

    x = input_list_element("¿Qué quiere hacer?\n1) Cambiar información de la cuenta\n2) Borrar cuenta\n3) Salir\n", ['1', '2', '3'])
    if x == '1':
        users[logged_user].change_info()
        write_users_to_file(users, "users.txt")
    elif x == '2':
        xa = input_list_element("Confirmar: ¿Desea borrar los datos de la cuenta?\n1) Sí\n2) No\n", ['1', '2'])
        if xa == '1': delete_account(users, logged_user)

def name_from_user_id(id: str) -> str:
    '''
    Retorna el nombre del usuario con el id inputeado
    :param id: ID del usuario del cual se va a retornar el nombre
    '''
    users_dict = read_dict_from_file_or_website_qae("users.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    users = [Musician(i) if i["type"] == "musician" else Listener(i) for i in users_dict]
    try: x = users[[i.id for i in users].index(id)]
    except: return "Esta usuario no existe\n"
    return x.name

def menu_str_from_user_id(id: str) -> str:
    '''
    Retorna un str con los parámetros del objeto especificado por el ID inputeado en un formato de str amigable para el usuario.
    :param id: ID del usuario del cual se va a retornar el menu_str
    '''
    users_dict = read_dict_from_file_or_website_qae("users.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    users = [Musician(i) if i["type"] == "musician" else Listener(i) for i in users_dict]
    try: x = users[[i.id for i in users].index(id)]
    except: return "Esta usuario no existe\n"
    return x.menu_str()

def user_id_and_type_from_name(name) -> tuple[str, int]:
    '''
    Guía al usuario a buscar a un usuario registrado por nombre. Retorna el ID y tipo del usuario (0 = Escucha, 1 = Músico) buscado.
    ERROR si no hay usuario con el nombre que se insertó.
    :return: ID y tipo del usuario buscado en una tupla.
    '''
    users_dict = read_dict_from_file_or_website_qae("users.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    users = [Musician(i) if i["type"] == "musician" else Listener(i) for i in users_dict]
    x = users[[i.name for i in users].index(name)]
    if type(x) is Listener: y=0
    else: y=1
    return x.id, y

def user1_has_liked_user2_from_ids(user1_id: str, user2_id: str) -> bool:
    '''
    Retorna un bool que dice si el usuario del primer parámetro likeo el usuario del segundo parámetro.
    :param user1_id: ID del usuario que puede haber likeado al otro usuario.
    :param user2_id: ID del usuario que puede haber recibido un like del otro usuario.
    '''
    users_dict = read_dict_from_file_or_website_qae("users.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    users = [Musician(i) if i["type"] == "musician" else Listener(i) for i in users_dict]
    user2 = users[[i.id for i in users].index(user2_id)]
    return user1_id in user2.likes

def add_user1_to_user2_likes_from_ids(user1_id: str, user2_id: str):
    '''
    Añade un like por parte del primer usuario al segundo usuario.
    :param user1_id: ID del usuario que likeará al otro usuario.
    :param user2_id: ID del usuario que recibirá un like del otro usuario.
    '''
    users_dict = read_dict_from_file_or_website_qae("users.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    users = [Musician(i) if i["type"] == "musician" else Listener(i) for i in users_dict]
    user2_index = [i.id for i in users].index(user2_id)
    user2 = users[user2_index]
    user2.likes.append(user1_id)
    users.pop(user2_index)
    users.append(user2)
    write_users_to_file(users, "users.txt")

def remove_user1_to_user2_likes_from_ids(user1_id: str, user2_id: str):
    '''
    Quita un like por parte del primer usuario al segundo usuario.
    :param user1_id: ID del usuario que quitará su like al otro usuario.
    :param user2_id: ID del usuario del cual se va a quitar el like del otro usuario.
    '''
    users_dict = read_dict_from_file_or_website_qae("users.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    users = [Musician(i) if i["type"] == "musician" else Listener(i) for i in users_dict]
    user2_index = [i.id for i in users].index(user2_id)
    user2 = users[user2_index]
    user2.likes.remove(user1_id)
    users.pop(user2_index)
    users.append(user2)
    write_users_to_file(users, "users.txt")

def search_artist_ret_song_id() -> str:
    '''
    Guía al usuario a buscar un usuario de tipo Musician por nombre y retorna el ID de una de la canción subsecuentemente seleccionada por el usuario
    '''
    users_dict = read_dict_from_file_or_website_qae("users.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    users = [Musician(i) for i in users_dict if i["type"] == "musician"]

    name = input("Buscar Usuario:\n")
    searched_user = users[[i.name for i in users].index(name)]
    return select_artist_album_ret_song_id(searched_user.id)

def print_most_streamed_musicians():
    '''
    Hace print y plot a los 5 músicos con más streams totales.
    '''
    users_dict = read_dict_from_file_or_website_qae("users.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
    users = [Musician(i) for i in users_dict if i["type"] == "musician"]
    user_ids = [i.id for i in users]
    x = [users[user_ids.index(j)] for j in sorted(user_ids, key=lambda i: -musician_total_streams(i))[:5]]
    print("Artistas más escuchados:\n" + '\n\n'.join([str(i+1) + ")" + x[i].menu_str() for i in range(len(x))]))
    matplotlib_barchart([i.name for i in x], [musician_total_streams(i.id) for i in x], "Artistas más escuchados", "Reproducciones totales")