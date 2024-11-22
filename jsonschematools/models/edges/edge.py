from enum import Enum, auto

from typing import Optional, Any
from pydantic import BaseModel, Field


class EdgeType(str, Enum):
    CONDITIONAL_INVESTIGATION = 'CONDITIONAL_INVESTIGATION'
    SIMPLE_EDGE = 'SIMPLE_EDGE'


class EdgeMetadata(BaseModel):
    is_computed: bool = False
    is_optional: bool = False


class Edge(BaseModel, frozen=True):
    src: str 
    dst: str 
    type: Optional[str] = None
    data: Optional[Any] = None
    metadata: EdgeMetadata = EdgeMetadata()

    def __str__(self) -> str:
        return f"Edge: {self.src} -> {self.dst}"

    def __repr__(self) -> str:
        return self.__str__()
