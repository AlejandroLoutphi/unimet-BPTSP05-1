#Universidad Metropolitana
#Proyecto: Metrotify
#Trimestre 2324-2
#Algoritmos y Programación (BPTSP05) Sección 1
#Alejandro Loutphi Trasande

#Este archivo contiene varias funciones misceláneas usadas en varias partes de la aplicación

import urllib.request
import json
import datetime
import random
import matplotlib.pyplot

def get_dict_from_urljson_qae(url: str) -> list:
    '''
    Devuelve una lista de diccionarios con los contenidos del archivo JSON en la URL especificada
    Si no se puede realizar la transacción, imprime el error correspondiente
    :param url: str con la URL del archivo JSON a cargar
    :return: list de diccionarios con los contenidos del JSON de la URL
    '''
    try:
        return json.loads(urllib.request.urlopen(url).read())
    except json.JSONDecodeError as e:
        print(e.msg)
    except urllib.error.URLError as e:
        print(e.reason)
    except urllib.error.HTTPError as e:
        print(str(e.code))
        print(e.read())
    except:
        print("Error al abrir o parsear página web")
    quit()

def input_list_element(prompt: str, options: list) -> str:
    '''
    Hace un input de tal manera de que solo se pueda devolver una de las opciones especificadas
    Admite respuestas en UPPERCASE o lowercase
    :param prompt: str con el texto conteniendo la pregunta que se le va a hacer al usuario
    :param options: list de str que contiene las únicas respuestas válidas a la pregunta. Todos los str deben ser lowercase
    :return: Un str contenido en la lista
    '''
    while True:
        x = input(prompt)
        x = x.lower()
        if x in options: return x
        print("Seleccione una de las opciones posibles")

def read_dict_from_file_or_website_qae(file_name: str, web_page: str) -> list:
    '''
    Convierte el JSON del archivo de nombre file_name a una lista de diccionarios.
    Si un no existe archivo con el nombre especificado, este se carga de la página web web_page
    :param file_name: Nombre del archivo a convertir a un diccionario
    :param web_page: URL de la página web de la cual cargar el archivo si el archivo con nombre file_name no existe
    '''
    while True:
        try: users_dict = json.load(open(file_name))
        except FileNotFoundError:
            json.dump(get_dict_from_urljson_qae(web_page), open(file_name, "w"))
            continue
        except json.decoder.JSONDecodeError:
            print("Error al parsear archivo de texto")
            quit()
        except:
            print("Error al abrir archivo de texto")
            quit()
        else: return users_dict

def iso_str_from_current_time() -> str:
    '''
    Retorna un str con el la fecha y el tiempo en el formato YYYY-MM-DDTHH-MM-ss.mmmZ
    '''
    return str(datetime.datetime.now().isoformat())[0:-3] + "Z"

def create_id() -> str:
    '''
    Returna un str con un ID en el formato xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    '''
    a = random.randbytes(4).hex()
    b = random.randbytes(2).hex()
    c = random.randbytes(2).hex()
    d = random.randbytes(2).hex()
    e = random.randbytes(6).hex()
    return a + "-" + b + "-" + c + "-" + d + "-"+ e

def matplotlib_barchart(names: list, values: list, title: str, ylabel: str):
    '''
    Hace un barchart en matplotlib.
    :param names: lista contieniendo los nombres de las barras
    :param values: lista conteniendo las alturas de las barras
    :param title: título del gráfico
    :param ylabel: etiqueta para el eje y
    '''
    matplotlib.pyplot.bar(names, values)
    matplotlib.pyplot.suptitle(title)
    matplotlib.pyplot.ylabel(ylabel)
    matplotlib.pyplot.show()