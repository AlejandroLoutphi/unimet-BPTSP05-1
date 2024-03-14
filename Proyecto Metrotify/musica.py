#Universidad Metropolitana
#Proyecto: Metrotify
#Trimestre 2324-2
#Algoritmos y Programación (BPTSP05) Sección 1
#Alejandro Loutphi Trasande

#Este archivo contiene las clases Song y Album, junto con todas las funciones que interactúan con estas y albums.txt

from funcs import read_dict_from_file_or_website_qae
from funcs import input_list_element
from funcs import iso_str_from_current_time
from funcs import create_id
from funcs import matplotlib_barchart
import json
import webbrowser

class Song:
    def __init__(self, song_info: dict):
        self.id = song_info["id"]
        self.name = song_info["name"]
        self.duration = song_info["duration"]
        self.link = song_info["link"]
        try: self.likes = song_info["likes"]
        except: self.likes = []
        try: self.streams = song_info["streams"]
        except: self.streams = 0
    def menu_str(self) -> str:
        '''
        Retorna los parámetros en un formato de str amigable para el usuario.
        '''
        return ("\nNombre: " + self.name + "\nDuración: " + self.duration + "\nLikes: " + str(len(self.likes)) + "\nReproducciones: " + str(self.streams) + '\n')
    def to_dict(self) -> dict:
        '''
        Convierte atributos a formato de diccionario
        :return: Diccionario con los atributos
        '''
        return {
            "id": self.id,
            "name": self.name,
            "duration": self.duration,
            "link": self.link,
            "likes": self.likes,
            "streams": self.streams,
        }
    def play(self):
        '''
        Abre el link de la canción en el buscador.
        A veces soundcloud reproduce un canción previamente accesada en vez de la canción del link por defecto. 🫤
        Añade 1 a self.streams (reproducciones)
        '''
        self.streams+=1
        webbrowser.open(self.link + "#play")

class Album:
    def __init__(self, album_info: dict):
        self.id = album_info["id"]
        self.name = album_info["name"]
        self.description = album_info["description"]
        self.cover = album_info["cover"]
        self.published = album_info["published"]
        self.genre = album_info["genre"]
        self.artist = album_info["artist"]
        self.tracklist = [Song(i) for i in album_info["tracklist"]]
        try: self.likes = album_info["likes"]
        except: self.likes = []
    def menu_str(self):
        '''
        Retorna los parámetros en un formato de str amigable para el usuario.
        '''
        return ("\nNombre: " + self.name + "\nFecha de publicación: " + self.published + "\nGénero: " + self.genre + "\nLikes: " + str(len(self.likes)) + "\nTracklist:\n" + '\n'.join([i.name for i in self.tracklist]))
    def to_dict(self) -> dict:
        '''
        Convierte atributos a formato de diccionario
        :return: Diccionario con los atributos
        '''
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "cover": self.cover,
            "published": self.published,
            "genre": self.genre,
            "artist": self.artist,
            "tracklist": [i.to_dict() for i in self.tracklist],
            "likes": self.likes,
        }

def write_albums_to_file(albums: list, file_name: str):
    '''
    Convierte a una lista de objetos Album a formato JSON y los mueve al archivo con nombre file_name
    :param users: lista de objetos album
    :param file_name: nombre del archivo al que se deben guardar el JSON
    '''
    albums_dict_list = [i.to_dict() for i in albums]
    json.dump(albums_dict_list, open(file_name, "w"))
    return

def song_list_from_album_list(albums: list) -> list:
    '''
    Retorna la lista de todos los Songs en los tracklist en la lista de Albums
    :param albums: Lista de objetos Album de la cual se van a extraer los objetos Song
    '''
    songs = []
    for i in albums:
        for j in i.tracklist:
            songs.append(j)
    return songs

def create_album_id() -> str:
    '''
    Retorna un ID único para los albumes en albums.txt.
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    x = create_id()
    while x in [i.id for i in albums]: x = create_id()
    return x

def create_song_id() -> str:
    '''
    Retorna un ID único para las canciones en albums.txt.
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    songs = song_list_from_album_list(albums)
    x = create_id()
    while x in [i.id for i in songs]: x = create_id()
    return x

