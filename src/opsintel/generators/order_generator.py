import random
from datetime import datetime, timezone

from opsintel.generators.id_generator import EventIdGenerator
from opsintel.models.event import OperationalEvent
from opsintel.models.enums import EventStatus, EventType, Region, Service


class OrderGenerator:

    def __init__(self, event_id_generator: EventIdGenerator):
        self.event_id_generator = event_id_generator

    def generate(self) -> OperationalEvent:
        return OperationalEvent(
            event_id=self.event_id_generator.generate(),
            timestamp=datetime.now(timezone.utc),
            event_type=EventType.ORDER_CREATED,
            user_id=random.randint(1, 10000),
            service=Service.ORDER,
            region=random.choice(list(Region)),
            amount=round(random.uniform(50, 2000), 2),
            latency_ms=None,
            status=EventStatus.SUCCESS,
        )