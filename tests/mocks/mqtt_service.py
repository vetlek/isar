from typing import Optional

from paho.mqtt.properties import readUTF

from isar.models.communication.messages import StartMessage, StopMessage
from isar.models.mission import Mission
from isar.services.service_connections.mqtt.mqtt_service_interface import (
    MQTTServiceInterface,
)
from isar.state_machine.states_enum import States
from robot_interface.models.mission.status import MissionStatus
from robot_interface.models.mission.step import Step


class MQTTServiceMock(MQTTServiceInterface):
    def is_connected(self) -> bool:
        return True

    def time_since_disconnect(self) -> float:
        return 0.0

    def publish_mission_status_message(self, status: MissionStatus) -> None:
        return

    def publish_mission_in_progress_message(self, mission_in_progress: bool) -> None:
        return

    def publish_current_mission_instance_id(
        self, mission_instance_id: Optional[int]
    ) -> None:
        return

    def publish_current_mission_step(self, mission_step: Optional[Step]) -> None:
        return

    def publish_mission_schedule(self, mission_schedule: Mission) -> None:
        return

    def publish_current_state(self, state: States) -> None:
        return

    def publish_start_mission(self, mission: Mission) -> None:
        return

    def publish_start_mission_ack(self, start_mission_message: StartMessage) -> None:
        return

    def publish_stop_mission(self) -> None:
        return

    def publish_stop_mission_ack(self, stop_mission_message: StopMessage) -> None:
        return

    def subscribe_start_mission(self, callback=None) -> None:
        return

    def subscribe_start_mission_ack(self, callback=None) -> None:
        return

    def subscribe_stop_mission(self, callback=None) -> None:
        return

    def subscribe_stop_mission_ack(self, callback=None) -> None:
        return
