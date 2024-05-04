import threading

from sistema_musica.sys_music.model.sys_music import AudioPlayer, console_input, start_menu

start_menu()

player = AudioPlayer()

console_thread = threading.Thread(target=console_input, args=(player,))
console_thread.start()
