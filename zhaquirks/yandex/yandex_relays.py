"""Support for YNDX-00537 and YNDX-00538 single-channel and dual-channel relays."""

from typing import Any, Final

from zigpy.profiles import zha
from zigpy.quirks import CustomCluster
from zigpy.quirks.v2 import QuirkBuilder
from zigpy.zcl import ClusterType
from zigpy.zcl.clusters.general import Basic, Identify, OnOff
from zigpy.zcl.foundation import (
    BaseAttributeDefs,
    BaseCommandDefs,
    Direction,
    ZCLAttributeDef,
    ZCLCommandDef,
)

from zhaquirks.const import (
    CLUSTER_ID,
    COMMAND,
    COMMAND_OFF,
    COMMAND_ON,
    COMMAND_TOGGLE,
    DOUBLE_PRESS,
    ENDPOINT_ID,
    LONG_PRESS,
    SHORT_PRESS,
)
from zhaquirks.yandex import (
    YANDEX,
    YANDEX_MANUFACTURER_CODE_1,
    YandexType_Interlock,
    YandexType_PowerType,
    YandexType_SwitchType,
)


class YandexSwitchClusterRelay(CustomCluster):
    """Yandex switch cluster for YNDX-00537, YNDX-00538 relays."""

    cluster_id = 0xFC03
    manufacturer_id_override = YANDEX_MANUFACTURER_CODE_1

    class AttributeDefs(BaseAttributeDefs):
        """Attribute definitions."""

        switch_type: Final = ZCLAttributeDef(
            id=0x0002,
            type=YandexType_SwitchType,
            access="rw",
        )
        power_type: Final = ZCLAttributeDef(
            id=0x0003,
            type=YandexType_PowerType,
            access="rw",
        )
        interlock: Final = ZCLAttributeDef(
            id=0x0007,
            type=YandexType_Interlock,
            access="rw",
        )

    class ServerCommandDefs(BaseCommandDefs):
        """Server command definitions."""

        switch_type: Final = ZCLCommandDef(
            id=0x02,
            schema={"value": YandexType_SwitchType},
            direction=Direction.Client_to_Server,
            is_manufacturer_specific=True,
        )
        power_type: Final = ZCLCommandDef(
            id=0x03,
            schema={"value": YandexType_PowerType},
            direction=Direction.Client_to_Server,
            is_manufacturer_specific=True,
        )
        interlock: Final = ZCLCommandDef(
            id=0x07,
            schema={"value": YandexType_Interlock},
            direction=Direction.Client_to_Server,
            is_manufacturer_specific=True,
        )

    async def write_attributes(
        self, attributes: dict[str | int, Any], manufacturer: int | None = None
    ) -> list:
        """Write attributes using commands because manufacturer-specific attribute writing is unsupported by Yandex devices."""

        result = []
        remaining_attributes = attributes.copy()

        if "switch_type" in attributes:
            remaining_attributes.pop("switch_type")
            result += await self.command(0x02, attributes.get("switch_type"))
        if 0x0002 in attributes:
            remaining_attributes.pop(0x0002)
            result += await self.command(0x02, attributes.get(0x0002))
        if "power_type" in attributes:
            remaining_attributes.pop("power_type")
            result += await self.command(0x03, attributes.get("power_type"))
        if 0x0003 in attributes:
            remaining_attributes.pop(0x0003)
            result += await self.command(0x03, attributes.get(0x0003))
        if "interlock" in attributes:
            remaining_attributes.pop("interlock")
            result += await self.command(0x07, attributes.get("interlock"))
        if 0x0007 in attributes:
            remaining_attributes.pop(0x0007)
            result += await self.command(0x07, attributes.get(0x0007))

        if remaining_attributes:
            result += await super().write_attributes(remaining_attributes, manufacturer)

        return result


(
    QuirkBuilder(YANDEX, "YNDX-00537")
    .replaces(YandexSwitchClusterRelay, endpoint_id=1)
    .adds_endpoint(
        endpoint_id=2,
        profile_id=zha.PROFILE_ID,
        device_type=zha.DeviceType.ON_OFF_LIGHT_SWITCH,
    )
    .adds(Basic, endpoint_id=2, cluster_type=ClusterType.Server)
    .adds(Identify, endpoint_id=2, cluster_type=ClusterType.Server)
    .adds(Identify, endpoint_id=2, cluster_type=ClusterType.Client)
    .adds(OnOff, endpoint_id=2, cluster_type=ClusterType.Client)
    .device_automation_triggers(
        {
            (SHORT_PRESS, "Button"): {
                COMMAND: COMMAND_TOGGLE,
                CLUSTER_ID: OnOff.cluster_id,
                ENDPOINT_ID: 2,
            },
            (DOUBLE_PRESS, "Button"): {
                COMMAND: COMMAND_ON,
                CLUSTER_ID: OnOff.cluster_id,
                ENDPOINT_ID: 2,
            },
            (LONG_PRESS, "Button"): {
                COMMAND: COMMAND_OFF,
                CLUSTER_ID: OnOff.cluster_id,
                ENDPOINT_ID: 2,
            },
        }
    )
    .enum(
        attribute_name=YandexSwitchClusterRelay.AttributeDefs.power_type.name,
        enum_class=YandexType_PowerType,
        cluster_id=YandexSwitchClusterRelay.cluster_id,
        translation_key="power_type",
        fallback_name="Power Type",
    )
    .enum(
        attribute_name=YandexSwitchClusterRelay.AttributeDefs.switch_type.name,
        enum_class=YandexType_SwitchType,
        cluster_id=YandexSwitchClusterRelay.cluster_id,
        translation_key="switch_type",
        fallback_name="Switch Type",
    )
    .add_to_registry()
)

