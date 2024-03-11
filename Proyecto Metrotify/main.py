#Universidad Metropolitana
#Proyecto: Metrotify
#Trimestre 2324-2
#Algoritmos y Programación (BPTSP05) Sección 1
#Alejandro Loutphi Trasande

#Este es el archivo que se va a correr al iniciar la aplicación
#Contiene el proceso de login y sign up

from funcs import input_list_element
from usuarios import user_id_and_type_from_name
from usuarios import register_user
from menu import menu_escucha
from menu import menu_musico

def sign_up():
    '''
    Guía al usuario a insertar los parámetros para crear su usuario.
    Subsecuentemente corre menu_escucha() o menu_musico().
    '''
    logged_user_id, logged_user_type = register_user()
    if logged_user_type == 0: menu_escucha(logged_user_id)
    else: menu_musico(logged_user_id)

def login():
    '''
    Guía al usuario a hacer login al buscar su nombre en la lista de usuarios de users.txt.
    Subsecuentemente corre menu_escucha() o menu_musico().
    '''
    while True:
        x = input("Introduzca su nombre de usuario:\n")
        try: logged_user_id, logged_user_type = user_id_and_type_from_name(x)
        except: print("Introduzca un nombre válido")
        else: break
    if logged_user_type == 0: menu_escucha(logged_user_id)
    else: menu_musico(logged_user_id)

x = input_list_element("¿Qué quiere hacer?\n1) Login a usuario existente\n2) Registrarse como nuevo usuario\n", ['1','2'])
if x=='1': login()
else: sign_up()