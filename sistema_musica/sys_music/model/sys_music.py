import pygame
import random


class Usuario:

    def __init__(self, name: str, email: str, occupation: str, age: int, country: str):
        self.name = name
        self.email = email
        self.occupation = occupation
        self.age = age
        self.country = country

    def create_user(self):
        while True:
            self.name = input('Ingrese su nombre: ')
            if self.name.isalpha():
                break
            else:
                print('El nombre no puede contener números')

        while True:
            self.email = input('Ingrese su correo: ')
            if '@' in self.email and '.' in self.email:
                break
            else:
                print('El correo debe contener un "@" y un "."')

        while True:
            self.occupation = input('Ingrese su ocupación: ')
            if self.occupation.isalpha():
                break
            else:
                print('La ocupación no puede contener números')

        while True:
            self.country = input('Ingrese su país de orígen: ')
            if self.country.isalpha():
                break
            else:
                print('El país no puede contener números')

        while True:
            self.age = int(input('Ingrese su edad: '))
            if self.age > 0:
                break
            elif self.age > 100:
                print('Edad no válida')
            else:
                print('La edad no puede ser negativa')
        return self

    def __str__(self):
        return f'Nombre: {self.name}\nCorreo: {self.email}\nOcupación: {self.occupation}\nEdad: {self.age}\
        \nPaís de orígen: {self.country}'


class Song:
    def __init__(self, title: str, artist: str, genre: str, file_path: str):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.file_path = file_path

    def add_song(self):
        self.title = input('Ingrese el título de la canción: ')
        self.artist = input('Ingrese el artista de la canción: ')
        self.genre = input('Ingrese el género de la canción: ')
        self.file_path = input('Ingrese la ruta del archivo de la canción: ')
        print('Canción agregada con éxito')
        return self

    def __str__(self):
        return f'Título: {self.title}\nArtista: {self.artist}\nGénero: {self.genre}\n'


class Playlist:
    def __init__(self, playlist_name: str, playlist: list[Song]):
        self.playlist_name = playlist_name
        self.playlist = playlist

    def create_playlist(self):
        self.playlist_name = input('Ingrese el nombre de la playlist: ')
        return self

    def delete_playlist(self):
        self.playlist_name = input('Ingrese el nombre de la playlist a eliminar: ')
        return self

    def add_song(self, song: Song):
        if song not in self.playlist:
            self.playlist.append(song)
        else:
            print('La canción ya está en la playlist')

    def remove_song(self, song: Song):
        self.playlist.remove(song)

    def print_songs(self):
        for song in self.playlist:
            print(f'-{song.title} ({song.genre})')

    def __str__(self):
        return f'Playlist: {self.playlist}'


