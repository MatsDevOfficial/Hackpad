import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()
layers = Layers()
macros = Macros()
keyboard.modules = [layers, macros]

PINS = [board.D3, board.D4, board.D2, board.D1, board.D0, board.D5]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.F13,
        KC.F14,
        KC.F15,
        KC.F16,
        KC.F17,
        KC.TO(1)
    ],

    [
        KC.F13,
        KC.F14,
        KC.F15,
        KC.F16,
        KC.F17,
        KC.TO(2)
    ],

    [
        KC.F13,
        KC.F14,
        KC.F15,
        KC.F16,
        KC.F17,
        KC.TO(0)
    ],
]

if __name__ == '__main__':
    keyboard.go()