def create_song_dict() -> dict:
    '''
    Guía al usuario a insertar los datos de un Song y retorna un dict con esos parámetros.
    '''
    name = input("¿Cuál sería el nombre de la canción?\n")
    duration = input("¿Cuál es la duración de la canción? (Formato mm:ss)\n")
    link = input("Link a la canción:\n")
    return {
        "id": create_song_id(),
        "name": name,
        "duration": duration,
        "link": link,
    }

def create_and_save_album(logged_user_id):
    '''
    Guía al usuario a insertar los datos de un álbum y actualiza albums.txt
    :param logged_user_id: ID del usuario creando el álbum
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]

    name = input("¿Cuál sería el nombre del álbum?\n")
    description = input("¿Cuál sería la descripción del álbum?\n")
    cover = input("Link al cover del álbum:\n")
    published = iso_str_from_current_time()
    genre = input("¿A qué género pertenece el álbum?\n")
    tracklist = []
    while True:
        tracklist.append(create_song_dict())
        if input_list_element("¿Desea añadir otra canción?\n1) Sí\n2) No, esas son todas las canciones del álbum\n", ['1', '2']) == '2': break
    album_info = {
        "id": create_album_id(),
        "name": name,
        "description": description,
        "cover": cover,
        "published": published,
        "genre": genre,
        "artist": logged_user_id,
        "tracklist": tracklist,
    }
    albums.append(Album(album_info))
    write_albums_to_file(albums, "albums.txt")

def id_of_album_with_song_qae(albums: list, song: Song) -> tuple[int, int]: 
    '''
    Retorna una tupla con el index del album en una lista y el index de la canción en el tracklist de ese álbum que contiene el objeto Song pasado.
    :param albums: Lista de objetos Album cuyos tracklists contienen el Song del segundo parámetro
    :param song: Objeto Song que será buscado en la lista albums
    '''
    x = [[song.id == j.id for j in i.tracklist] for i in albums]
    try:
        album_id = [any(i) for i in x].index(True)
        song_id = x[album_id].index(True)
    except:
        print("La canción a modificar no existe")
        quit()
    return (album_id, song_id)

def song_menu(song: Song, logged_user_id: str):
    '''
    Menú del cual el usuario puede decidir reproducir o likear una canción.
    Actualiza albums.txt con esa información.
    :param song: Canción a reproducir o likear
    :param logged_user_id: ID del usuario (para identificar si le ha dado like o no previamente)
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    new_song = song
    print("Canción seleccionada: " + song.name + "\nLikes: " + str(len(song.likes)) + "\nReproducciones: " + str(song.streams))
    while True:
        if logged_user_id in song.likes:
            x = input_list_element("¿Qué desea hacer?\n1) Reproducir canción\n2) Quitar el like de la canción\n3) Salir\n", ['1', '2', '3'])
            if x=='2': new_song.likes.remove(logged_user_id)
        else: 
            x = input_list_element("¿Qué desea hacer?\n1) Reproducir canción\n2) Likear canción\n3) Salir\n", ['1', '2', '3'])
            if x=='2': new_song.likes.append(logged_user_id)
        if x=='1': song.play()
        if x=='3': break
    album_id, song_id = id_of_album_with_song_qae(albums, song)
    modified_album = albums.pop(album_id)
    modified_album.tracklist.pop(song_id)
    modified_album.tracklist.append(new_song)
    albums.append(modified_album)
    write_albums_to_file(albums, "albums.txt")

def search_song_to_play(logged_user_id: str):
    '''
    Guía al usuario por el proceso de buscar una canción para luego reproducirla o darle like.
    :param logged_user_id: ID del usuario
    '''
    x = input("Nombre de la canción:\n")
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    songs = song_list_from_album_list(albums)
    try: searched_song = songs[[i.name for i in songs].index(x)]
    except:
        print("Ninguna canción coincide con la busqueda")
        return
    song_menu(searched_song, logged_user_id)

