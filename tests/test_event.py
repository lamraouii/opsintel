from datetime import datetime

import pytest
from pydantic import ValidationError
from opsintel.models.event import OperationalEvent
from opsintel.models.enums import EventStatus, EventType, Region, Service


def test_valid_event():
    event = OperationalEvent(
        event_id="evt_000001",
        timestamp=datetime.now(),
        event_type=EventType.PAYMENT_COMPLETED,
        user_id=4821,
        service=Service.PAYMENT,
        region=Region.CASABLANCA,
        amount=742.50,
        latency_ms=183,
        status=EventStatus.SUCCESS,
    )

    assert event.event_id == "evt_000001"
    assert event.status == EventStatus.SUCCESS

def test_payment_failed_must_have_failed_status():
    with pytest.raises(ValidationError):
        OperationalEvent(
            event_id="evt_000003",
            timestamp=datetime.now(),
            event_type=EventType.PAYMENT_FAILED,
            user_id=100,
            service=Service.PAYMENT,
            region=Region.RABAT,
            amount=200,
            status=EventStatus.SUCCESS,
        )

def test_order_created_requires_amount():
    with pytest.raises(ValidationError):
        OperationalEvent(
            event_id="evt_000004",
            timestamp=datetime.now(),
            event_type=EventType.ORDER_CREATED,
            user_id=100,
            service=Service.ORDER,
            region=Region.RABAT,
            status=EventStatus.SUCCESS,
        )

def test_event_service_consistency():
    with pytest.raises(ValidationError):
        OperationalEvent(
            event_id="evt_000005",
            timestamp=datetime.now(),
            event_type=EventType.PAYMENT_FAILED,
            user_id=100,
            service=Service.INVENTORY,
            region=Region.RABAT,
            amount=200,
            status=EventStatus.FAILED,
        )