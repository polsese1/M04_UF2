#!/usr/bin/env python3

import sys
import os

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
covers = []



def menu():
	print (title)
	print ("-"*len(title))
	print("1. Albumes")
	print("2. Artistas")
	print("3. Canciones")
	print("4. Género")
	print("0. Salir")

	while True:
		opcion = input("Elije una opcion del 0-4: ")
		match int(opcion):
			case 0:
				print("Saliendo...")
				break
			case 1:
				print ("Has selecionado la opcion "+str (opcion))
				show_menu_albums()
			case 2:
				print ("Has selecionado la opcion "+str (opcion))
				show_menu_artistas()
			case 3:
				print("Has selecionado la opcion "+str (opcion))
				show_menu_songs()
			case 4:
				print ("Has selecionado la opcion "+str (opcion))
				show_menu_genres()
			case _:
				print("El numero o caracter introducido no es correcto.")

def show_menu_songs():
		print("-----Canciones-----")
		print("1. Listar todas las canciones")
		print("2. Buscar cancion por titulo")
		print("0. Volver")
		
		while True:
			opcion = input("Elije una opcion del 0-2 ")
		
			if opcion == "0":
				print ("Volviendo al menu principal...")
				break
			elif opcion == "1":
				print ("Mostrando todas las canciones...")
			elif opcion == "2":
				print ("Introduce el titulo de la cancion que quieres buscar: ")
				titulo_cancion = input("")
				print (titulo_cancion)
			else:
				print("El numero o caracter introducido no es correcto.")

def show_menu_albums():
	print("-----Albumes-----")
	print ("1. Listar todos los albumes")
	print ("2. Buscar album por titulo")
	print ("0. Volver")
	
	while True:
	
		opcion = input("Elije una opcion del 0-2 ")
		if opcion == "0":
			print("Volviendo al menu prinipal...")
			break
		elif opcion == "1":
			print("Mostrando todos los albumes...")
			load_albums()
		elif opcion == "2":
			print ("Introduce el nombre del album que deseas buscar: ")
			nombre_album = input("")
			print (nombre_album)
		else:
			print("El numero o caracter introducido no es correcto.")



def show_menu_artistas():
	print("-----Artistas-----")
	print("1. Listar todos los artistas")
	print("2. Buscar artista por nombre")
	print("0. Volver")

	while True:
		opcion = input("Elije una opcion del 0-2 ")
		if opcion == "0":
			print("Volviendo al menu prinipal...")
			break
		elif opcion == "1":
			print("Mostrando todos los artistas...")
		elif opcion == "2":
			print ("Introduce el nombre del artista que deseas buscar: ")
			nombre_artista = input("")
			print (nombre_artista)
		else:
			print("El numero o caracter introducido no es correcto.")



def show_menu_genres():
	print("-----Genero-----")
	print("1. Listar todos los generos")
	print("2. Buscar genero por nombre")
	print("0. Volver.")
	
	while True:
		opcion = input("Elige una opción del 0-2: ")
		if opcion == "0":
			print("Volviendo al menu principal...")
			break
		elif opcion == "1":
			print ("Mostrando todos los generos...")
		elif opcion == "2":
			print ("Introduce el nombre del genero que quieres buscar: ")
			nombre_genero = input("")
			print (nombre_genero)
		else:
			print("El numero o caracter introducido no es correcto")

def open_xml(file_path):
    with open(file_path, "r", encoding="utf-8") as file_xml:
        album_xml = BeautifulSoup(file_xml, "xml") 

    return album_xml  

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

    album = {
        "id": album_xml.album["id"],
        "titulo": album_xml.title.text,
        "songs": album_songs, 
    }

    return album


def load_album_num (album_num):
	global ALBUMS_PATH

	file_name = "album"+str(album_num)+".xml"
	
	return load_album(file_name)
	
def load_albums():
    global ALBUMS_PATH
    global albums

    albums = [] 

    albums_dir = os.listdir(ALBUMS_PATH)
    albums_dir.sort() 

    for album in albums_dir:
        if not album.endswith(".xml"):
            continue

        albums.append(load_album(album))

    return albums
	

load_albums()
print (albums)


version = 0.5
title = "Playlist v"+str(version)

menu()

#xml_ejemplo = '<personaje><nombre>Jacinto</nombre><edad valor="33"/></personaje>'

#personaje = BeautifulSoup(xml_ejemplo, 'xml')

#print (personaje.prettify())

#nombre = (personaje.nombre)


#print(nombre.text)

#songs_xml_file = open("songs/song.xml", "r")

#song_xml = songs_xml_file.read()

#print (song_xml)

#song = BeautifulSoup(song_xml, 'xml')

#print (song.title.text)
#print (int(song.duration["seconds"])/60)
#for artists in song.artists.find("artista"):
#	print (artists.text)
