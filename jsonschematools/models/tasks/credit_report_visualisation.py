from typing import Literal, List, Optional
from enum import Enum
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from pydantic import BaseModel, Field

from .task import Task, TaskType


class VisualisationType(str, Enum):
    LINE_PLOT = "LINE_PLOT"


class Series(BaseModel):
    name: str = Field(description="Name of the data series")
    y_values: List[float | None] = Field(description="List of y-axis values")


class VisualisationData(BaseModel):
    x_values: List[float | str] = Field(description="List of x-axis values")
    series: List[Series] = Field(description="List of data series to plot")


class Visualisation(BaseModel):
    title: str = Field(description="Title of the visualisation")
    description: str = Field(description="Description of the visualisation")
    type: Literal[VisualisationType.LINE_PLOT] = Field(default=VisualisationType.LINE_PLOT, description="Type of visualization")
    data: VisualisationData = Field(description="The actual plot data")


class CreditReportVisualisationData(BaseModel):
    visualisations: List[Visualisation] = Field(description="List of visualisations")


class CreditReportVisualisation(Task):
    type: Literal[TaskType.CREDIT_REPORT_VISUALISATION] = TaskType.CREDIT_REPORT_VISUALISATION
    data: Optional[CreditReportVisualisationData] = None
