from enum import Enum, auto
from typing import Any, Optional, List, Literal
from pydantic import BaseModel, Field, field_validator
from ..source import Source


class TaskType(str, Enum):
    CREDIT_REPORT_VISUALISATION = 'CREDIT_REPORT_VISUALISATION'


class Control(BaseModel):
    instructions: Optional[str] = None


class Task(BaseModel):
    type: TaskType
    description: Optional[str] = None
    control: Optional[Control] = None
    data: Optional[Any] = None

    def __str__(self):
        return f"Task(type={self.type})"

    def __repr__(self):
        return self.__str__()
