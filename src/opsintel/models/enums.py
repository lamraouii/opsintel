from enum import Enum


class EventType(str, Enum):
    ORDER_CREATED = "ORDER_CREATED"
    PAYMENT_COMPLETED = "PAYMENT_COMPLETED"
    PAYMENT_FAILED = "PAYMENT_FAILED"
    ORDER_CANCELLED = "ORDER_CANCELLED"
    DELIVERY_DELAYED = "DELIVERY_DELAYED"
    API_REQUEST = "API_REQUEST"
    API_ERROR = "API_ERROR"
    LOGIN = "LOGIN"
    PRODUCT_VIEW = "PRODUCT_VIEW"
    INVENTORY_UPDATED = "INVENTORY_UPDATED"


class Service(str, Enum):
    ORDER = "order"
    PAYMENT = "payment"
    DELIVERY = "delivery"
    INVENTORY = "inventory"
    AUTHENTICATION = "authentication"
    API = "api"


class Region(str, Enum):
    CASABLANCA = "Casablanca"
    RABAT = "Rabat"
    OUJDA = "Oujda"
    MARRAKECH = "Marrakech"
    TANGIER = "Tangier"
    FES = "Fes"


class EventStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PENDING = "PENDING"