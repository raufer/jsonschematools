from typing import Annotated, Literal, List, Optional

from pydantic import BaseModel, Field
from .node import Node, NodeType


class SummaryGuidelines(BaseModel):
    content_requirements: List[str] = Field(default=[], description="The content requirements for the summary.")
    style_guidelines: List[str] = Field(default=[], description="The style guidelines for the summary.")
    best_practices_examples: List[str] = Field(default=[], description="Best practices examples of a good summary")


class Summary(BaseModel):
    summary: Annotated[Optional[str], Field(
        default=None,
        # min_length=150,
        # max_length=800,
        description="A factual presentation of the company's key identifying characteristics, ownership structure, and operational setup with focus on verifiable information.. Should be between 150 and 800 characters.",
    )]


class GuidedSummaryData(BaseModel):
    guidelines: SummaryGuidelines = Field(description="The guidelines for the summary.")
    summary: Optional[Summary] = Field(default=None, description="The summary of the analysis.")


class GuidedSummary(Node):
    type: Literal[NodeType.GUIDED_SUMMARY] = NodeType.GUIDED_SUMMARY
    data: Optional[GuidedSummaryData] = Field(default=None, description="The data for the guided summary.")