def pick_song_from_list_to_play(song_list: list, logged_user_id: str):
    '''
    Le pregunta al usuario cuál canción de una lista él quiere seleccionar y llama song_menu() con la lista seleccionada
    :param song_list: Lista de objetos Song de la cual el usuario seleccionará una
    :param logged_user_id: ID del usuario loggeado
    '''
    x = input_list_element("Seleccione una canción:\n" + ''.join([str(i+1) + ")" + song_list[i].menu_str() for i in range(len(song_list))]), [str(i+1) for i in range(len(song_list))])
    song_menu(song_list[int(x)-1], logged_user_id)

def pick_song_from_id_list_to_play(song_id_list: list, logged_user_id: str):
    '''
    Le pregunta al usuario cuál canción de una lista él quiere seleccionar y llama song_menu() con la lista seleccionada
    :param song_id_list: Lista de IDs de canciones de la cual el usuario seleccionará una
    :param logged_user_id: ID del usuario loggeado
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    songs = song_list_from_album_list(albums)
    song_list = [songs[[i.id for i in songs].index(j)] for j in song_id_list]
    pick_song_from_list_to_play(song_list, logged_user_id)

def search_album_to_play(logged_user_id: str):
    '''
    Guía al usuario por el proceso de buscar un album por nombre.
    Si ningún álbum coincide con la búsqueda, le informá al usuario y hace return.
    Una vez que el usuario haya buscado el album, este puede likearlo o ver las canciones de su tracklist.
    :param logged_user_id: ID del usuario loggeado.
    '''
    x = input("Nombre del álbum:\n")
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    try: searched_album = albums[[i.name for i in albums].index(x)]
    except:
        print("Ningún álbum coincide con la busqueda")
        return

    searched_album_id = [i for i in range(len(albums)) if vars(albums[i])==vars(searched_album)][0]
    if logged_user_id in searched_album.likes:
        x = input_list_element("¿Qué desea hacer?\n1) Ver canciones\n2) Quitar like al album\n3) Salir\n", ['1','2','3'])
        if x=='2': searched_album.likes.remove(logged_user_id)
    else:
        x = input_list_element("¿Qué desea hacer?\n1) Ver canciones\n2) Likear album\n3) Salir\n", ['1','2','3'])
        if x=='2': searched_album.likes.append(logged_user_id)
    if x=='2':
        albums.pop(searched_album_id)
        albums.append(searched_album)
        write_albums_to_file(albums, "albums.txt")
    if x=='1': pick_song_from_list_to_play(searched_album.tracklist, logged_user_id)

def select_artist_album_to_play(artist_id: str, logged_user_id: str):
    '''
    Le pregunta al usuario cuál álbum de un artista específico quiere seleccionar. Subsecuentemente hace lo mismo con las canciones de ese álbum
    :param artist_id: ID del artista de cuyos álbumes el usuario va a seleccionar.
    :param logged_user_id: ID del usuario loggeado
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    artist_albums = [i for i in albums if i.artist == artist_id]

    x = input_list_element("Seleccione un álbum:\n" + '\n\n'.join([str(i+1) + ")" + artist_albums[i].menu_str() for i in range(len(artist_albums))]) + '\n', [str(i+1) for i in range(len(artist_albums))])
    pick_song_from_list_to_play(artist_albums[int(x)-1].tracklist, logged_user_id)

def menu_str_from_song_id(id: str) -> str:
    '''
    Retorna un str con los parámetros del objeto Song especificado por el ID inputeado en un formato de str amigable para el usuario.
    :param id: ID del objeto Song del cual se va a retornar el menu_str
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    songs = song_list_from_album_list(albums)
    try: x = songs[[i.id for i in songs].index(id)]
    except: return "Esta canción no existe\n"
    return x.menu_str()

def search_song_ret_id() -> str:
    '''
    Guía al usuario por el proceso de buscar una canción, de la cual se retorna el id.
    ERROR: si ninguna canción coincide con la busqueda.
    :return: ID de la canción buscada
    '''
    x = input("Nombre de la canción:\n")
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    songs = song_list_from_album_list(albums)
    searched_song = songs[[i.name for i in songs].index(x)]
    return searched_song.id

def pick_song_from_list_ret_id(song_list: list) -> str:
    '''
    Guía al usuario a seleccionar una canción de una lista y retorna su ID.
    :param song_list: Lista de objetos Song de la cual el usuario va a seleccionar un elemento.
    '''
    x = input_list_element("Seleccione una canción:\n" + ''.join([str(i+1) + ")" + song_list[i].menu_str() for i in range(len(song_list))]), [str(i+1) for i in range(len(song_list))])
    return song_list[int(x)-1].id

def select_artist_album_ret_song_id(artist_id: str) -> str:
    '''
    Guía al usuario a seleccionar un álbum y subsecuentemente una canción de una lista y retorna su ID.
    :param song_list: Lista de objetos Song de la cual el usuario va a seleccionar un elemento.
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    artist_albums = [i for i in albums if i.artist == artist_id]

    x = input_list_element("Seleccione un álbum:\n" + '\n\n'.join([str(i+1) + ")" + artist_albums[i].menu_str() for i in range(len(artist_albums))]) + '\n', [str(i+1) for i in range(len(artist_albums))])
    return pick_song_from_list_ret_id(artist_albums[int(x)-1].tracklist)

