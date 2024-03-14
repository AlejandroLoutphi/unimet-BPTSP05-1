#Universidad Metropolitana
#Proyecto: Metrotify
#Trimestre 2324-2
#Algoritmos y Programación (BPTSP05) Sección 1
#Alejandro Loutphi Trasande

#Este archivo contiene la clase Playlist, junto con todas las funciones que interactúan con esta y playlists.txt

from funcs import read_dict_from_file_or_website_qae
from funcs import input_list_element
from musica import menu_str_from_song_id
from usuarios import name_from_user_id
from usuarios import menu_str_from_user_id
from musica import search_song_ret_id
from usuarios import search_artist_ret_song_id
from musica import pick_song_from_id_list_to_play
from musica import song_id_stream_lists
from usuarios import user_id_and_type_from_name
from musica import musician_total_streams
from musica import select_artist_album_to_play
from usuarios import user1_has_liked_user2_from_ids
from usuarios import add_user1_to_user2_likes_from_ids
from usuarios import remove_user1_to_user2_likes_from_ids
from musica import print_most_streamed_songs_by_musician
from musica import print_liked_album_names
from musica import print_liked_song_names
from funcs import matplotlib_barchart
import json

class Playlist:
    def __init__(self, playlist_info: dict):
        self.id = playlist_info["id"]
        self.name = playlist_info["name"]
        self.description = playlist_info["description"]
        self.creator = playlist_info["creator"]
        self.tracks = playlist_info["tracks"]
        try: self.likes = playlist_info["likes"]
        except: self.likes = []
    def menu_str(self) -> str:
        '''
        Retorna los parámetros en un formato de str amigable para el usuario.
        '''
        return ("\nNombre: " + self.name + "\nDescripción: " + self.description + "\nCreador: " + name_from_user_id(self.creator) + "Likes: " + str(len(self.likes)) + "\nCanciones: " + '\n'.join([menu_str_from_song_id(i) for i in self.tracks]) + "\n\n")
    def to_dict(self) -> dict:
        '''
        Convierte atributos a formato de diccionario
        :return: Diccionario con los atributos
        '''
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "creator": self.creator,
            "tracks": self.tracks,
            "likes": self.likes,
        }

def write_playlists_to_file(playlists: list, file_name: str):
    '''
    Convierte a una lista de objetos Playlist a formato JSON y los mueve al archivo con nombre file_name
    :param users: lista de objetos Playlist 
    :param file_name: nombre del archivo al que se deben guardar el JSON
    '''
    playlists_dict_list = [i.to_dict() for i in playlists]
    json.dump(playlists_dict_list, open(file_name, "w"))
    return

def create_and_save_playlist(logged_user_id: str):
    '''
    Guía al usuario a insertar los datos de un playlist y actualiza playlists.txt
    :param logged_user_id: ID del usuario creando el playlist
    '''
    playlists_dict = read_dict_from_file_or_website_qae("playlists.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json")
    playlists = [Playlist(i) for i in playlists_dict]

    name = input("¿Cuál sería el nombre del playlist?\n")
    description = input("¿Cuál sería la descripción del playlist?\n")
    print("Ahora buscarás las canciones que van a estar en el playlist.")

    tracks = []
    while True:
        x = input_list_element("¿Desearía buscar la canción por:\n1) Nombre, o\n2) Artista\n?\n", ['1', '2'])
        try:
            if x=='1': song_id = search_song_ret_id()
            else: song_id = search_artist_ret_song_id()
        except:
            print("Ningún artista o canción coincide con la busqueda")
            continue
        if song_id in tracks:
            print("Esta canción ya estaba en el playlist")
            continue
        tracks.append(song_id)
        if input_list_element("¿Desea añadir otra canción?\n1) Sí\n2) No, esas son todas las canciones del playlist\n", ['1', '2']) == '2': break

    playlist_info = {
        "id": "00000000-0000-0000-0000-000000000000",
        "name": name,
        "description": description,
        "creator": logged_user_id,
        "tracks": tracks,
    }
    playlists.append(Playlist(playlist_info))
    write_playlists_to_file(playlists, "playlists.txt")

