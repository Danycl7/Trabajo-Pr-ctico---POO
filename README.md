# SISTEMA DE MÚSICA

Este proyecto es un reproductor de audio que personaliza la experiencia musical del usuario,
ofreciendo funcionalidades que se adapten a sus gustos y preferencias. Utiliza la biblioteca `pygame` para la reproducción de audio y la biblioteca `threading` para manejar la entrada del usuario en un hilo separado.

## Funcionalidades

- Reproducción de archivos de audio
- Control de volumen
- Pausa, reanudación y detención de la reproducción
- Retroceso de la reproducción
- Cola de reproducción
- Información del usuario

## Cómo usar

1. Inicie el programa en `sistema_musica\sys_music\app.py`. Se le pedirá que ingrese su información de usuario.
2. Se mostrará un menú con las opciones disponibles. Puede ingresar los siguientes comandos:
   - `user_info`: Ver información del usuario
   - `play <file_path>`: Reproducir un archivo de audio
   - `volume <volume>`: Cambiar el volumen del reproductor
   - `pause`: Pausar la reproducción
   - `unpause`: Reanudar la reproducción
   - `stop`: Detener la reproducción
   - `rewind`: Reiniciar la reproducción
   - `queue <file_path>`: Agregar un archivo a la cola de reproducción
   - `next`: Reproducir el siguiente archivo en la cola
   - `exit`: Salir del reproductor
  
Puedes encontrar música de prueba en el directorio `sistema_musica/assets`

## Dependencias

Este proyecto depende de las siguientes bibliotecas de Python:

- `pygame`
- `threading`

## Instalación

Para instalar las dependencias, puede usar pip:

```bash
pip install pygame
```

## Ejecución

Para ejecutar el programa, simplemente ejecúte el script `model1.py` en su entorno Python:

```bash
python model1.py
```
