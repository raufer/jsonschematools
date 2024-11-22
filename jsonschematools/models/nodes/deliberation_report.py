from typing import Annotated, Literal, List, Optional

from pydantic import BaseModel, Field
from .node import Node, NodeType


class SectionSummary(BaseModel):
    """Represents a summary of a specific section within a report."""
    
    title: Annotated[str, Field(
        min_length=1,
        max_length=200,
        description="The title of the section. Must be between 1 and 200 characters.",
        examples=["Financial Performance", "Market Analysis"]
    )]
    
    summary: Annotated[str, Field(
        min_length=50,
        max_length=2000,
        description="A comprehensive summary of the section's content. Should be between 50 and 2000 characters.",
        examples=["The company showed strong financial performance in Q4 2023, with revenue growing 15% YoY..."]
    )]


class KeyMetric(BaseModel):
    metric: Annotated[str, Field(
        min_length=1,
        max_length=100,
        description="The metric name.",
        examples=["Revenue", "Market share", "Customer satisfaction"]
    )]
    value: Annotated[str, Field(
        min_length=1,
        max_length=100,
        description="The metric value.",
        examples=["100M", "23%", "€1.74M (2023, +79.5% YoY)"]
    )]


class Summary(BaseModel):
    company_overview: Annotated[str, Field(
        min_length=100,
        max_length=3000,
        description="A detailed overview of the company, including its business model, market position, and current status.",
        examples=["XYZ Corp is a leading technology company specializing in cloud computing solutions..."]
    )]
    key_metrics: Annotated[List[KeyMetric], Field(
        min_length=1,
        max_length=10,
        description="A list of 1-10 crucial quantitative and qualitative metrics highlighted in the report.",
        examples=[["Revenue growth: 15% YoY", "Market share: 23%", "Customer satisfaction: 4.8/5"]]
    )] 
    key_strengths: Annotated[List[str], Field(
        min_length=1,
        max_length=10,
        description="A list of 1-10 major competitive advantages or positive aspects identified in the report.",
        examples=[["Strong market position", "Innovative product pipeline", "Robust financial health"]]
    )]
    key_risks: Annotated[List[str], Field(
        min_length=1,
        max_length=10,
        description="A list of 1-10 significant risks or challenges faced by the company.",
        examples=[["Increasing competition", "Regulatory changes", "Supply chain vulnerabilities"]]
    )]
    
    sections_summary: Annotated[List[SectionSummary], Field(
        min_length=1,
        max_length=20,
        description="A list of 1-20 detailed summaries for each major section of the report.",
    )]
    
    final_summary: Annotated[str, Field(
        min_length=200,
        max_length=5000,
        description="A comprehensive conclusion that synthesizes all key findings and provides an overall assessment.",
        examples=["Based on our analysis, XYZ Corp demonstrates strong market positioning with significant growth potential..."]
    )]



class DeliberationReportData(BaseModel):
    summary: Optional[Summary] = Field(None, description="The summary report of the analysis.")


class DeliberationReport(Node):
    type: Literal[NodeType.DELIBERATION_REPORT] = NodeType.DELIBERATION_REPORT
    data: DeliberationReportData = Field(default=DeliberationReportData(), description="The data for the deliberation report.")
