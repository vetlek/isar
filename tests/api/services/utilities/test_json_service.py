import json
from typing import Any

import pytest

from isar.models.communication.messages import StartMessage, StopMessage
from isar.services.utilities.json_service import EnhancedJSONEncoder, JsonService


class TestJsonService:
    @pytest.mark.parametrize(
        "original_object",
        [
            StartMessage(message="help", started=False),
            StopMessage(message="Yes, sir!", stopped=True),
        ],
    )
    @pytest.mark.unittest
    def test_dataclass_to_object(self, original_object: Any):
        json_string: str = json.dumps(original_object, cls=EnhancedJSONEncoder)
        as_object: Any = JsonService.to_object(json_string)
        assert as_object is not None
