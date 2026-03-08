"""Support for YNDX-00530 dimmer."""

from typing import Any, Final

from zigpy.quirks import CustomCluster
from zigpy.quirks.v2 import QuirkBuilder
from zigpy.zcl.foundation import (
    BaseAttributeDefs,
    BaseCommandDefs,
    Direction,
    ZCLAttributeDef,
    ZCLCommandDef,
)

from zhaquirks.yandex import (
    YANDEX,
    YANDEX_MANUFACTURER_CODE_1,
    YandexType_ButtonMode,
    YandexType_LedIndicator,
)


class YandexSwitchClusterDimmer(CustomCluster):
    """Yandex switch cluster for the YNDX-00530 dimmer."""

    cluster_id = 0xFC03
    manufacturer_id_override = YANDEX_MANUFACTURER_CODE_1

    class AttributeDefs(BaseAttributeDefs):
        """Attribute definitions."""

        led_indicator: Final = ZCLAttributeDef(
            id=0x0005,
            type=YandexType_LedIndicator,
            access="rw",
        )
        button_mode: Final = ZCLAttributeDef(
            id=0x0008,
            type=YandexType_ButtonMode,
            access="rw",
        )

    class ServerCommandDefs(BaseCommandDefs):
        """Server command definitions."""

        button_mode: Final = ZCLCommandDef(
            id=0x08,
            schema={"value": YandexType_ButtonMode},
            direction=Direction.Client_to_Server,
            is_manufacturer_specific=True,
        )

    async def write_attributes(
        self, attributes: dict[str | int, Any], manufacturer: int | None = None
    ) -> list:
        """Write attributes using commands because manufacturer-specific attribute writing is unsupported by Yandex devices."""

        result = []
        remaining_attributes = attributes.copy()

        if "button_mode" in attributes:
            remaining_attributes.pop("button_mode")
            result += await self.command(0x08, attributes.get("button_mode"))
        if 0x0008 in attributes:
            remaining_attributes.pop(0x0008)
            result += await self.command(0x08, attributes.get(0x0008))

        if remaining_attributes:
            result += await super().write_attributes(remaining_attributes, manufacturer)

        return result


(
    QuirkBuilder(YANDEX, "YNDX-00530")
    .replaces(YandexSwitchClusterDimmer)
    .enum(
        attribute_name=YandexSwitchClusterDimmer.AttributeDefs.button_mode.name,
        enum_class=YandexType_ButtonMode,
        cluster_id=YandexSwitchClusterDimmer.cluster_id,
        translation_key="button_mode",
        fallback_name="Button Mode",
    )
    .switch(
        attribute_name=YandexSwitchClusterDimmer.AttributeDefs.led_indicator.name,
        cluster_id=YandexSwitchClusterDimmer.cluster_id,
        translation_key="led_indicator",
        fallback_name="LED Indicator",
        off_value=YandexType_LedIndicator.Disabled,
        on_value=YandexType_LedIndicator.Enabled,
    )
    .add_to_registry()
)
