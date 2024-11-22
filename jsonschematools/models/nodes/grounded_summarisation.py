from typing import Literal, List, Optional

from pydantic import BaseModel, Field
from .node import Node, NodeType


class Criterion(BaseModel):
    name: str 
    description: str 
    justification: str 
    measurements: List[str] = []
    thresholds: List[str] = []
    positive_examples: List[str] = []
    negative_examples: List[str] = []


class PrimaryFindings(BaseModel):
    main_observations: List[str] = Field(
        description="Key observations extracted from the answers"
    )
    trends_patterns: List[str] = Field(
        description="Significant trends or patterns identified"
    )
    # strengths: List[str] = Field(
    #     description="Notable strengths identified"
    # )
    # weaknesses: List[str] = Field(
    #     description="Notable weaknesses identified"
    # )


class CriteriaAssessment(BaseModel):
    criterion: str = Field(
        description="Name of the criterion being assessed"
    )
    requirement: str = Field(
        description="The required threshold or condition"
    )
    actual: str = Field(
        description="The actual observed value or condition"
    )
    assessment: str = Field(
        description="Evaluation of how the actual value compares to the requirement. Be detailed and specific."
    )


class RiskImplications(BaseModel):
    key_risks: List[str] = Field(
        description="Key risks identified in this category"
    )
    mitigating_factors: List[str] = Field(
        description="Factors that help mitigate identified risks"
    )
    attention_areas: List[str] = Field(
        description="Areas requiring special attention or monitoring"
    )


class CategoryObservation(BaseModel):
    category_name: str = Field(
        description="Name of the analysis category"
    )
    primary_findings: PrimaryFindings = Field(
        description="Primary findings for this category"
    )
    criteria_alignment: List[CriteriaAssessment] = Field(default=[],
        description="How observations align with each criterion"
    )
    # risk_implications: RiskImplications = Field(
    #     description="Risk implications for this category"
    # )


class RiskFactors(BaseModel):
    primary_strengths: List[str] = Field(
        default=[],
        description="Primary risk strengths identified"
    )
    key_concerns: List[str] = Field(
        default=[],
        description="Key risk concerns identified"
    )
    monitoring_points: List[str] = Field(
        default=[],
        description="Points requiring ongoing monitoring"
    )


class Summary(BaseModel):
    category_observations: List[CategoryObservation] = Field(
        default=[],
        description="Observations organized by category"
    )
    # risk_factors: RiskFactors = Field(
    #     description="Summary of risk factors"
    # )
    final_summary: str = Field(
        description="Final summary consolidating the most important findings"
    )



class GroundedSummarisationData(BaseModel):
    criteria: List[Criterion] = []
    summary: Optional[Summary] = None


class GroundedSummarisation(Node):
    type: Literal[NodeType.GROUNDED_SUMMARISATION] = NodeType.GROUNDED_SUMMARISATION
    data: GroundedSummarisationData = GroundedSummarisationData()
