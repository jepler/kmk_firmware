import board

from kmk.consts import DiodeOrientation
from kmk.mcus.circuitpython_usbhid import KeyboardConfig as _KeyboardConfig
from kmk.pins import Pin as P


class KeyboardConfig(_KeyboardConfig):
    col_pins = (P.SDA, P.A2, P.A3, P.A4, P.A5, P.SCK, P.MOSI)
    row_pins = (P.TX, P.A0, P.RX, P.A1, P.D11, P.D9, P.D12, P.D10)
    diode_orientation = DiodeOrientation.COLUMNS
    rgb_pixel_pin = board.D13