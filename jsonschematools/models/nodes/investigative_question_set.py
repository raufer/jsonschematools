from typing import Literal, Optional, List

from pydantic import BaseModel, Field
from .node import Node, NodeType, NodeMetadata


class Reference(BaseModel):
    document_id: str = Field(description="The original document ID that was used to answer the question")
    document_filename: Optional[str] = Field(default=None, description="The filename of the original document that was used to answer the question")
    pages: list[str] = Field(default=[], description="The pages of the original document that were used to answer the question, if relevant")
    sections: list[str] = Field(default=[], description="The sections of the original document that were used to answer the question, if relevant")
    quotes: list[str] = Field(default=[], description="Relevant quotes from the original document")


class Answer(BaseModel):
    id: str = Field(description="The id of the question")
    answer: str = Field(description="The answer to the question")
    references: list[Reference] = Field(description="The references to the sources that were used to answer the question")


class Question(BaseModel):
    id: str
    question: str
    additional_considerations: Optional[str] = None
    answer: Optional[Answer] = None


class InformationGap(BaseModel):
    name: str
    description: str = Field(description="A detailed description of the information gap")


class RiskImplication(BaseModel):
    name: str
    description: str = Field(description="A detailed description of the risk implication")


class InvestigativeQuestionSetData(BaseModel):
    name: str 
    description: str 
    trigger_conditions: List[str] = []
    questions: List[Question] = []
    resolution_criteria: List[str] = []
    positive_example: str 
    negative_example: str 
    information_gaps: List[InformationGap] = Field(default=[], description="The list of critical information gaps that were identified")
    risk_implications: List[RiskImplication] = Field(default=[], description="The list of risk implications of the information gaps that were identified")


class InvestigativeQuestionSet(Node):
    type: Literal[NodeType.INVESTIGATIVE_QUESTION_SET] = NodeType.INVESTIGATIVE_QUESTION_SET
    data: InvestigativeQuestionSetData
    metadata: NodeMetadata = NodeMetadata(is_optional=True)