class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)
        self.volume: float = 0.5
        self.playlists: dict[str, Playlist] = {}
        self.queue: list[str] = []
        self.songs: list[Song] = [
            Song('bad guy', 'Billie Eilish', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Billie Eilish - bad guy.mp3'),
            Song('Kiss Me More', 'Doja Cat ft. SZA', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Doja Cat - Kiss Me More.mp3'),
            Song('Levitating', 'Dua Lipa', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Dua Lipa - Levitating.mp3'),
            Song('Shape of You', 'Ed Sheeran', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Ed Sheeran - Shape of You.mp3'),
            Song('As it was', 'Harry Styles', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Harry Styles - As It Was.mp3'),
            Song('Roar', 'Katy Perry', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Katy Perry - Roar.mp3'),
            Song('Bad Romance', 'Lady Gaga', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Lady Gaga - Bad Romance.mp3'),
            Song('Sugar', 'Maroon 5', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Maroon 5 - Sugar.mp3'),
            Song('Billie Jean', 'Michael Jackson', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Michael Jackson - Billie Jean.mp3'),
            Song('good 4 u', 'Olivia Rodrigo', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Olivia Rodrigo - good 4 u.mp3'),
            Song('Sunflower', 'Post Malone ft. Swae Lee', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Post Malone & Swae Lee - Sunflower.mp3'),
            Song('Bohemian Rhapsody', 'Queen', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Queen - Bohemian Rhapsody.mp3'),
            Song('Leave the Door Open', 'Silk Sonic', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Silk Sonic - Leave the Door Open.mp3'),
            Song('Blank Space', 'Taylor Swift', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Taylor Swift - Blank Space.mp3'),
            Song('Blinding Lights', 'The Weeknd', 'Pop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\The Weeknd - Blinding Lights.mp3'),
            Song('Back in Black', 'AC/DC', 'Rock',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\ACDC - Back in Black.mp3'),
            Song('Sweet Child O Mine', 'Guns N Roses', 'Rock',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Guns N Roses - Sweet Child o Mine.mp3'),
            Song('Smells Like Teen Spirit', 'Nirvana', 'Rock',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Nirvana - Smells Like Teen Spirit.mp3'),
            Song('Radioactive', 'Imagine Dragons', 'Rock',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Imagine Dragons - Radioactive.mp3'),
            Song('Everlong', 'Foo Fighters', 'Rock',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Foo Fighters - Everlong.mp3'),
            Song('In the End', 'Linkin Park', 'Rock',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Linkin Park - In the End.mp3'),
            Song('Stairway to Heaven', 'Led Zeppelin', 'Rock',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Led Zeppelin - Stairway to Heaven.mp3'),
            Song('Enter Sandman', 'Metallica', 'Rock',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Metallica - Enter Sandman.mp3'),
            Song('Hey Jude', 'The Beatles', 'Rock',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\The Beatles - Hey Jude.mp3'),
            Song('Wish You Were Here', 'Pink Floyd', 'Rock',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Pink Floyd - Wish You Were Here.mp3'),
            Song('One more time', 'Daft Punk', 'Electronica',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Daft Punk - One More Time.mp3'),
            Song('Feel so close', 'Calvin Harris', 'Electronica',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Calvin Harris - Feel So Close.mp3'),
            Song('Wake me up', 'Avicii', 'Electronica',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Avicii - Wake Me Up.mp3'),
            Song('Dont you worry child', 'Swedish House Mafia', 'Electronica',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Swedish House Mafia - Dont You Worry Child.mp3'),
            Song('Animals', 'Martin Garrix', 'Electronica',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Martin Garrix - Animals.mp3'),
            Song('Ghost n Stuff', 'Deadmau5', 'Electronica',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Deadmau5 - Ghosts n Stuff.mp3'),
            Song('D.A.N.C.E.', 'Justice', 'Electronica',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Justice - D.A.N.C.E..mp3'),
            Song('Galvanize', 'The Chemical Brothers', 'Electronica',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\The Chemical Brothers - Galvanize.mp3'),
            Song('HUMBLE.', 'Kendrick Lamar', 'Hip Hop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Kendrick Lamar - HUMBLE..mp3'),
            Song('Gods Plan', 'Drake', 'Hip Hop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Drake - Gods Plan.mp3'),
            Song('Stronger', 'Kanye West', 'Hip Hop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Kanye West - Stronger.mp3'),
            Song('Lose Yourself', 'Eminem', 'Hip Hop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Eminem - Lose Yourself.mp3'),
            Song('Empire State of Mind', 'Jay Z ft. Alicia', 'Hip Hop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Jay-Z - Empire State of Mind.mp3'),
            Song('Changes', '2Pac', 'Hip Hop',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Tupac Shakur - Changes.mp3'),
        ]

    def set_volume(self, volume: float):
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)
        print(f'Volumen cambiado a {int(self.volume*100)}%')

    def add_queue(self, file_path: str):
        self.queue.append(file_path)

    def next(self):
        if self.queue:
            next_song: str = self.queue.pop(0)
            pygame.mixer.music.load(next_song)
            pygame.mixer.music.play()
        else:
            print('No hay canciones en la cola')

    def new_playlist(self):
        playlist = Playlist('', [])
        self.playlists[playlist.playlist_name] = playlist.create_playlist()

    def delete_playlist(self):
        playlist_name = input('Ingrese el nombre de la playlist a eliminar: ')
        if playlist_name in self.playlists:
            del self.playlists[playlist_name]
            print('Playlist eliminada con éxito')
        else:
            print('Playlist no encontrada')

    def rename_playlist(self):
        playlist_name = input('Ingrese el nombre de la playlist a renombrar: ')
        if playlist_name in self.playlists:
            new_name = input('Ingrese el nuevo nombre de la playlist: ')
            self.playlists[new_name] = self.playlists.pop(playlist_name)
            print('Playlist renombrada con éxito')
        else:
            print('Playlist no encontrada')

    def add_to_playlist(self, playlist_name: str, song: Song):
        self.playlists[playlist_name].add_song(song)

    def remove_from_playlist(self, playlist_name: str, song: Song):
        self.playlists[playlist_name].remove_song(song)

    def print_playlists(self):
        for playlist_name, playlist in self.playlists.items():
            print(f'Playlist: {playlist_name}')
            playlist.print_songs()
            print("\n")

    def recommend_playlist(self, reference_playlist_name: str):
        if reference_playlist_name not in self.playlists:
            print("Playlist de referencia no encontrada")
            return

        reference_playlist = self.playlists[reference_playlist_name]
        if len(reference_playlist.playlist) < 5:
            print("La playlist de referencia no tiene suficientes canciones")
            return

        reference_songs = random.sample(reference_playlist.playlist, 5)
        reference_genres = {song.genre for song in reference_songs}

        recommended_songs = [song for song in self.songs if
                             song.genre in reference_genres and song.title not in {song.title for song in
                                                                                   reference_songs}]

        if len(recommended_songs) < 5:
            print("No hay suficientes canciones para generar una playlist recomendada")
            return

        playlist_name = "Recommended Playlist"
        i = 1
        while playlist_name in self.playlists:
            playlist_name = f"Recommended Playlist {i}"
            i += 1

        selected_songs = random.sample(recommended_songs, 5)

        recommended_playlist = Playlist(playlist_name, selected_songs)
        self.playlists[recommended_playlist.playlist_name] = recommended_playlist

        print(f"Playlist recomendada '{recommended_playlist.playlist_name}' creada con éxito, Generos: {reference_genres}")

    def random_playlist(self):
        if len(self.songs) < 5:
            print("No hay suficientes canciones para generar una playlist aleatoria")
            return

        playlist_name = "Random Playlist"
        i = 1
        while playlist_name in self.playlists:
            playlist_name = f"Random Playlist {i}"
            i += 1

        random_playlist = Playlist(playlist_name, random.sample(self.songs, 5))
        self.playlists[random_playlist.playlist_name] = random_playlist

        print(f"Playlist aleatoria '{random_playlist.playlist_name}' creada con éxito")

    def random_song(self):
        random_song = random.choice(self.songs)
        print(f"Reproduciendo {random_song.title}")
        pygame.mixer.music.load(random_song.file_path)
        pygame.mixer.music.play()


def start_menu():
    print('Bienvenido al reproductor de música')
    print('1. Iniciar sesión')
    print('2. Salir')
    option = input('Ingrese una opción: ')
    if option == '1':
        console_input(AudioPlayer())
    elif option == '2':
        exit()
    else:
        print('Opción no válida')
        start_menu()


def print_menu():
    user = Usuario('', '', '', 0, "").create_user()
    print(f"\nHola {user.name}, Bienvenido.")
    print("Opciones disponibles:\n")
    print("user info - Ver información del usuario")
    print("add song - Agregar una canción")
    print("songs - Ver lista de canciones")
    print("play <nombre de la canción> - Reproducir una canción")
    print("pause - Pausar la canción actual")
    print("unpause - Reanudar la canción actual")
    print("stop - Detener la canción actual")
    print("rewind - Retroceder la canción actual")
    print("queue <nombre de la canción> - Agregar una canción a la cola")
    print("next - Reproducir la siguiente canción en la cola")
    print("volume <número> - Cambiar el volumen")
    print("new playlist - Crear una nueva playlist")
    print("delete playlist - Eliminar una playlist")
    print("rename playlist - Renombrar una playlist")
    print("show playlists - Ver lista de playlists")
    print("add to playlist - Agregar una canción a una playlist")
    print("remove from playlist - Remover una canción de una playlist")
    print("start playlist - Reproducir una playlist")
    print("random playlist - Crear una playlist aleatoria")
    print("random song - Reproducir una canción aleatoria")
    print("recommend playlist - Crear una playlist recomendada")
    print("exit - Salir del reproductor de audio\n")
    return user


def console_input(audio_player: AudioPlayer):
    user = print_menu()
    while True:
        command: str = input().lower()
        if command == 'user info'.lower():
            print(user)
        elif command == 'add song':
            audio_player.songs.append(Song("", "", "", "").add_song())
        elif command == 'songs':
            if not audio_player.songs:
                print("No hay canciones en la lista")
            else:
                for song in audio_player.songs:
                    print(song)
        elif command.startswith('play'):
            _, song_name = command.split(maxsplit=1)
            for song in audio_player.songs:
                if song.title.lower() == song_name.lower():
                    pygame.mixer.music.load(song.file_path)
                    pygame.mixer.music.play()
                    break
            else:
                print("Canción no encontrada")
        elif command == 'pause':
            pygame.mixer.music.pause()
        elif command == 'unpause':
            pygame.mixer.music.unpause()
        elif command == 'stop':
            pygame.mixer.music.fadeout(400)
        elif command == 'rewind':
            pygame.mixer.music.rewind()
        elif command.startswith('queue'):
            _, song_name = command.split(maxsplit=1)
            for song in audio_player.songs:
                if song.title == song_name:
                    audio_player.add_queue(song.file_path)
                    print(f"{song.title} agregada a la cola")
                    break
            else:
                print("Canción no encontrada")
        elif command == 'next':
            audio_player.next()
        elif command.startswith('volume'):
            _, volume = command.split(maxsplit=1)
            if 0 < float(volume) < 100:
                audio_player.set_volume(float(volume)/100)
            else:
                print("El volumen debe estar entre 0 y 100")
        elif command == 'new playlist':
            audio_player.new_playlist()
            print("Playlist creada con éxito")
        elif command == 'show playlists':
            if not audio_player.playlists:
                print("No hay playlists")
            else:
                audio_player.print_playlists()
        elif command == 'add to playlist':
            playlistname = input("Ingrese el nombre de la playlist: ")
            if playlistname not in audio_player.playlists:
                print("Playlist no encontrada")
            else:
                songname = input("Ingrese el nombre de la canción: ")
                for song in audio_player.songs:
                    if song.title.lower() == songname.lower():
                        audio_player.add_to_playlist(playlistname, song)
                        print(f"{song.title} agregada a la playlist {playlistname}")
                        break
                else:
                    print("Canción no encontrada")
        elif command == 'remove from playlist':
            playlistname = input("Ingrese el nombre de la playlist: ")
            if playlistname not in audio_player.playlists:
                print("Playlist no encontrada")
            else:
                songname = input("Ingrese el nombre de la canción: ")
                for song in audio_player.songs:
                    if song.title.lower() == songname.lower():
                        audio_player.remove_from_playlist(playlistname, song)
                        print(f"{song.title} removida de la playlist {playlistname}")
                        break
                else:
                    print("Canción no encontrada")
        elif command == 'start playlist':
            playlistname = input("Ingrese el nombre de la playlist: ")
            if playlistname in audio_player.playlists:
                songs = audio_player.playlists[playlistname].playlist
                if songs:
                    first_song = songs[0]
                    print(f"Reproduciendo {first_song.title}")
                    pygame.mixer.music.load(first_song.file_path)
                    pygame.mixer.music.play()
                    for song in songs[1:]:
                        audio_player.add_queue(song.file_path)
            else:
                print("Playlist no encontrada")
        elif command == 'random playlist':
            audio_player.random_playlist()
        elif command == 'recommend playlist':
            playlistname = input("Ingrese el nombre de la playlist de referencia: ")
            audio_player.recommend_playlist(playlistname)
        elif command == 'delete playlist':
            audio_player.delete_playlist()
        elif command == 'random song':
            audio_player.random_song()
        elif command == 'rename playlist':
            audio_player.rename_playlist()
        elif command == 'exit':
            exit()
        else:
            print("Comando no reconocido")
