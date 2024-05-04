import pygame


class Usuario:

    def __init__(self, name: str, email: str, occupation: str, age: int, country: str):
        self.name = name
        self.email = email
        self.occupation = occupation
        self.age = age
        self.country = country

    def create_user(self):
        self.name = input('Ingrese su nombre: ')
        self.email = input('Ingrese su correo: ')
        self.occupation = input('Ingrese su ocupación: ')
        self.country = input('Ingrese su país de orígen: ')

        while True:
            try:
                self.age = int(input('Ingrese su edad: '))
                if self.age < 0:
                    print('La edad no puede ser un número negativo')
                else:
                    break
            except ValueError:
                print('La edad debe ser un número entero válido')
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
    def __init__(self, playlistname: str, playlist: list[Song]):
        self.playlistname = playlistname
        self.playlist = playlist

    def create_playlist(self):
        self.playlistname = input('Ingrese el nombre de la playlist: ')
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
            print(f'-{song.title}')

    def __str__(self):
        return f'Playlist: {self.playlist}'


class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1)
        self.volume: float = 1
        self.playlists: dict[str, Playlist] = {}
        self.queue: list[str] = []
        self.songs: list[Song] = [
            Song('Big Sur Moon', 'Artista 1', 'Género 1',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Big Sur Moon.mp3'),
            Song('Billie Jean', 'Artista 2', 'Género 2',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Billie Jean.mp3'),
            Song('Elixer', 'Artista 3', 'Género 3',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Elixer.mp3'),
            Song('Guitar', 'Artista 4', 'Género 4',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Guitar.mp3'),
            Song('Get Lucky', 'Artista 5', 'Género 5',
                 r'C:\Users\Tomas\PycharmProjects\Trabajo-Pr-ctico---POO\sistema_musica\assets\Get Lucky.mp3'),
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
        self.playlists[playlist.playlistname] = playlist.create_playlist()

    def add_to_playlist(self, playlistname: str, song: Song):
        self.playlists[playlistname].add_song(song)

    def remove_from_playlist(self, playlistname: str, song: Song):
        self.playlists[playlistname].remove_song(song)

    def print_playlists(self):
        for playlist_name, playlist in self.playlists.items():
            print(f'Playlist: {playlist_name}')
            playlist.print_songs()


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
        elif command == 'exit':
            exit()
        else:
            print("Comando no reconocido")
