"""Common code for Yandex devices."""

import zigpy.types as t

### CONSTANTS ###

YANDEX = "Yandex"
YANDEX_MANUFACTURER_CODE_1 = 0x140A


### TYPES ###


class YandexType_LedIndicator(t.basic.enum8):
    """Enable/disable LED indicator."""

    Enabled = 0
    Disabled = 1


class YandexType_ButtonMode(t.enum8):
    """Dimmer only: button presses interpretation."""

    General = 0x00
    Alternative = 0x01