def print_most_streamed_songs():
    '''
    Hace print y plot a las 5 canciones con más streams totales.
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    songs = song_list_from_album_list(albums)
    x = sorted(songs, key=lambda i: -i.streams)[:5]
    print("Canciones más escuchadas:\n" + '\n\n'.join([str(i+1) + ")" + x[i].menu_str() for i in range(len(x))]))
    matplotlib_barchart([i.name for i in x], [i.streams for i in x], "Canciones más escuchadas", "Reproducciones")

def print_most_streamed_songs_by_musician(musician_id):
    '''
    Hace print y plot a las 5 canciones con más streams totales de un músico específico.
    :param musician_id: ID del músico del cual se van a imprimir sus canciones más populares.
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    musician_albums =  [i for i in albums if i.artist==musician_id]
    songs = song_list_from_album_list(musician_albums)
    x = sorted(songs, key=lambda i: -i.streams)[:10]
    print("Sus canciones más escuchadas:\n" + '\n\n'.join([str(i+1) + ")" + x[i].menu_str() for i in range(len(x))]))

def print_most_streamed_albums():
    '''
    Hace print y plot a los 5 álbumes con más streams totales.
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    x = sorted(albums, key=lambda i: -sum([j.streams for j in i.tracklist]))[:5]
    print("Álbumes más escuchados:\n" + '\n\n'.join([str(i+1) + ")" + x[i].menu_str() for i in range(len(x))]))
    matplotlib_barchart([i.name for i in x], [sum([j.streams for j in i.tracklist]) for i in x], "Álbumes más escuchados", "Reproducciones totales")

def musician_total_streams(musician_id: str) -> int:
    '''
    Retorna el número de streams totales de un músico: la suma de los streams de todas sus canciones.
    :param musician_id: ID del músico del cual se van a retornar sus streams totales
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    return sum([sum([i.streams for i in j.tracklist]) for j in albums if j.artist==musician_id])

def song_id_stream_lists() -> tuple[list, list]:
    '''
    Retorna una tupla con 2 listas: una con el id de todas las canciones en albums.txt, y otra con el número de streams de cada una de esas canciones
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    songs = song_list_from_album_list(albums)
    return [i.id for i in songs], [i.streams for i in songs]

def print_liked_song_names(user_id: str):
    '''
    Imprime los nombres de todas las canciones que un usuario a likeado
    :param user_id: ID del usuario del cual se van a imprimir sus canciones likeadas
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    songs = song_list_from_album_list(albums)
    liked_songs = [i for i in songs if user_id in i.likes]
    print("Canciones gustadas:\n" + '\n'.join([str(i+1) + ')' + liked_songs[i].menu_str() for i in range(len(liked_songs))]))

def print_liked_album_names(user_id: str):
    '''
    Imprime los nombres de todos los álbumes que un usuario a likeado
    :param user_id: ID del usuario del cual se van a imprimir sus álbumes likeados
    '''
    albums_dict = read_dict_from_file_or_website_qae("albums.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
    albums = [Album(i) for i in albums_dict]
    liked_albums = [i for i in albums if user_id in i.likes]
    print("Álbumes gustados:\n" + '\n'.join([str(i+1) + ')' + liked_albums[i].menu_str() for i in range(len(liked_albums))]))