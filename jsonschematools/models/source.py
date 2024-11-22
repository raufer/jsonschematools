from typing import List, Optional
from pydantic import BaseModel


class Source(BaseModel):
    id: Optional[str] = None
    type: str 
    subtype: str 
    sections: List[str] = []

    def model_post_init(self, __context):
        if not self.id:
            self.id = f"{self.type}:{self.subtype}"


class UnknownSource(Source):
    id: str = ""
    type: str = "UNKNOWN"
    subtype: str = "UNKNOWN"
