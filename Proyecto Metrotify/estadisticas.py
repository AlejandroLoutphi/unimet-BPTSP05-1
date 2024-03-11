#Universidad Metropolitana
#Proyecto: Metrotify
#Trimestre 2324-2
#Algoritmos y Programación (BPTSP05) Sección 1
#Alejandro Loutphi Trasande

#Este archivo contiene un sub-menú con la funcionalidad respectiva a los indicadores de gestión

from funcs import input_list_element
from usuarios import print_most_streamed_musicians
from musica import print_most_streamed_albums
from musica import print_most_streamed_songs
from playlists import print_most_streamed_listeners

def menu_estadisticas():
    '''
    Menú en el que el usuario puede seleccionar ver el top 5 de músicos, álbumes, canciones o usuarios escucha en términos de reproducciones (streams).
    '''
    x = input_list_element("Ver el top 5 de:\n1) Músicos\n2) Álbumes\n3) Canciones\n4) Escuchas\n", ['1', '2', '3', '4'])
    if x=='1': print_most_streamed_musicians()
    elif x=='2': print_most_streamed_albums()
    elif x=='3': print_most_streamed_songs()
    else: print_most_streamed_listeners()
    print()