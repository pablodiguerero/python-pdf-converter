from io import BytesIO
from typing import List
from base64 import b64encode

from fastapi import APIRouter, HTTPException
from fastapi.params import Body, Query
from starlette.responses import StreamingResponse

from application.config import ChromeTask, ChromeResultList
from utils.chrome import get_files

from starlette.status import HTTP_400_BAD_REQUEST


chrome = APIRouter()


@chrome.post(
    "/chrome/screenshot/",
    responses={HTTP_400_BAD_REQUEST: {"description": "Bad request, check URLs"}},
)
async def screenshot(body: ChromeTask = Body(...)) -> StreamingResponse:
    results = await get_files([body])

    if not len(results):
        raise HTTPException(status_code=400, detail=f"Bad URL in task")

    file = results[0]

    return StreamingResponse(BytesIO(file.content), media_type="application/pdf")


@chrome.get(
    "/chrome/screenshot/",
    responses={HTTP_400_BAD_REQUEST: {"description": "Bad request, check URLs"}},
)
async def get_screenshot(url: str = Query(...)) -> StreamingResponse:
    return await screenshot(body=ChromeTask(url=url))


@chrome.post("/chrome/screenshot-pulls/", response_model=List[ChromeResultList])
async def screenshot_pulls(body: List[ChromeTask] = Body(...)):
    results = await get_files(body)
    return [ChromeResultList(url=x.url, content=b64encode(x.content)) for x in results]
