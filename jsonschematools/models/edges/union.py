from .simple_edge import SimpleEdge
from .conditional_investigation import ConditionalInvestigation


Edge = (
    ConditionalInvestigation
    | SimpleEdge
)
