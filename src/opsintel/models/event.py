from typing import ClassVar
from datetime import datetime

from pydantic import BaseModel, Field, model_validator

from .enums import EventStatus, EventType, Region, Service


class OperationalEvent(BaseModel):
    event_id: str = Field(min_length=1)

    timestamp: datetime

    event_type: EventType

    user_id: int | None = Field(default=None, gt=0)

    service: Service

    region: Region

    amount: float | None = Field(default=None, ge=0)

    latency_ms: float | None = Field(default=None, ge=0)

    status: EventStatus

    EVENT_SERVICE_MAP: ClassVar[dict[EventType, Service]] =  {
        EventType.ORDER_CREATED: Service.ORDER,
        EventType.ORDER_CANCELLED: Service.ORDER,
        EventType.PAYMENT_COMPLETED: Service.PAYMENT,
        EventType.PAYMENT_FAILED: Service.PAYMENT,
        EventType.DELIVERY_DELAYED: Service.DELIVERY,
        EventType.API_REQUEST: Service.API,
        EventType.API_ERROR: Service.API,
        EventType.LOGIN: Service.AUTHENTICATION,
        EventType.PRODUCT_VIEW: Service.API,
        EventType.INVENTORY_UPDATED: Service.INVENTORY,
    }

    @model_validator(mode="after")
    def validate_business_rules(self):
        if (
                self.event_type == EventType.PAYMENT_FAILED
                and self.status != EventStatus.FAILED
        ):
            raise ValueError(
                "PAYMENT_FAILED events must have FAILED status"
            )

        if (
                self.event_type == EventType.PAYMENT_COMPLETED
                and self.status != EventStatus.SUCCESS
        ):
            raise ValueError(
                "PAYMENT_COMPLETED events must have SUCCESS status"
            )

        if (
                self.event_type == EventType.API_ERROR
                and self.status != EventStatus.FAILED
        ):
            raise ValueError(
                "API_ERROR events must have FAILED status"
            )

        if (
                self.event_type == EventType.ORDER_CREATED
                and self.amount is None
        ):
            raise ValueError(
                "ORDER_CREATED events must have an amount"
            )

        if (
                self.event_type == EventType.API_REQUEST
                and self.latency_ms is None
        ):
            raise ValueError(
                "API_REQUEST events must have latency_ms"
            )

        expected_service = self.EVENT_SERVICE_MAP.get(self.event_type)

        if expected_service and self.service != expected_service:
            raise ValueError(
                f"{self.event_type.value} events must use "
                f"{expected_service.value} service"
            )

        return self
