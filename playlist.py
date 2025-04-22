#!/usr/bin/python3

from bs4 import BeautifulSoup

def show_menu():
        while True:
                print("Menu")
                print("1. Albums")
                print("2. Artists")
                print("3. Songs")
                print("4. Genres")
                print("0. Exit")

                option = input("Escoge (0-4): ")

                if option.isdigit():
                        option = int(option)
                        if 0 <= option <= 4:
                                return option
                        else:
                                print("Ingresa un numero entre 0 y 4.")
                else:
                        print("Error, ingresa un numero valido.")

def show_menu_songs():
        print("Menu de canciones")
        print("1. Listar todas las canciones")
        print("2. Buscar cancion por titulo")
        print("0. Volver")

def show_menu_albums():
        print("Menu de albumes")
        print("1. Listar todos los albumes")
        print("2. Buscar album por titulo")
        print("0. Volver")

def show_menu_artists():
        print("Menu de artistas")
        print("1. Listar todos los artistas")
        print("2. Buscar artista por titulo")
        print("0. Volver")

def show_menu_genres():
        print("Menu de generos")
        print("1. Listar todos los generos")
        print("2. Buscar genero por titulo")
        print("0. Volver")

version = 0.5

app_title="Playlist v" + str(version)

print(app_title)
print("-" * len(app_title))

song_xml = open("songs/song1.xml", "r").read()

song = BeautifulSoup(song_xml, 'xml')

print(song.title.text)
print(int(song.duration["second"])/60)

print(song.artists.find("artist"))

for artist in song.artists.find("artist"):
    print(artist.text)

option = show_menu()
print("Escoge:", option)

show_menu_songs()
show_menu_albums()
show_menu_artists()
show_menu_genres()
