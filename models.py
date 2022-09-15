from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Agent:
    platform: str
    paw: str
    username: str
    host: str
    role: str = ""

    def from_dict(d):
        return Agent(
            d["platform"],
            d["paw"],
            d["username"],
            d["host"]
        )

class FieldType(Enum):
    int = auto()
    float = auto()
    text = auto()
    radio = auto()
    checkbox = auto()

@dataclass
class ContextField:
    name: str
    label: str
    type: FieldType
    required: bool
    affected: list

@dataclass
class IntField(ContextField):
    min: int
    max: int

@dataclass
class FloatField(ContextField):
    min: float
    max: float

@dataclass
class TextField(ContextField):
    pass

@dataclass
class FieldOption:
    value: str
    name: str
    checked: bool

@dataclass
class RadioField(ContextField):
    options: list