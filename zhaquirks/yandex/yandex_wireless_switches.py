"""Support for YNDX-00534 and YNDX-00535 one-gang and two-gang wireless switches."""

from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import Basic, Identify, OnOff, Ota, PowerConfiguration

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
from zhaquirks.yandex import YANDEX


class YandexOneGangWirelessSwitch(CustomDevice):
    """YNDX-00534 one-gang wireless switch."""

    signature = {
        MODELS_INFO: [(YANDEX, "YNDX-00534")],
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=259
            # device_version=0
            # input_clusters=[0, 1, 3]
            # output_clusters=[3, 6, 25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    Ota.cluster_id,
                ],
            },
            # <SimpleDescriptor endpoint=2 profile=260 device_type=259
            # device_version=0
            # input_clusters=[0, 3]
            # output_clusters=[3, 6]>
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                ],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            # Down
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    Ota.cluster_id,
                ],
            },
            # Up
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                ],
            },
        }
    }

    device_automation_triggers = {
        (SHORT_PRESS, "Button (Down)"): {
            COMMAND: COMMAND_TOGGLE,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 1,
        },
        (DOUBLE_PRESS, "Button (Down)"): {
            COMMAND: COMMAND_ON,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 1,
        },
        (LONG_PRESS, "Button (Down)"): {
            COMMAND: COMMAND_OFF,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 1,
        },
        (SHORT_PRESS, "Button (Up)"): {
            COMMAND: COMMAND_TOGGLE,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 2,
        },
        (DOUBLE_PRESS, "Button (Up)"): {
            COMMAND: COMMAND_ON,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 2,
        },
        (LONG_PRESS, "Button (Up)"): {
            COMMAND: COMMAND_OFF,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 2,
        },
    }


class YandexTwoGangWirelessSwitch(CustomDevice):
    """YNDX-00535 two-gang wireless switch."""

    signature = {
        MODELS_INFO: [(YANDEX, "YNDX-00535")],
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=259
            # device_version=0
            # input_clusters=[0, 1, 3]
            # output_clusters=[3, 6, 25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    Ota.cluster_id,
                ],
            },
            # <SimpleDescriptor endpoint=2 profile=260 device_type=259
            # device_version=0
            # input_clusters=[0, 3]
            # output_clusters=[3, 6]>
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                ],
            },
            # <SimpleDescriptor endpoint=3 profile=260 device_type=259
            # device_version=0
            # input_clusters=[0, 3]
            # output_clusters=[3, 6]>
            3: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                ],
            },
            # <SimpleDescriptor endpoint=4 profile=260 device_type=259
            # device_version=0
            # input_clusters=[0, 3]
            # output_clusters=[3, 6]>
            4: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                ],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            # Button 1 Down
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    Ota.cluster_id,
                ],
            },
            # Button 2 Down
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                ],
            },
            # Button 1 Up
            3: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                ],
            },
            # Button 2 Up
            4: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                ],
            },
        }
    }

    device_automation_triggers = {
        (SHORT_PRESS, "Button 1 (Down)"): {
            COMMAND: COMMAND_TOGGLE,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 1,
        },
        (DOUBLE_PRESS, "Button 1 (Down)"): {
            COMMAND: COMMAND_ON,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 1,
        },
        (LONG_PRESS, "Button 1 (Down)"): {
            COMMAND: COMMAND_OFF,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 1,
        },
        (SHORT_PRESS, "Button 2 (Down)"): {
            COMMAND: COMMAND_TOGGLE,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 2,
        },
        (DOUBLE_PRESS, "Button 2 (Down)"): {
            COMMAND: COMMAND_ON,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 2,
        },
        (LONG_PRESS, "Button 2 (Down)"): {
            COMMAND: COMMAND_OFF,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 2,
        },
        (SHORT_PRESS, "Button 1 (Up)"): {
            COMMAND: COMMAND_TOGGLE,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 3,
        },
        (DOUBLE_PRESS, "Button 1 (Up)"): {
            COMMAND: COMMAND_ON,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 3,
        },
        (LONG_PRESS, "Button 1 (Up)"): {
            COMMAND: COMMAND_OFF,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 3,
        },
        (SHORT_PRESS, "Button 2 (Up)"): {
            COMMAND: COMMAND_TOGGLE,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 4,
        },
        (DOUBLE_PRESS, "Button 2 (Up)"): {
            COMMAND: COMMAND_ON,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 4,
        },
        (LONG_PRESS, "Button 2 (Up)"): {
            COMMAND: COMMAND_OFF,
            CLUSTER_ID: OnOff.cluster_id,
            ENDPOINT_ID: 4,
        },
    }
