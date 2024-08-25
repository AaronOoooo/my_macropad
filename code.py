from adafruit_macropad import MacroPad
import time

macropad = MacroPad()

# Define the keyboard shortcut for launching Chrome
# (Windows Key + R, then type 'chrome' and Enter)
def launch_chrome():
    macropad.keyboard.press(macropad.Keycode.WINDOWS, macropad.Keycode.R)
    macropad.keyboard.release_all()
    time.sleep(0.5)  # Small delay to let the Run dialog open
    macropad.keyboard_layout.write('chrome\n')

while True:
    key_event = macropad.keys.events.get()

    if key_event and key_event.pressed:
        if key_event.key_number == 0:  # Button 1 is at index 0
            launch_chrome()

    time.sleep(0.1)  # Small delay to debounce
