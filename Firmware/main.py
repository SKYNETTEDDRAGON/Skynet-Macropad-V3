# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D7, board.D6, board.D3, board.D4, board.D2, board.D1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.Macro(Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)), 
     KC.Macro(Press(KC.LCMD), Tap(KC.Z), Release(KC.LCMD)),
     KC.Macro(Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)), 
     KC.Macro(Press(KC.ALT), Tap(KC.TAB), Release(KC.ALT)), 
     KC.Macro(Press(KC.LCMD), Tap(KC.T), Release(KC.LCMD)),
     KC.Macro(Press(KC.LCMD), Tap(KC.W), Release(KC.LCMD))]
]
 


# Start kmk!
if __name__ == '__main__':
    keyboard.go()