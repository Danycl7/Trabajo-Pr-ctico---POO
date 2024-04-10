import pygame


class Usuario:

    def __init__(self, name: str, email: str, occupation: str, age: int, country: str):
        self.name = name
        self.email = email
        self.occupation = occupation
        self.age = age
        self.country = country

    def __str__(self):
        return f"Nombre: {self.name}\nCorreo: {self.email}\nOcupación: {self.occupation}\nEdad: {self.age}\
        \nPaís de orígen: {self.country}"


def create_user():
    name = input("Ingrese su nombre: ")
    email = input("Ingrese su correo: ")
    occupation = input("Ingrese su ocupación: ")
    age = int(input("Ingrese su edad: "))
    country = input("Ingrese su país de orígen: ")
    return Usuario(name, email, occupation, age, country)


User = create_user()


class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.volume: float = 1
        pygame.mixer.music.set_volume(self.volume)
        self.playlist: list[str] = []

    def set_volume(self, volume: float):
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)

    def queue(self, file_path: str):
        self.playlist.append(file_path)

    def next(self):
        if self.playlist:
            next_song: str = self.playlist.pop(0)
            pygame.mixer.music.load(next_song)
            pygame.mixer.music.play()
        else:
            print("No hay canciones en la cola")


def console_input(audio_player: AudioPlayer):
    while True:
        command: str = input()
        if command.startswith('play'):
            _, file_path = command.split(maxsplit=1)
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        elif command.startswith('volume '):
            _, volume = command.split(maxsplit=1)
            if float(volume) < 0 or float(volume) > 1:
                print("El volumen debe ser un valor entre 0 y 1")
            else:
                audio_player.set_volume(float(volume))
        elif command == 'user_info':
            print(User)
        elif command == 'pause':
            pygame.mixer.music.pause()
        elif command == 'unpause':
            pygame.mixer.music.unpause()
        elif command == 'stop':
            pygame.mixer.music.fadeout(400)
        elif command == 'rewind':
            pygame.mixer.music.rewind()
        elif command.startswith('queue'):
            _, file_path = command.split(maxsplit=1)
            audio_player.queue(file_path)
        elif command == 'next':
            audio_player.next()
        elif command == 'exit':
            break
        else:
            print("Comando no reconocido")


def print_menu():
    print(f"\nHola {User.name}, Bienvenido al reproductor de audio")
    print("Opciones disponibles:\n")
    print("- user_info: Ver información del usuario")
    print("- play <file_path>: Reproducir un archivo de audio")
    print("- volume <volume>: Cambiar el volumen del reproductor")
    print("- pause: Pausar la reproducción")
    print("- unpause: Reanudar la reproducción")
    print("- stop: Detener la reproducción")
    print("- rewind: Reiniciar la reproducción")
    print("- queue <file_path>: Agregar un archivo a la cola de reproducción")
    print("- next: Reproducir el siguiente archivo en la cola")
    print("- exit: Salir del reproductor")
