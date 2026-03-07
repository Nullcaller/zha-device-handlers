"""Common code for Yandex devices."""

import zigpy.types as t

### CONSTANTS ###

YANDEX = "Yandex"
YANDEX_MANUFACTURER_CODE_1 = 0x140A


### TYPES ###


class YandexType_SwitchType(t.enum8):
    """Relays: connected switch type."""

    Rocker = 0x00
    Button = 0x01
    Decoupled = 0x02


class YandexType_PowerType(t.enum8):
    """Wired devices: power level."""

    High = 0x00
    Medium = 0x01
    Low = 0x02


class YandexType_Interlock(t.basic.enum8):
    """Dual relay only: enable/disable interlock mode."""

    Disabled = 0
    Enabled = 1
