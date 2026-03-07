"""Common code for Yandex devices."""

import zigpy.types as t

### CONSTANTS ###

YANDEX = "Yandex"
YANDEX_MANUFACTURER_CODE_2 = 0x132F


### TYPES ###


class YandexType_VelocityLift(t.enum16):
    """Curtain motor: velocity options."""

    Slow = 6
    Normal = 9
    Fast = 12
