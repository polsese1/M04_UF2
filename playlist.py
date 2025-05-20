#!/usr/bin/env python3

import sys
import os
import base64
from bs4 import BeautifulSoup

ALBUMS_PATH = "albums/"
ARTISTS_PATH = "artists/"
GENRES_PATH = "genres/"
SONGS_PATH = "songs/"
COVERS_PATH = "albums/covers/"

albums = []
artists = []
genres = []
songs = []


def open_xml(file_path):
    with open(file_path, "r", encoding="utf-8") as file_xml:
        xml_content = BeautifulSoup(file_xml, "xml")
    return xml_content

def load_album(file_name):
    file_path = ALBUMS_PATH + file_name
    album_xml = open_xml(file_path)

    album_songs = []
    for song in album_xml.find_all("song"):
        album_song = {
            "id": song["id"],
            "title": song.text
        }
        album_songs.append(album_song)

    cover_filename = album_xml.cover.text
    cover_path = COVERS_PATH + cover_filename

    if os.path.exists(cover_path):
        with open(cover_path, "rb") as image_file:
            encoded_cover = base64.b64encode(image_file.read()).decode("utf-8")
    else:
        encoded_cover = None

    album = {
        "id": album_xml.album["id"],
        "titulo": album_xml.title.text,
        "songs": album_songs,
        "cover": encoded_cover
    }
    return album

def load_albums():
    global albums
    albums = []

    albums_dir = os.listdir(ALBUMS_PATH)
    albums_dir.sort()

    for album in albums_dir:
        if not album.endswith(".xml"):
            continue
        albums.append(load_album(album))
    return albums

def load_artist(file_name):
    file_path = ARTISTS_PATH + file_name
    artist_xml = open_xml(file_path)

    artist = {
		"id": artist_xml.artist["id"],
        "name": artist_xml.artist.find("name").text,
        "nationality": artist_xml.artist.find("nationality")["country"],
        "birthdate": artist_xml.artist.find("birthdate")["date"]
    }
    return artist

def load_artists():
    global artists
    artists = []

    artists_dir = os.listdir(ARTISTS_PATH)
    artists_dir.sort()

    for artist in artists_dir:
        if not artist.endswith(".xml"):
            continue
        artists.append(load_artist(artist))
    return artists

def load_song(file_name):
    file_path = SONGS_PATH + file_name
    song_xml = open_xml(file_path)

    song = {
        "id": song_xml.song["id"],
        "title": song_xml.title.text,
        "duration": song_xml.duration["second"],
        "artist": song_xml.artist.text
    }
    return song

def load_songs():
    global songs
    songs = []

    songs_dir = os.listdir(SONGS_PATH)
    songs_dir.sort()

    for song in songs_dir:
        if not song.endswith(".xml"):
            continue
        songs.append(load_song(song))
    return songs

def load_genre(file_name):
    file_path = GENRES_PATH + file_name
    genre_xml = open_xml(file_path)

    genre = {
        "id": genre_xml.genre["id"],
        "nombre": genre_xml.find("name").text,
        "descripcion": genre_xml.find("origin")["country"]
    }
    return genre

def load_genres():
    global genres
    genres = []

    genres_dir = os.listdir(GENRES_PATH)
    genres_dir.sort()

    for genre in genres_dir:
        if not genre.endswith(".xml"):
            continue
        genres.append(load_genre(genre))
    return genres


def menu():
    print(title)
    print("-" * len(title))
    print("1. Álbumes")
    print("2. Artistas")
    print("3. Canciones")
    print("4. Géneros")
    print("0. Salir")

    while True:
        opcion = input("Elige una opción del 0-4: ")
        match int(opcion):
            case 0:
                print("Saliendo...")
                break
            case 1:
                show_menu_albums()
            case 2:
                show_menu_artistas()
            case 3:
                show_menu_songs()
            case 4:
                show_menu_genres()
            case _:
                print("El número o carácter introducido no es correcto.")

def show_menu_albums():
    print("-----Álbumes-----")
    print("1. Listar todos los álbumes")
    print("2. Buscar álbum por título")
    print("0. Volver")

    while True:
        opcion = input("Elige una opción del 0-2: ")
        if opcion == "0":
            print("Volviendo al menú principal...")
            break
        elif opcion == "1":
            print("Mostrando todos los albumes...")
            load_albums()
            for album in albums:
                print(f"{album['id']} - {album['titulo']}")
        elif opcion == "2":
            nombre_album = input("Introduce el nombre del álbum que deseas buscar: ")
            load_albums()
            encontrados = [a for a in albums if nombre_album.lower() in a['titulo'].lower()]
            for album in encontrados:
                print(f"{album['id']} - {album['titulo']}")
        else:
            print("El numero o caracter introducido no es correcto.")

def show_menu_artistas():
    print("-----Artistas-----")
    print("1. Listar todos los artistas")
    print("2. Buscar artista por nombre")
    print("0. Volver")

    while True:
        opcion = input("Elige una opción del 0-2: ")
        if opcion == "0":
            print("Volviendo al menú principal...")
            break
        elif opcion == "1":
            print("Mostrando todos los artistas...")
            load_artists()
            for artist in artists:
                print(f"{artist['id']} - {artist['name']} ({artist['nationality']})")
        elif opcion == "2":
            nombre_artista = input("Introduce el nombre del artista que deseas buscar: ")
            load_artists()
            encontrados = [a for a in artists if nombre_artista.lower() in a['name'].lower()]
            for artist in encontrados:
                print(f"{artist['id']} - {artist['name']} ({artist['nationality']})")
        else:
            print("El numero o caracter introducido no es correcto.")

def show_menu_songs():
    print("-----Canciones-----")
    print("1. Listar todas las canciones")
    print("2. Buscar canción por título")
    print("0. Volver")

    while True:
        opcion = input("Elige una opción del 0-2: ")
        if opcion == "0":
            print("Volviendo al menú principal...")
            break
        elif opcion == "1":
            print("Mostrando todas las canciones...")
            load_songs()
            for song in songs:
                print(f"{song['id']} - {song['title']} ({song['duration']}) - {song['artist']}")
        elif opcion == "2":
            titulo_cancion = input("Introduce el título de la canción que deseas buscar: ")
            load_songs()
            encontrados = [s for s in songs if titulo_cancion.lower() in s['title'].lower()]
            for song in encontrados:
                print(f"{song['id']} - {song['title']} ({song['duration']}) [{song['genre']}] - {song['artist']}")
        else:
            print("El número o carácter introducido no es correcto.")

def show_menu_genres():
    print("-----Géneros-----")
    print("1. Listar todos los géneros")
    print("2. Buscar género por nombre")
    print("0. Volver")

    while True:
        opcion = input("Elige una opción del 0-2: ")
        if opcion == "0":
            print("Volviendo al menú principal...")
            break
        elif opcion == "1":
            print("Mostrando todos los géneros...")
            load_genres()
            for genre in genres:
                print(f"{genre['id']} - {genre['nombre']}: {genre['descripcion']}")
        elif opcion == "2":
            nombre_genero = input("Introduce el nombre del género que deseas buscar: ")
            load_genres()
            encontrados = [g for g in genres if nombre_genero.lower() in g['nombre'].lower()]
            for genre in encontrados:
                print(f"{genre['id']} - {genre['nombre']}: {genre['descripcion']}")
        else:
            print("El número o carácter introducido no es correcto.")


version = 0.5
title = "Playlist v" + str(version)

menu()