def search_playlist_to_play(logged_user_id: str):
    '''
    Guía al usuario por el proceso de buscar un playlist por nombre.
    Si ningún playlist coincide con la búsqueda, le informá al usuario y hace return.
    Una vez que el usuario haya buscado el playlist, este puede likearlo o ver las canciones de su tracklist.
    :param logged_user_id: ID del usuario loggeado.
    '''
    playlists_dict = read_dict_from_file_or_website_qae("playlists.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json")
    playlists = [Playlist(i) for i in playlists_dict]

    name = input("Buscar Playlist:\n")
    try: searched_playlist = playlists[[i.name for i in playlists].index(name)]
    except: 
        print("Ningún playlist coincide con la busqueda")
        return

    searched_playlist_id = [i for i in range(len(playlists)) if vars(playlists[i])==vars(searched_playlist)][0]
    if logged_user_id in searched_playlist.likes:
        x = input_list_element("¿Qué desea hacer?\n1) Ver canciones\n2) Quitar like al playlist\n3) Salir\n", ['1','2','3'])
        if x=='2': searched_playlist.likes.remove(logged_user_id)
    else:
        x = input_list_element("¿Qué desea hacer?\n1) Ver canciones\n2) Likear playlist\n3) Salir\n", ['1','2','3'])
        if x=='2': searched_playlist.likes.append(logged_user_id)
    if x=='2':
        playlists.pop(searched_playlist_id)
        playlists.append(searched_playlist)
        write_playlists_to_file(playlists, "playlists.txt")
    if x=='1': pick_song_from_id_list_to_play(searched_playlist.tracks, logged_user_id)

def print_created_playlists(user_id: str):
    '''
    Hace print a los playlist que un músico específico ha creado.
    :param musician_id: ID del usuario del cual se van a imprimir sus playlists.
    '''
    playlists_dict = read_dict_from_file_or_website_qae("playlists.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json")
    playlists = [Playlist(i) for i in playlists_dict]
    user_playlists = [i for i in playlists if i.creator == user_id]
    print("Playlists creados:\n" + '\n'.join([str(i+1) + ')' + user_playlists[i].menu_str() for i in range(len(user_playlists))]))

def print_most_streamed_listeners():
    '''
    Hace print y plot a los 5 listeners cuyos playlists tienen las canciones con más streams totales.
    '''
    playlists_dict = read_dict_from_file_or_website_qae("playlists.txt", "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json")
    playlists = [Playlist(i) for i in playlists_dict]
    song_ids, song_streams = song_id_stream_lists()
    creator_ids = list(set(i.creator for i in playlists))
    creator_playlists = [[i for i in playlists if i.creator==j] for j in creator_ids]
    creator_songs = [sum([j.tracks for j in k], []) for k in creator_playlists]
    creator_streams = [sum([song_streams[song_ids.index(i)] for i in j if i in song_ids]) for j in creator_songs]
    top_creator_indexes = sorted([i for i in range(len(creator_streams))], key=lambda i: -creator_streams[i])[:5]
    creator_ids = [creator_ids[i] for i in top_creator_indexes]
    print("Escuchas con los playlists más escuchados:\n" + '\n\n'.join([str(i+1) + ")" + menu_str_from_user_id(creator_ids[i]) + "\nStreams Totales: " + str(creator_streams[top_creator_indexes[i]]) for i in range(len(creator_ids))]))
    matplotlib_barchart([name_from_user_id(i) for i in creator_ids], [creator_streams[i] for i in top_creator_indexes], "Escuchas más escuchados", "Reproducciones de canciones en playlists")

def search_user_to_play(logged_user_id: str):
    '''
    Guía al usuario por el proceso de buscar un usuario por nombre.
    Si ningún usuario coincide con la búsqueda, le informá al usuario y hace return.
    Una vez que el usuario haya buscado el usuario, este puede likearlo, ver sus álbumes o ver sus canciones más populares si este es de tipo artista.
    Si el usuario buscado es de tipo escucha, se pueden ver sus álbumes likeados, ver sus canciones likeadas o veer sus playlists.
    :param logged_user_id: ID del usuario loggeado.
    '''
    name = input("Buscar Usuario:\n")
    try: searched_user_id, searched_user_type = user_id_and_type_from_name(name)
    except: 
        print("Ningún usuario coincide con la busqueda")
        return
    if searched_user_type==0:
        x = input_list_element("¿Qué desea hacer?\n1) Ver álbumes gustados\n2) Ver canciones gustadas\n3) Ver playlists\n4) Salir\n", ['1','2','3','4'])
        if x=='1': print_liked_album_names(searched_user_id)
        elif x=='2': print_liked_song_names(searched_user_id)
        elif x=='3': print_created_playlists(searched_user_id)
        return

    print("Tipo de Usuario: Artista\nReproducciones Totales: " + str(musician_total_streams(searched_user_id)))
    if user1_has_liked_user2_from_ids(logged_user_id, searched_user_id):
        x = input_list_element("¿Qué desea hacer?\n1) Ver álbumes\n2) Ver canciones más populares\n3) Quitar like al artista\n4) Salir\n", ['1','2','3','4'])
        if x=='3': remove_user1_to_user2_likes_from_ids(logged_user_id, searched_user_id)
    else:
        x = input_list_element("¿Qué desea hacer?\n1) Ver álbumes\n2) Ver canciones más populares\n3) Likear artista\n4) Salir\n", ['1','2','3','4'])
        if x=='3': add_user1_to_user2_likes_from_ids(logged_user_id, searched_user_id)
    if x=='1': select_artist_album_to_play(searched_user_id, logged_user_id)
    elif x=='2': print_most_streamed_songs_by_musician(searched_user_id)