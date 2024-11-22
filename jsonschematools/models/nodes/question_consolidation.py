from typing import Literal, Optional, List

from pydantic import BaseModel, Field
from .node import Node, NodeType


class Reference(BaseModel):
    document_id: str = Field(description="The original document ID that was used to answer the question")
    document_filename: Optional[str] = Field(default=None, description="The filename of the original document that was used to answer the question")
    pages: list[str] = Field(default=[], description="The pages of the original document that were used to answer the question, if relevant")
    sections: list[str] = Field(default=[], description="The sections of the original document that were used to answer the question, if relevant")
    quotes: list[str] = Field(default=[], description="Relevant quotes from the original document")


class Answer(BaseModel):
    id: str = Field(description="The id of the question")
    inconsistencies: list[str] = Field(default=[], description="The inconsistencies found in the answersj, if any")
    answer: str = Field(description="The answer to the question")
    references: list[Reference] = Field(description="The references to the sources that were used to answer the question")


class Question(BaseModel):
    id: str
    question: str
    additional_considerations: Optional[str] = None
    answer: Optional[Answer] = None


class QuestionConsolidationData(BaseModel):
    questions: List[Question] = []


class QuestionConsolidation(Node):
    type: Literal[NodeType.QUESTION_CONSOLIDATION] = NodeType.QUESTION_CONSOLIDATION
    data: Optional[QuestionConsolidationData] = None