(
    QuirkBuilder(YANDEX, "YNDX-00538")
    .replaces(YandexSwitchClusterRelay, endpoint_id=1)
    .replaces(YandexSwitchClusterRelay, endpoint_id=2)
    .adds_endpoint(
        endpoint_id=3,
        profile_id=zha.PROFILE_ID,
        device_type=zha.DeviceType.ON_OFF_LIGHT_SWITCH,
    )
    .adds(Basic, endpoint_id=3, cluster_type=ClusterType.Server)
    .adds(Identify, endpoint_id=3, cluster_type=ClusterType.Server)
    .adds(Identify, endpoint_id=3, cluster_type=ClusterType.Client)
    .adds(OnOff, endpoint_id=3, cluster_type=ClusterType.Client)
    .adds_endpoint(
        endpoint_id=4,
        profile_id=zha.PROFILE_ID,
        device_type=zha.DeviceType.ON_OFF_LIGHT_SWITCH,
    )
    .adds(Basic, endpoint_id=4, cluster_type=ClusterType.Server)
    .adds(Identify, endpoint_id=4, cluster_type=ClusterType.Server)
    .adds(Identify, endpoint_id=4, cluster_type=ClusterType.Client)
    .adds(OnOff, endpoint_id=4, cluster_type=ClusterType.Client)
    .device_automation_triggers(
        {
            (SHORT_PRESS, "Button 1"): {
                COMMAND: COMMAND_TOGGLE,
                CLUSTER_ID: OnOff.cluster_id,
                ENDPOINT_ID: 3,
            },
            (DOUBLE_PRESS, "Button 1"): {
                COMMAND: COMMAND_ON,
                CLUSTER_ID: OnOff.cluster_id,
                ENDPOINT_ID: 3,
            },
            (LONG_PRESS, "Button 1"): {
                COMMAND: COMMAND_OFF,
                CLUSTER_ID: OnOff.cluster_id,
                ENDPOINT_ID: 3,
            },
            (SHORT_PRESS, "Button 2"): {
                COMMAND: COMMAND_TOGGLE,
                CLUSTER_ID: OnOff.cluster_id,
                ENDPOINT_ID: 4,
            },
            (DOUBLE_PRESS, "Button 2"): {
                COMMAND: COMMAND_ON,
                CLUSTER_ID: OnOff.cluster_id,
                ENDPOINT_ID: 4,
            },
            (LONG_PRESS, "Button 2"): {
                COMMAND: COMMAND_OFF,
                CLUSTER_ID: OnOff.cluster_id,
                ENDPOINT_ID: 4,
            },
        }
    )
    .enum(
        attribute_name=YandexSwitchClusterRelay.AttributeDefs.power_type.name,
        enum_class=YandexType_PowerType,
        cluster_id=YandexSwitchClusterRelay.cluster_id,
        translation_key="power_type",
        fallback_name="Power Type",
    )
    .enum(
        attribute_name=YandexSwitchClusterRelay.AttributeDefs.switch_type.name,
        enum_class=YandexType_SwitchType,
        cluster_id=YandexSwitchClusterRelay.cluster_id,
        endpoint_id=1,
        translation_key="switch_type",
        fallback_name="Switch Type",
    )
    .enum(
        attribute_name=YandexSwitchClusterRelay.AttributeDefs.switch_type.name,
        enum_class=YandexType_SwitchType,
        cluster_id=YandexSwitchClusterRelay.cluster_id,
        endpoint_id=2,
        translation_key="switch_type",
        fallback_name="Switch Type",
    )
    .switch(
        attribute_name=YandexSwitchClusterRelay.AttributeDefs.interlock.name,
        cluster_id=YandexSwitchClusterRelay.cluster_id,
        translation_key="interlock",
        fallback_name="Interlock",
        off_value=YandexType_Interlock.Disabled,
        on_value=YandexType_Interlock.Enabled,
    )
    .add_to_registry()
)
