#Universidad Metropolitana
#Proyecto: Metrotify
#Trimestre 2324-2
#Algoritmos y Programación (BPTSP05) Sección 1
#Alejandro Loutphi Trasande

#Este archivo contiene los menús principales de la aplicación, a los cuales el usuario regresa después de realizar cualquier operación

from funcs import input_list_element
from usuarios import manage_profile
from musica import search_song_to_play
from musica import search_album_to_play
from playlists import search_user_to_play
from playlists import search_playlist_to_play
from playlists import create_and_save_playlist
from musica import create_and_save_album
from estadisticas import menu_estadisticas

def menu_escucha(logged_user_id: str):
    '''
    Menú principal para usuarios de tipo escucha.
    :param logged_user_id: ID del usuario loggeado
    '''
    while True:
        x = input_list_element("¿Qué desea hacer?\n1) Gestionar Perfil\n2) Buscar canciones\n3) Buscar álbumes\n4) Buscar usuarios\n5) Buscar playlists\n6) Crear playlist\n7) Ver Estadísticas\n8) Salir\n", ['1', '2', '3', '4', '5', '6', '7', '8'])

        if x=='1': manage_profile(logged_user_id)
        elif x=='2': search_song_to_play(logged_user_id)
        elif x=='3': search_album_to_play(logged_user_id)
        elif x=='4': search_user_to_play(logged_user_id)
        elif x=='5': search_playlist_to_play(logged_user_id)
        elif x=='6': create_and_save_playlist(logged_user_id)
        elif x=='7': menu_estadisticas()
        else: quit()

def menu_musico(logged_user_id: str):
    '''
    Menú principal para usuarios de tipo músico.
    Tiene más opciones que el de tipo escucha, debido a que los músicos pueden crear álbumes.
    :param logged_user_id: ID del usuario loggeado
    '''
    while True:
        x = input_list_element("¿Qué desea hacer?\n1) Gestionar Perfil\n2) Crear nuevo álbum\n3) Crear nuevo playlist\n4) Buscar canciones\n5) Buscar álbumes\n6) Buscar usuarios\n7) Buscar playlists\n8) Ver Estadísticas\n9) Salir\n", ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

        if x=='1': manage_profile(logged_user_id)
        elif x=='2': create_and_save_album(logged_user_id)
        elif x=='3': create_and_save_playlist(logged_user_id)
        elif x=='4': search_song_to_play(logged_user_id)
        elif x=='5': search_album_to_play(logged_user_id)
        elif x=='6': search_user_to_play(logged_user_id)
        elif x=='7': search_playlist_to_play(logged_user_id)
        elif x=='8': menu_estadisticas()
        else: quit()