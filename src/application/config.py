from pydantic import BaseModel


class ChromeTask(BaseModel):
    url: str


class ChromeResults(BaseModel):
    url: str
    content: bytes


class ChromeResultList(ChromeResults):
    content: str
