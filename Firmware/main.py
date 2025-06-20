import board
# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.handlers.sequences import send_string
from kmk.extensions.rgb import RGB


keyboard = KMKKeyboard()


macros = Macros()
keyboard.modules.append(macros)

PINS = [
    board.GP1,  # SW1 - Top Left (Microsoft Edge)
    board.GP2,  # SW2 - Top Right (Insert key)
    board.GP4,  # SW3 - Bottom Left (TickTick)
    board.GP3   # SW4 - Bottom Right (OneCommander)
]

# Add RGB support for SK6812MINI LEDs
rgb = RGB(
    pixel_pin=board.GP0,  # Data pin for RGB LEDs
    num_pixels=2,         # Number of SK6812MINI LEDs from your PCB
    rgb_order=(1, 0, 2),  # GRB order for SK6812MINI
    hue_default=100,
    sat_default=255,
    val_default=30,
    animation_mode='rainbow',
)
keyboard.extensions.append(rgb)

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Define custom macros for launching applications
EDGE_MACRO = KC.MACRO(
    Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),  # Open Run dialog
    KC.MACRO_SLEEP_MS(200),  # Wait for dialog to open
    send_string("msedge"),   # Type Edge executable name
    Tap(KC.ENTER)            # Press Enter to launch
)

TICKTICK_MACRO = KC.MACRO(
    Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),  # Open Run dialog
    KC.MACRO_SLEEP_MS(200),  # Wait for dialog to open
    send_string("ticktick"),  # Type TickTick executable name
    Tap(KC.ENTER)             # Press Enter to launch
)

ONECOMMANDER_MACRO = KC.MACRO(
    Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),  # Open Run dialog
    KC.MACRO_SLEEP_MS(200),  # Wait for dialog to open
    send_string("OneCommander"),  # Type OneCommander executable name
    Tap(KC.ENTER)                 # Press Enter to launch
)

keyboard.keymap = [
    [
        EDGE_MACRO,        # SW1 (Top Left) - Open Microsoft Edge
        KC.INSERT,         # SW2 (Top Right) - Insert key
        TICKTICK_MACRO,    # SW3 (Bottom Left) - Open TickTick
        ONECOMMANDER_MACRO # SW4 (Bottom Right) - Open OneCommander
    ]
]

# Enable debug output
keyboard.debug_enabled = True

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
