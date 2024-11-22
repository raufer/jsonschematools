from enum import Enum, auto

from .grounded_summarisation import GroundedSummarisation
from .investigative_question_set import InvestigativeQuestionSet
from .question_set import QuestionSet
from .question_consolidation import QuestionConsolidation
from .report_summary import ReportSummary
from .deliberation_report import DeliberationReport 
from .guided_summary import GuidedSummary



Node = (
    GroundedSummarisation
    | QuestionSet
    | QuestionConsolidation
    | InvestigativeQuestionSet
    | ReportSummary
    | DeliberationReport
    | GuidedSummary
)
