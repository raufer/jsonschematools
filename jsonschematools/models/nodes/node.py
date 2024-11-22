from enum import Enum, auto
from typing import Any, Optional, List, Literal
from pydantic import BaseModel, Field, field_validator

from ..tasks.union import Task
from ..source import Source


class NodeType(str, Enum):
    DELIBERATION_REPORT = 'DELIBERATION_REPORT'
    GUIDED_SUMMARY = 'GUIDED_SUMMARY'
    GROUNDED_SUMMARISATION = 'GROUNDED_SUMMARISATION'
    REPORT_SUMMARY = 'REPORT_SUMMARY'
    QUESTION_SET = 'QUESTION_SET'
    QUESTION_CONSOLIDATION = 'QUESTION_CONSOLIDATION'
    INVESTIGATIVE_QUESTION_SET = 'INVESTIGATIVE_QUESTION_SET'


class Control(BaseModel):
    instructions: Optional[str] = None


class NodeMetadata(BaseModel):
    level: Optional[int] = None
    is_computed: bool = False
    is_optional: bool = False


class TaskRequest(BaseModel):
    task: Task = Field(discriminator="type")
    data: Optional[Any] = None


class Node(BaseModel):
    id: str 
    name: str 
    description: Optional[str] = None
    type: NodeType
    sources: List[Source] = []
    control: Optional[Control] = None
    tasks: List[TaskRequest] = []
    data: Optional[Any] = None
    children: List[str] = []
    metadata: NodeMetadata = NodeMetadata()

    @field_validator('control', mode='before')
    def validate_control(cls, v):
        if isinstance(v, dict) and all(not v[k] for k in v):
            return None
        return v

    def __str__(self):
        return f"{self.id} - {self.name}"

    def __repr__(self):
        return self.__str__()
