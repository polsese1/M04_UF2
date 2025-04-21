#!/usr/bin/python3

from bs4 import BeautifulSoup
import os

version = 0.5
app_title = "Playlist v" + str(version)

print(app_title)
print("-" * len(app_title))


#FUNCIONES DE CARGA XML
def load_xml_file(filepath):
    try:
        with open(filepath, "r") as f:
            content = f.read()
            return BeautifulSoup(content, 'xml')
    except Exception as e:
        print(f"Error leyendo {filepath}: {e}")
        return None


#MENUS
def show_main_menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Albumes")
        print("2. Artistas")
        print("3. Canciones")
        print("4. Generos")
        print("0. Salir")

        try:
            option = int(input("Selecciona una opcion: "))
            if option in [0, 1, 2, 3, 4]:
                return option
            else:
                print("Opcion no valida.")
        except ValueError:
            print("Por favor, introduce un numero valido.")


def show_menu_songs():
    while True:
        print("\n--- Menu Canciones ---")
        print("1. Listar todas las canciones")
        print("2. Buscar cancion por titulo")
        print("0. Volver")
        try:
            option = int(input("Selecciona una opcion: "))
            if option in [0, 1, 2]:
                return option
            else:
                print("Opcion no valida.")
        except ValueError:
            print("Por favor, introduce un numero valido.")


def show_menu_albums():
    while True:
        print("\n--- Menu Albumes ---")
        print("1. Listar todos los albumes")
        print("2. Buscar album por titulo")
        print("0. Volver")
        try:
            option = int(input("Selecciona una opcion: "))
            if option in [0, 1, 2]:
                return option
            else:
                print("Opcion no valida.")
        except ValueError:
            print("Por favor, introduce un numero valido.")


def show_menu_artists():
    while True:
        print("\n--- Menu Artistas ---")
        print("1. Listar todos los artistas")
        print("2. Buscar artista por nombre")
        print("0. Volver")
        try:
            option = int(input("Selecciona una opcion: "))
            if option in [0, 1, 2]:
                return option
            else:
                print("Opcion no valida.")
        except ValueError:
            print("Por favor, introduce un numero valido.")


def show_menu_genres():
    while True:
        print("\n--- Menu Generos ---")
        print("1. Listar todos los generos")
        print("2. Buscar genero por nombre")
        print("0. Volver")
        try:
            option = int(input("Selecciona una opcion: "))
            if option in [0, 1, 2]:
                return option
            else:
                print("Opcion no valida.")
        except ValueError:
            print("Por favor, introduce un numero valido.")


#CANCIONES
def list_all_songs():
    print("\n Canciones disponibles:")
    for file in os.listdir("songs"):
        if file.endswith(".xml"):
            song = load_xml_file(os.path.join("songs", file))
            if song and song.title:
                print(f"- {song.title.text}")


def search_song_by_title():
    search = input(" Introduce el titulo de la cancion: ").lower()
    found = False
    for file in os.listdir("songs"):
        if file.endswith(".xml"):
            song = load_xml_file(os.path.join("songs", file))
            if song and song.title and search in song.title.text.lower():
                print(f"Cancion encontrada: {song.title.text}")
                found = True
    if not found:
        print("No se encontro ninguna cancion con ese titulo.")


#ALBUMES
def list_all_albums():
    print("\n Albumes disponibles:")
    for file in os.listdir("albums"):
        if file.endswith(".xml"):
            album = load_xml_file(os.path.join("albums", file))
            if album and album.title:
                print(f"- {album.title.text}")


def search_album_by_title():
    search = input("Introduce el título del album: ").lower()
    found = False
    for file in os.listdir("albums"):
        if file.endswith(".xml"):
            album = load_xml_file(os.path.join("albums", file))
            if album and album.title and search in album.title.text.lower():
                print(f" Album encontrado: {album.title.text}")
                found = True
    if not found:
        print("No se encontro ningun album con ese titulo.")


#ARTISTAS
def list_all_artists():
    print("\n Artistas disponibles:")
    for file in os.listdir("artists"):
        if file.endswith(".xml"):
            artist = load_xml_file(os.path.join("artists", file))
            if artist and artist.name:
                print(f"- {artist.name.text}")


def search_artist_by_name():
    search = input(" Introduce el nombre del artista: ").lower()
    found = False
    for file in os.listdir("artists"):
        if file.endswith(".xml"):
            artist = load_xml_file(os.path.join("artists", file))
            if artist and artist.name and search in artist.name.text.lower():
                print(f"Artista encontrado: {artist.name.text}")
                found = True
    if not found:
        print("No se encontro ningun artista con ese nombre.")


#GENEROS
def list_all_genres():
    print("\n Generos disponibles:")
    for file in os.listdir("genres"):
        if file.endswith(".xml"):
            genre = load_xml_file(os.path.join("genres", file))
            if genre and genre.name:
                print(f"- {genre.name.text}")


def search_genre_by_name():
    search = input(" Introduce el nombre del genero: ").lower()
    found = False
    for file in os.listdir("genres"):
        if file.endswith(".xml"):
            genre = load_xml_file(os.path.join("genres", file))
            if genre and genre.name and search in genre.name.text.lower():
                print(f"Genero encontrado: {genre.name.text}")
                found = True
    if not found:
        print("No se encontro ningun genero con ese nombre.")


# EJECUCION PRINCIPAL
if __name__ == "__main__":
    while True:
        option = show_main_menu()
        if option == 0:
            print("Saliendo del programa...")
            break
        elif option == 1:
            while True:
                album_option = show_menu_albums()
                if album_option == 0:
                    break
                elif album_option == 1:
                    list_all_albums()
                elif album_option == 2:
                    search_album_by_title()
        elif option == 2:
            while True:
                artist_option = show_menu_artists()
                if artist_option == 0:
                    break
                elif artist_option == 1:
                    list_all_artists()
                elif artist_option == 2:
                    search_artist_by_name()
        elif option == 3:
            while True:
                song_option = show_menu_songs()
                if song_option == 0:
                    break
                elif song_option == 1:
                    list_all_songs()
                elif song_option == 2:
                    search_song_by_title()
        elif option == 4:
            while True:
                genre_option = show_menu_genres()
                if genre_option == 0:
                    break
                elif genre_option == 1:
                    list_all_genres()
                elif genre_option == 2:
                    search_genre_by_name()

