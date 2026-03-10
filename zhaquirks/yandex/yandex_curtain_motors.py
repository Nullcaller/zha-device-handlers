"""Support for YNDX-00591 and YNDX-00592 curtain motors."""

from __future__ import annotations

from collections.abc import Coroutine
from typing import Any, Final

from zigpy.quirks import CustomCluster
from zigpy.quirks.v2 import QuirkBuilder
from zigpy.quirks.v2.homeassistant.number import NumberDeviceClass
import zigpy.types as t
from zigpy.zcl.clusters.closures import WindowCovering
from zigpy.zcl.foundation import (
    ZCL_CLUSTER_REVISION_ATTR,
    GeneralCommand,
    ZCLAttributeDef,
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
            access="r",
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


(
    QuirkBuilder(YANDEX, "YNDX-00591")
    .replaces(YandexWindowCovering)
    .applies_to(YANDEX, "YNDX-00591")
    .applies_to(YANDEX, "YNDX-00592")
    .enum(
        attribute_name=YandexWindowCovering.AttributeDefs.velocity_lift.name,
        enum_class=YandexType_VelocityLift,
        cluster_id=YandexWindowCovering.cluster_id,
        translation_key="velocity_lift",
        fallback_name="Velocity (Lift)",
    )
    .number(
        attribute_name=YandexWindowCovering.AttributeDefs.max_position.name,
        cluster_id=YandexWindowCovering.cluster_id,
        min_value=0,
        max_value=255,
        step=1,
        device_class=NumberDeviceClass.DISTANCE,
        translation_key="max_position",
        fallback_name="Maximum Position",
    )
    .number(
        attribute_name=YandexWindowCovering.AttributeDefs.min_position.name,
        cluster_id=YandexWindowCovering.cluster_id,
        min_value=0,
        max_value=255,
        step=1,
        device_class=NumberDeviceClass.DISTANCE,
        translation_key="min_position",
        fallback_name="Minimum Position",
    )
    .add_to_registry()
)
