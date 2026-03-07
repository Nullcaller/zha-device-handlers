"""Support for YNDX-00537 and YNDX-00538 single-channel and dual-channel relays."""

from typing import Final

from zigpy.profiles import zha
from zigpy.quirks import CustomCluster, CustomDevice
from zigpy.zcl.clusters.general import Basic, Identify, OnOff, Ota
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
    DEVICE_TYPE,
    DOUBLE_PRESS,
    ENDPOINT_ID,
    ENDPOINTS,
    INPUT_CLUSTERS,
    LONG_PRESS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
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


class YandexSingleRelay(CustomDevice):
    """YNDX-00537 single-channel relay."""

    signature = {
        MODELS_INFO: [(YANDEX, "YNDX-00537")],
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=0
            # input_clusters=[0, 3, 6, 64515]
            # output_clusters=[25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    YandexSwitchClusterRelay.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    YandexSwitchClusterRelay,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
            # Button (decoupled)
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Identify.cluster_id, OnOff.cluster_id],
            },
        },
    }

    device_automation_triggers = {
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


class YandexDualRelay(CustomDevice):
    """YNDX-00538 dual-channel relay."""

    signature = {
        MODELS_INFO: [(YANDEX, "YNDX-00538")],
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=0
            # input_clusters=[0, 3, 6, 64515]
            # output_clusters=[25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    YandexSwitchClusterRelay.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
            # <SimpleDescriptor endpoint=2 profile=260 device_type=256
            # device_version=0
            # input_clusters=[0, 3, 6, 64515]
            # output_clusters=[]>
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    YandexSwitchClusterRelay.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    YandexSwitchClusterRelay,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    YandexSwitchClusterRelay,
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id],
            },
            # Button 1
            3: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Identify.cluster_id, OnOff.cluster_id],
            },
            # Button 2
            4: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Identify.cluster_id, OnOff.cluster_id],
            },
        },
    }

    device_automation_triggers = {
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
