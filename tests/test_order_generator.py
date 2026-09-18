from opsintel.generators.order_generator import OrderGenerator
from opsintel.models.enums import EventStatus, EventType, Service


def test_generate_order():
    event_id_generator = EventIdGenerator()
    generator = OrderGenerator(event_id_generator)

    event = generator.generate()

    assert event.event_type is EventType.ORDER_CREATED
    assert event.service == Service.ORDER
    assert event.status == EventStatus.SUCCESS

    assert event.user_id is not None
    assert event.amount is not None
    assert event.amount > 0

from opsintel.generators.id_generator import EventIdGenerator


def test_event_ids_are_unique():
    id_generator = EventIdGenerator()

    ids = [
        id_generator.generate()
        for _ in range(1000)
    ]

    assert len(ids) == len(set(ids))