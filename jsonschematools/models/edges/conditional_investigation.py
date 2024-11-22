from typing import Literal, Optional, List

from pydantic import BaseModel, Field
from .edge import Edge, EdgeType


class TriggerEvaluation(BaseModel):
    """Represents the evaluation of a single trigger condition"""
    trigger_name: str = Field(description="Name or description of the trigger being evaluated")
    evidence: List[str] = Field(default=[], description="List of evidence points considered for this trigger")
    is_triggered: bool = Field(default=False, description="Whether the trigger condition was met")
    confidence_level: float = Field(default=0.0, ge=0, le=1, description="Confidence level from 0 to 1")


class SupportingEvidence(BaseModel):
    """Contains additional context and verification details"""
    key_data_points: List[str] = Field(default=[], description="List of key data points referenced in analysis")
    verification_methods: List[str] = Field(default=[], description="Methods used to verify the data and conclusions")
    additional_context: Optional[str] = Field(default=None, description="Any additional context or notes")


class TriggerDecision(BaseModel):
    trigger_evaluations: List[TriggerEvaluation] = Field(default=[], description="List of all trigger evaluations")
    supporting_evidence: List[SupportingEvidence] = Field(default=[], description="Supporting analysis and context")
    justification: str = Field(default="", description="Detailed justification for the decision")
    trigger_decision: bool = Field(default=False, description="Whether deeper analysis is warranted")


class Question(BaseModel):
    id: str
    question: str 
    additional_considerations: Optional[str] = None


class ConditionalInvestigationData(BaseModel):
    name: str 
    description: str 
    trigger_conditions: List[str] = []
    questions: List[Question] = []
    resolution_criteria: List[str] = []
    positive_example: str 
    negative_example: str 
    decision: Optional[TriggerDecision] = None


class ConditionalInvestigation(Edge, frozen=True):
    type: Literal[EdgeType.CONDITIONAL_INVESTIGATION] = EdgeType.CONDITIONAL_INVESTIGATION
    data: ConditionalInvestigationData
