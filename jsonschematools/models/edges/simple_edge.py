from typing import Literal, Optional, List

from pydantic import BaseModel, Field
from .edge import Edge
from .edge import Edge, EdgeType


class SimpleEdge(Edge):
    type: Literal[EdgeType.SIMPLE_EDGE] = EdgeType.SIMPLE_EDGE
