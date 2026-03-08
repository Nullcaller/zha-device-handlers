"""Support for YNDX-00534 and YNDX-00535 one-gang and two-gang wireless switches."""

from zigpy.quirks.v2 import QuirkBuilder
from zigpy.zcl.clusters.general import OnOff

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
from zhaquirks.yandex import YANDEX

(
    QuirkBuilder(YANDEX, "YNDX-00534")
    .device_automation_triggers(
        {
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
    )
    .add_to_registry()
)
(
    QuirkBuilder(YANDEX, "YNDX-00535")
    .device_automation_triggers(
        {
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
    )
    .add_to_registry()
)
