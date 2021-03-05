from typing import Optional
from pydantic import BaseModel


class ChromeTask(BaseModel):
    url: str
    delay: Optional[int] = 0


class ChromeResults(BaseModel):
    url: str
    content: bytes


class ChromeResultList(ChromeResults):
    content: str
