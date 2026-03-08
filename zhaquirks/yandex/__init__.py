"""Common code for Yandex devices."""

import zigpy.types as t

### CONSTANTS ###


YANDEX = "Yandex"
YANDEX_MANUFACTURER_CODE_1 = 0x140A
YANDEX_MANUFACTURER_CODE_2 = 0x132F


### TYPES ###


class YandexType_SwitchMode(t.enum8):
    """Wired switches: gang mode."""

    Control_Relay = 0x00
    Up_Decoupled = 0x01
    Decoupled = 0x02
    Down_Decoupled = 0x03


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


class YandexType_LedIndicator(t.basic.enum8):
    """Enable/disable LED indicator."""

    Enabled = 0
    Disabled = 1


class YandexType_Interlock(t.basic.enum8):
    """Dual relay only: enable/disable interlock mode."""

    Disabled = 0
    Enabled = 1


class YandexType_ButtonMode(t.enum8):
    """Dimmer only: button presses interpretation."""

    General = 0x00
    Alternative = 0x01


class YandexType_VelocityLift(t.enum16):
    """Curtain motor: velocity options."""

    Slow = 6
    Normal = 9
    Fast = 12
