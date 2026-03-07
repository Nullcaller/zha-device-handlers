"""Support for YNDX-00591 and YNDX-00592 curtain motors."""

from __future__ import annotations

from collections.abc import Coroutine
from typing import Any, Final

from zigpy.profiles import zgp, zha
from zigpy.quirks import CustomCluster, CustomDevice
import zigpy.types as t
from zigpy.zcl.clusters.closures import WindowCovering
from zigpy.zcl.clusters.general import (
    Basic,
    GreenPowerProxy,
    Groups,
    Identify,
    Ota,
    Scenes,
)
from zigpy.zcl.clusters.homeautomation import Diagnostic
from zigpy.zcl.foundation import (
    ZCL_CLUSTER_REVISION_ATTR,
    GeneralCommand,
    ZCLAttributeDef,
)

from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)
from zhaquirks.yandex import YANDEX, YANDEX_MANUFACTURER_CODE_2, YandexType_VelocityLift


class YandexWindowCovering(CustomCluster, WindowCovering):
    """Window covering cluster for YNDX-00591 and YNDX-00592 curtain motors with Yandex-specific attributes and commands."""

    CMD_UP_OPEN = WindowCovering.commands_by_name["up_open"].id
    CMD_DOWN_CLOSE = WindowCovering.commands_by_name["down_close"].id

    manufacturer_id_override = YANDEX_MANUFACTURER_CODE_2

    class AttributeDefs(WindowCovering.AttributeDefs):
        """Attribute definitions."""

        velocity_lift: Final = ZCLAttributeDef(
            id=WindowCovering.AttributeDefs.velocity_lift.id,
            type=YandexType_VelocityLift,
            access="rw",
        )
        unknown_attribute_61440: Final = ZCLAttributeDef(
            id=0xF000,
            type=t.Bool,
            access="rw",
            is_manufacturer_specific=True,
        )
        max_position: Final = ZCLAttributeDef(
            id=0xF001,
            type=t.uint8_t,
            access="rw",
            is_manufacturer_specific=True,
        )
        min_position: Final = ZCLAttributeDef(
            id=0xF002,
            type=t.uint8_t,
            access="rw",
            is_manufacturer_specific=True,
        )
        cluster_revision: Final = ZCL_CLUSTER_REVISION_ATTR

    async def command(
        self,
        command_id: GeneralCommand | int | t.uint8_t,
        *args,
        manufacturer: int | t.uint16_t | None = None,
        expect_reply: bool = True,
        tsn: int | t.uint8_t | None = None,
        **kwargs: Any,
    ) -> Coroutine:
        """Reverse the open and close commands."""

        if command_id == self.CMD_UP_OPEN:
            command_id = self.CMD_DOWN_CLOSE
        elif command_id == self.CMD_DOWN_CLOSE:
            command_id = self.CMD_UP_OPEN

        return await super().command(
            command_id,
            *args,
            manufacturer=manufacturer,
            expect_reply=expect_reply,
            tsn=tsn,
            **kwargs,
        )


class YandexCurtainMotor(CustomDevice):
    """YNDX-00591 and YNDX-00592 curtain motors."""

    signature = {
        MODELS_INFO: [(YANDEX, "YNDX-00591"), (YANDEX, "YNDX-00592")],
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=514
            # device_version=0
            # input_clusters=[0, 3, 4, 5, 258, 2821]
            # output_clusters=[3, 25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    WindowCovering.cluster_id,
                    Diagnostic.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Identify.cluster_id, Ota.cluster_id],
            },
            # <SimpleDescriptor endpoint=242 profile=41440 device_type=97
            # device_version=0
            # input_clusters=[]
            # output_clusters=[33]>
            242: {
                PROFILE_ID: zgp.PROFILE_ID,
                DEVICE_TYPE: zgp.DeviceType.PROXY_BASIC,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.WINDOW_COVERING_DEVICE,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    YandexWindowCovering,
                    Diagnostic.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Identify.cluster_id, Ota.cluster_id],
            },
            242: {
                PROFILE_ID: zgp.PROFILE_ID,
                DEVICE_TYPE: zgp.DeviceType.PROXY_BASIC,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }
